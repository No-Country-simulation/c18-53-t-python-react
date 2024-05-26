import Carousel from "./Carousel"

const Favorites = () => {
  return (
    <div className="w-full max-w-[1440px] mx-auto px-[3%] pb-14">
      <header className="py-14">
        <span className="uppercase">Encuentra tus favoritos</span>
        <h2 className="text-[2.5rem]">Las Mejores Opciones Para Tí</h2>
      </header>
      <Carousel />
    </div>
  )
}

export default Favorites
