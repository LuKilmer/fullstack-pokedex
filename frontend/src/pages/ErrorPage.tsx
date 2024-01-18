import { useNavigate } from "react-router-dom";

const ErrorPage = () =>{
    const navigate = useNavigate();


    const handleErrorMsg = () =>{
        return navigate("/")
    }

    
    return(
        <div>
            <h1>Página não encontrada</h1>
            <button onClick={handleErrorMsg}>Voltar</button>
        </div>
    )
    
}

export default ErrorPage;