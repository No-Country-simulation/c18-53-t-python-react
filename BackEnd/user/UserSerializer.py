from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken , AccessToken
from rest_framework_simplejwt.exceptions import TokenError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'user_type', 'is_active', 'is_staff', 'date_joined']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid login credentials")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'")
        
        data['user'] = user
        return data
    
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        self.token = data['refresh']
        return data

    def save(self, **kwargs):
        try:
            # Invalidar el token de actualización
            refresh_token = RefreshToken(self.token)
            print(refresh_token)
            refresh_token.blacklist()
            try:
                access_token = AccessToken(refresh_token.access_token)
                print(access_token)
                # Eliminar el token de acceso de la lista de OutstandingTokens
                OutstandingToken.objects.filter(token=access_token).delete()
            except TokenError:
                pass 
            
        except TokenError as e:
            raise serializers.ValidationError(str(e))