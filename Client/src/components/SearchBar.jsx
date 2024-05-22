import { FaSearch } from "react-icons/fa";

const SearchBar = () => {
  return (
    <div className="mx-auto flex items-center w-2/3">
      <form className="flex flex-row bg-gray-100 border-2 border-gray-400 shadow-md w-full rounded-lg h-10 px-3">
        <input
          className="text-black text-lg font-bold border-none w-full bg-gray-100 outline-none"
          type="text"
          placeholder="buscar..."
        />
        <button className="cursor-pointer">
          <FaSearch />
        </button>
      </form>
    </div>
  );
};

export default SearchBar;
