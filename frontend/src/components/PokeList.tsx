import { useEffect, useState } from "react";
import Poke_Basic from "../model/Pokemon";

interface idPokedex{
    id:string
}

function PokeList(props: idPokedex) {
    const [error, setError] = useState<Error | null>(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [items, setItems] = useState<Poke_Basic[]>([]);
    console.log(props.id)
    useEffect(() => {
    fetch(`http://localhost:5000/pokedex/${props.id}`)
        .then(res => res.json())
        .then(
          (result) => {
            setIsLoaded(true);
            setItems(result);
          },
          
          (error) => {
            setIsLoaded(true);
            setError(error);
          }
        )
    }, [])
  
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div>
            <ul>
            {items.map(item => (
                <li key={item.id}>
                <img src={item.img}></img> 
                {item.nome} {item.id}
                </li>
            ))}
            </ul>

        </div>
      );
    }
  }

export default PokeList;