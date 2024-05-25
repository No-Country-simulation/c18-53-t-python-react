import { Outlet } from "react-router-dom";
import NavBar from "../components/NavBar";
import SearchBar from "../components/SearchBar";
import Login from "../components/Login";
import ShoppingCartLogo from "../components/ShoppingCartLogo";
import { TbTruckDelivery } from 'react-icons/tb'

const Layout = () => {
  return (
    <>
      <header>
        <section className="flex items-center justify-center gap-2 font-inter text-base bg-[#e6e5ff] h-10 font-light">
          Con tu compra de $500.000 o más <TbTruckDelivery /> <span className="font-semibold">!ENVIO GRATIS!</span>
        </section>
        <div className="flex gap-4 w-full max-w-[1440px] mx-auto items-center py-5 px-[3%] justify-between ">
          <section>
            LOGO
          </section>
          <section className="max-[768px]:hidden">
            <SearchBar />
          </section>
          <section className="flex gap-4">
            <Login />
            <ShoppingCartLogo />
          </section>
        </div>
        <section className="hidden max-[768px]:block mb-4 px-[3%]">
          <SearchBar fill={true} />
        </section>
        <NavBar />
      </header>
      <main className="mt-20 mx-auto max-w-7xl p-10 bg-white shadow">
        <Outlet />
      </main>
    </>
  );
};

export default Layout;
