import Splide from '@splidejs/splide';
import { useEffect, useRef } from 'react';
import Card from './Card';

const Carousel = () => {
  const carouselRef = useRef(null)
  useEffect(() => {
    if (carouselRef.current) {
      let splide = new Splide(carouselRef.current, {
        type: 'loop',
        perPage: 3,
        perMove: 1,
        gap: '1.5rem',
        pagination: false
      })
      splide.mount()
    }
  }, [])
  return (
    <div id='splide2' ref={carouselRef} className="splide">
      <div className="splide__track">
        <ul className="splide__list">
          <li className="splide__slide"><Card /></li>
          <li className="splide__slide"><Card /></li>
          <li className="splide__slide"><Card /></li>
          <li className="splide__slide"><Card /></li>
          <li className="splide__slide"><Card /></li>
          <li className="splide__slide"><Card /></li>
        </ul>
      </div>
    </div>
  )
}

export default Carousel
