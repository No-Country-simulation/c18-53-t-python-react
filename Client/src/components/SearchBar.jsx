import { CiSearch } from "react-icons/ci";

const SearchBar = ({ fill }) => {
  return (
    <div
      className={`flex justify-between items-center border-[1px] border-gray-400 border-solid rounded-full bg-[#e6e5ff] text-md px-3 py-1 ${fill ? "w-full" : "w-[400px]"}  min-w-[300px]`}
    >
      <input
        className="w-full h-full"
        type="text"
        placeholder="Buscar producto..."
      />
      <button className="">
        <CiSearch size={24} />
      </button>
    </div >
  );
};

export default SearchBar;
