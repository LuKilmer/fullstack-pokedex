import { Link } from "react-router-dom";
import PokeList from "../components/PokeList";
import { useParams } from "react-router-dom";

function Pokedex(){
    
    const { id } = useParams();
    
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
    
            {id !== undefined ? (
                <PokeList id={id} />
            ) : (

                 <ul>
                    <li><Link to={"/pokedex/0"}>Gold Silver and Crystal</Link></li>
                    <li><Link to={"/pokedex/1"}>Red Blue and Yellow</Link></li>
                    <li><Link to={"/pokedex/2"}>FireRed and LeafGreen</Link></li>
                    <li><Link to={"/pokedex/3"}>Ruby Sapphire and Emerald</Link></li>
                    <li><Link to={"/pokedex/4"}>Platinum</Link></li>
                    <li><Link to={"/pokedex/5"}>HeartGold and SoulSilver</Link></li>
                    <li><Link to={"/pokedex/6"}>Black and White</Link></li>
                    <li><Link to={"/pokedex/7"}>Black and White 2</Link></li>
                </ul>
            )}
        </div>
    )
    
}

export default Pokedex;