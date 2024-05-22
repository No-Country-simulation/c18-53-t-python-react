import { useState } from "react";
import { Link } from "react-router-dom";
import { FaBars, FaTimes } from "react-icons/fa";

const Navbar = () => {
  const [nav, setNav] = useState(false);
  const handleClick = () => setNav(!nav);
  const navPages = [
    { text: "Home", to: "/" },
    { text: "Capilares", to: "/productos/capilares" },
    { text: "Manos y Uñas", to: "productos/manosyuñas" },
    { text: "Maquillaje", to: "/productos/maquillaje" },
    { text: "Equipamiento", to: "/productos/equipamiento" },
    { text: "Preguntas Frecuentes", to: "/preguntasfrecuentes" },
  ];

  return (
    <div className="fixed w-full h-[60px] px-4 bg-pink-700 text-white flex justify-between items-center text-2xl">
      {/* menu */}
      <ul className="hidden md:flex md:justify-around md:w-full md:items-center">
        {navPages.map((item, i) => (
          <li className="font-bold" key={i}>
            <Link to={item.to}>{item.text}</Link>
          </li>
        ))}
      </ul>

      {/* Hamburger */}
      <div onClick={handleClick} className="sm:hidden z-10">
        {!nav ? <FaBars /> : <FaTimes />}
      </div>

      {/* Mobile menu */}
      <ul
        className={
          !nav
            ? "hidden"
            : "absolute top-0 left-0 w-full bg-rose-700 flex flex-col py-10 items-center"
        }
      >
        {navPages.map((item, i) => (
          <li className="py-2 text-3xl" key={i}>
            <Link to={item.to}>{item.text}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Navbar;
