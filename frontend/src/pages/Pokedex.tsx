import React from "react";
import { Link } from "react-router-dom";

class Pokedex extends React.Component{
    render(){
        return(
            <div>
                <ul>
                    <li><Link to={"/pokemon/1"}>Poke1</Link></li>
                    <li><Link to={"/pokemon/2"}>Poke2</Link></li>
                    <li><Link to={"/pokemon/3"}>Poke3</Link></li>
                    <li><Link to={"/pokemon/4"}>Poke4</Link></li>
                    <li><Link to={"/pokemon/5"}>Poke5</Link></li>
                    <li><Link to={"/poke-nao-existente/"}>Poke6</Link></li>
                </ul>

            </div>
        )
    }
}

export default Pokedex;