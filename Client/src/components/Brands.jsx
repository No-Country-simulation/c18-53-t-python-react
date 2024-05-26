import img from '../assets/brands.jpeg'
const Brands = () => {
  return (
    <div className="w-full max-w-[1440px] mx-auto px-[3%]">
      <header className="py-14 pb-8 flex flex-col items-center justify-center">
        {/* <span className="uppercase">Encuentra tus favoritos</span> */}
        <h2 className="text-[1.2rem]">MARCAS CON LAS QUE TRABAJAMOS</h2>
      </header>
      <div className="brand-gallery">
        <div className='brand-wrapper'>
          <img src={img} />
        </div>
        <div className='brand-wrapper'>
          <img src={img} />
        </div><div className='brand-wrapper'>
          <img src={img} />
        </div><div className='brand-wrapper'>
          <img src={img} />
        </div><div className='brand-wrapper'>
          <img src={img} />
        </div><div className='brand-wrapper'>
          <img src={img} />
        </div>
        <div className='brand-wrapper'>
          <img src={img} />
        </div><div className='brand-wrapper'>
          <img src={img} />
        </div>
      </div>
    </div>
  )
}

export default Brands
