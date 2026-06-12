import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-gray-900 text-white px-8 py-4 flex gap-8">
      <Link to="/">
        Dashboard
      </Link>

      <Link to="/reviews">
        Reviews
      </Link>

      <Link to="/analytics">
        Analytics
      </Link>
    </nav>
  );
}

export default Navbar;