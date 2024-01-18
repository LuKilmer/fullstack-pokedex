import * as React from "react";
import { Link } from "react-router-dom";

class Home extends React.Component {
    render() {
    console.log("home")
      return (
          <div>
            <h1>Home</h1>
            <p>


              <Link to={"pokedex-regional"}>Pokedex regional</Link>
            </p>
          </div>
      )


    }
}

export default Home;