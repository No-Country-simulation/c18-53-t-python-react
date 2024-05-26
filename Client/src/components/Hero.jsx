import { useEffect, useRef } from 'react';
import heroImgOne from '../assets/heroOne.webp'
import heroImgTwo from '../assets/heroTwo.webp'
import heroImgThree from '../assets/heroThree.webp'
import heroImgFour from '../assets/heroFour.webp'
import Splide from '@splidejs/splide';

const Hero = () => {
  const splideRef = useRef(null)
  useEffect(() => {
    if (splideRef.current) {
      let splite = new Splide(splideRef.current, {
        type: 'loop',
        autoplay: true,
        pagination: false,
        interval: 5000,
        speed: 1000,
        perMove: 1,
        perPage: 1,
        pauseOnHover: false
      })
      let bar = splite.root.querySelector('.my-slider-progress')
      splite.on('mounted move', function() {
        let end = splite.Components.Controller.getEnd() + 0;
        let rate = Math.min(((splite.index + 0) / end), 1);
        bar.style.width = String(100 * rate) + "%";
      })
      splite.mount()
    }
  }, [])

  return (
    <div className="relative w-full flex flex-col">
      <div className='text-white z-10 absolute top-[50%] left-0 bottom-0 right-0 w-full h-fit px-[3%] max-w-[1440px] mx-auto translate-y-[-50%] flex flex-col gap-4'>
        <h1 className='text-[5rem] max-w-[800px] leading-[1.2] '>The Future for Furniture Retailers</h1>
        <p className='text-[18px] max-w-[800px] mb-4'>Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.</p>
        <div className='flex gap-8'>
          <button className='text-[18px] w-fit bg-[#434375] rounded-full py-2 px-6'>Ver todos los catalogos</button>
          <button className='text-[18px] w-fit '><span className='border-b-[1px] border-b-white border-solid py-1'>Ver productos</span> </button>
        </div>
      </div>

      <div id='splide1' ref={splideRef} className="splide">
        <div className="splide__track">
          <ul className="splide__list">
            <li className="splide__slide">
              <div className='image-wrapper'>
                <img src={heroImgThree} alt="" loading="lazy" />
              </div>
            </li>
            <li className="splide__slide">
              <div className='image-wrapper'>
                <img src={heroImgTwo} alt="" loading="lazy" />
              </div>
            </li>
            <li className="splide__slide">
              <div className='image-wrapper'>
                <img src={heroImgOne} alt="" loading="lazy" />
              </div>
            </li>
            <li className="splide__slide">
              <div className='image-wrapper'>
                <img src={heroImgFour} alt="" loading="lazy" />
              </div>
            </li>
          </ul>
        </div>

        <div className="absolute bottom-0 left-0 my-slider-progress">
          <div className="my-slider-progress-bar"></div>
        </div>
      </div>


    </div>
  )
}

export default Hero 
