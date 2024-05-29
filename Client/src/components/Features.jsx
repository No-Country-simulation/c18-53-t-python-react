import { CiBookmarkCheck } from "react-icons/ci";
import { CiMoneyCheck1 } from "react-icons/ci";
import { PiMapPinLineLight } from "react-icons/pi";
import { PiShootingStarLight } from "react-icons/pi";
import { PiTagLight } from "react-icons/pi";

const Features = () => {

  const features = [
    {
      name: 'Feature One',
      icon: <CiMoneyCheck1 size={30} />,
    },
    {
      name: 'Feature Two',
      icon: <CiBookmarkCheck size={30} />,
    }, {
      name: 'Feature Three',
      icon: <PiMapPinLineLight size={30} />,
    }, {
      name: 'Feature Four',
      icon: <PiShootingStarLight size={30} />,
    }, {
      name: 'Feature Five',
      icon: <PiTagLight size={30} />,
    },
  ]

  return (
    <div className='w-full max-w-[1440px] mx-auto px-[3%]'>
      <ul className='flex flex-wrap justify-between items-center py-8 gap-8 border-b-[1px] border-solid border-gray-400'>
        {
          features.map(({ name, icon }, i) => {
            return (
              <li key={name + i} className='flex items-center justify-center text-[#434375] gap-3'>
                <span>
                  {icon}
                </span>
                <h3 className='text-[16px] uppercase'>
                  {name}
                </h3>
              </li>
            )
          })
        }
      </ul>
    </div>
  )
}

export default Features
