import { useParams } from "react-router-dom";

const Pokemon = () => {
    const { id } = useParams();

    return (
        <div>
            {/* Puedes usar la variable 'id' aquí */}
            <p>ID del Pokémon: {id}</p>
        </div>
    );
};

export default Pokemon;