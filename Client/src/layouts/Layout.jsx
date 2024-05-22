import { Outlet } from "react-router-dom";
import NavBar from "../components/NavBar";
import SearchBar from "../components/SearchBar";
import Login from "../components/Login";
import ShoppingCartLogo from "../components/ShoppingCartLogo";

const Layout = () => {
  return (
    <>
      <header>
        <div className="flex w-full flex-row items-center py-10">
          <section className="flex flex-row w-2/3">
            <SearchBar />
          </section>
          <section className="flex flex-row w-1/3">
            <ShoppingCartLogo />
            <Login />
          </section>
        </div>
        <NavBar />
      </header>
      <main className="mt-20 mx-auto max-w-7xl p-10 bg-white shadow">
        <Outlet />
      </main>
    </>
  );
};

export default Layout;
