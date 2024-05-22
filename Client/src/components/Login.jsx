import { RiAccountBoxFill } from "react-icons/ri";

const Login = () => {
  return (
    <div className="flex items-center w-2/3">
      <button className="bg-pink-700 h-10 flex flex-row items-center rounded-md w-52 justify-center">
        <RiAccountBoxFill className="h-8 w-8 text-white" />
        <p className="uppercase font-extrabold ml-2 text-white">
          Iniciar sesión
        </p>
      </button>
    </div>
  );
};

export default Login;
