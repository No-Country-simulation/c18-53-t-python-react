from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status , generics
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .UserSerializer import UserSerializer , LoginSerializer , LogoutSerializer
from user.utils import send_confirmation_email

class UserViewSet(viewsets.ModelViewSet):
    permission_classes =[]
    serializer_class = UserSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active= True, user_type='client')
        else :
            return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True , user_type='client').first()
        
    def get_object(self):
        pk = self.kwargs.get('pk')
        queryset = User.objects.all()
        user = queryset.filter(id=pk).first()
        if user is None:
            raise NotFound(detail={"error": f"No user with ID {pk} matches the given query."})
        if not user.is_active:
            raise NotFound(detail={"error": f"User with ID {pk} is deactivated."})
        return user
        
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user =serializer.save()
            if user:
                send_confirmation_email(user)
                refresh = RefreshToken.for_user(user)
                response_data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': {
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'user_type': user.user_type,
                    }
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            return Response({'message':'falta validad tu cuenta con tu correo'}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            customer_serializer =self.serializer_class(self.get_queryset(pk),data= request.data, partial=True)
            if customer_serializer.is_valid():
                customer_serializer.save()
                print(request.data)
                return Response(customer_serializer.data , status= status.HTTP_200_OK)
            return Response(customer_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        customer = self.get_queryset().filter(id=pk).first()
        if customer:
            customer.is_active = False
            customer.save()
            return Response({'message': 'Customer eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un customer con esos datos'}, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(generics.CreateAPIView):
    permission_classes =[]
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        if user.is_active and user.user_type == 'client':
            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'user_type': user.user_type,
                }
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "User account is not active."}, status=status.HTTP_401_UNAUTHORIZED)
        
class LogoutView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class ConfirmEmailView(APIView):
    def get(self, request, email, token, *args, **kwargs):
        try:
            user = User.objects.get(email=email, confirmation_token=token)
            if user:
                user.is_email_confirmed = True
                user.confirmation_token = None  # Elimina el token de confirmación después de usarlo
                user.save()
                return Response({"detail": "Email confirmed successfully."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "Invalid confirmation link."}, status=status.HTTP_400_BAD_REQUEST)