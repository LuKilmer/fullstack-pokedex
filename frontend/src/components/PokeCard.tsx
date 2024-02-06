import Poke_Basic from "../model/Pokemon";
import './PokeCard.css'

interface IProductProps {
    props: Poke_Basic;
   
}

export const PokeCard= ({props}:IProductProps) => {
    
    console.log(props.nome);
    return (
    <li className="card-pokemon">
        
        <img src={props.img} alt={props.nome}></img>
        <h4 className="card-name">{props.nome}</h4>
        <p>#{
            props.id < 100 ? props.id < 10? "00"+props.id: "0"+props.id : props.id
        }
        
        
        </p>
        {
            props.tipo.length > 1 ? 
            <div className="card-type-session">
                <a href="">{props.tipo[0]}</a>
                <a href="">{props.tipo[1]}</a>
            </div>

            : 
            <div className="card-type-session">
                <a href="">{props.tipo[0]}</a>
            </div>
        }

    </li>
    );
    
  }
