import { useEffect, useState } from "react";
import Poke_Basic from "../model/Pokemon";

interface idPokedex{
    id:string
}

function PokeList(props: idPokedex) {
    const [error, setError] = useState<Error | null>(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [items, setItems] = useState<Poke_Basic[]>([]);
   
    useEffect(() => {
    fetch(`http://localhost:5000/pokedex/${props.id}`)
        .then(res => res.json())
        .then(
          (result) => {
            setIsLoaded(true);
            setItems(result);
            console.log(result);
          },
          
          (error) => {
            setIsLoaded(true);
            setError(error);
          }
        )
    },[props.id])
  
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div>
            <ul>
            {items.map(item => (
                <li key={item.nome}>
                <img src={item.img}></img> 
                {item.nome} {item.id}
                {item.tipo.map(tip =>(
                  <p key={tip}>{tip}</p>
                ))}
                </li>
            ))}
            </ul>

        </div>
      );
    }
  }

export default PokeList;