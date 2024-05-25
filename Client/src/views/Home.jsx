import { useSelector, useDispatch } from "react-redux";
import Hero from "../components/Hero";

const Home = () => {
  const user = useSelector((state) => state.user)
  // const dispatch = useDispatch();
  return (
    <div>
      <Hero />
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
