import { GiShoppingCart } from "react-icons/gi";

const ShoppingCartLogo = () => {
  return (
    <div className="w-1/3 flex items-center">
      <button>
        <GiShoppingCart className="h-10 w-10" />
        <span className="absolute bg-red-600 text-white px-2 py-1 rounded-full top-8 left-[1310px] text-xs">
          0
        </span>
      </button>
    </div>
  );
};

export default ShoppingCartLogo;
