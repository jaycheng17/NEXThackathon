import { Outlet, Link } from "react-router-dom";
import "../css/Layout.css";

const Layout = () => {
  return (
    <>
      <nav>
          <Link to="/">Home</Link>
          <Link to="/about">About</Link>
          <Link to="/services">Login</Link>
          <Link to="/gallery">Gallery</Link>
          <Link to="/contactus">Contact Us</Link>
      </nav>

      <Outlet />
    </>
  )
};

export default Layout;