import { GiShoppingCart } from "react-icons/gi";

const ShoppingCartLogo = () => {
  return (
    <div className="flex items-center">
      <button className="relative">
        <GiShoppingCart size={28} />
        <span className="absolute top-[-30%] right-[-30%] bg-[#A788FF] text-white rounded-full text-xs aspect-square w-4 h-auto flex items-center justify-center">
          2
        </span>
      </button>
    </div>
  );
};

export default ShoppingCartLogo;
