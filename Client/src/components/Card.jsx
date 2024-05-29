import img from '../assets/card-product.jpeg'

const Card = ({ type = 'main' }) => {
  return (
    <div className='relative cursor-pointer'>
      {
        type == 'main' ?
          <span className='absolute top-4 left-4 px-2 bg-[#434375] rounded-full text-white font-light text-[14px]'>Favorite</span>
          :
          null
      }
      <div className='aspect-square flex items-center justify-center rounded-[4px] overflow-hidden bg-red-500'>
        <img src={img} className='flex w-full bg-blue-500' />
      </div>
      {
        type == 'main' ?
          <div className='absolute bottom-0 left-0 right-0 top-0 p-4 flex gap-4 justify-between items-end linear-gradient text-white'>
            <h4 className='font-normal text-[1.5rem]'>Product 1</h4>
            <p className='hidden'>Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.</p>
            <span className='text-[1.5rem]'>$33.34</span>
          </div>
          :
          <div className='pt-4'>
            <h4 className='font-normal text-[1.5rem]'>Product 1</h4>
            <p className='mb-2'>Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.</p>
            <span className='text-[1.5rem]'>$33.34</span>
          </div>
      }
    </div >
  )
}

export default Card
