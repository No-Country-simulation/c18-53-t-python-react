import { RiAccountBoxFill } from "react-icons/ri";

const Login = () => {
  return (
    <div className="flex gap-6 font-light text-[15px] text-nowrap">
      <button className="flex items-end">
        {/* <RiAccountBoxFill className="h-8 w-8" /> */}
        <p className="">
          Crear cuenta
        </p>
      </button>
      <button className="flex items-end">
        {/* <RiAccountBoxFill className="h-8 w-8" /> */}
        <p className="">
          Iniciar sesión
        </p>
      </button>
    </div>
  );
};

export default Login;
