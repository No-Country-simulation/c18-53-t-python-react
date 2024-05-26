import { useSelector, useDispatch } from "react-redux";
import Hero from "../components/Hero";
import Features from "../components/Features";
import Favorites from "../components/Favorites";
import Brands from "../components/Brands";

const Home = () => {
  const user = useSelector((state) => state.user)
  console.log(user)
  // const dispatch = useDispatch();
  return (
    <div>
      <Hero />
      <Features />
      <Favorites />
      <Brands />

      {/* <h1>Desde home</h1> */}
      {/* <div> */}
      {/*   <span> */}
      {/*     Current User: */}
      {/*   </span> */}
      {/*   <p>{user.name}</p> */}
      {/*   <p>{user.email}</p> */}
      {/*   <span>isLogged: {user.loggedIn ? 'true' : 'false'}</span> */}
      {/* </div> */}
    </div>
  );
};

export default Home;
