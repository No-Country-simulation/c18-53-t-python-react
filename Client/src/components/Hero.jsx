import { useEffect, useRef } from 'react';
import heroImgOne from '../assets/heroOne.webp'
import heroImgTwo from '../assets/heroTwo.webp'
import heroImgThree from '../assets/heroThree.webp'
import heroImgFour from '../assets/heroFour.webp'
import '@splidejs/splide/dist/css/splide.min.css';
import Splide from '@splidejs/splide';

const Hero = () => {
  const splideRef = useRef(null)
  useEffect(() => {
    if (splideRef.current) {
      let splite = new Splide('.splide', {
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
    <div ref={splideRef} className="relative w-full flex flex-col">
      <div className="splide">
        <div className="splide__track">
          <ul className="splide__list">
            <li className="splide__slide">
              <div className='image-wrapper'>
                <img src={heroImgOne} alt="" loading="lazy" />
              </div>
            </li>
            <li className="splide__slide">
              <div className='image-wrapper'>
                <img src={heroImgTwo} alt="" loading="lazy" />
              </div>
            </li>
            <li className="splide__slide">
              <div className='image-wrapper'>
                <img src={heroImgThree} alt="" loading="lazy" />
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
