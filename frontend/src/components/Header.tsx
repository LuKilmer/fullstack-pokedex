import * as React from "react";
import { Link } from "react-router-dom";

class Header extends React.Component {
    render() {
      return (
        <nav>
            <ul>
            <li>
              <Link to={`/`}>home</Link>
            </li>
            <li>
              <Link to={`wiki`}>wiki</Link>
            </li>
            <li>
              <Link to={`pokedex`}>pokedex</Link>
            </li>
          </ul>
        </nav>

      );
    }
}

export default Header;