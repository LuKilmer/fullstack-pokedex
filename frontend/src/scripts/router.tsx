import { Navigate, createBrowserRouter } from 'react-router-dom';
import Home from '../pages/Home';
import Wiki from '../pages/Wiki';
import App from '../App';
import ErrorPage from '../pages/ErrorPage';
import Pokedex from '../pages/Pokedex';
import Pokemon from '../pages/Pokemon';


const routerApp = createBrowserRouter([
  {
    path:"/",
    element: <App/>,
    errorElement: <ErrorPage/>,
    children:[
      {
        path:"/",
        element:<Home/>
      },
      {
        path:"wiki",
        element:<Wiki/>
      },
      {
        path:"pokedex",
        element:<Pokedex/>
      },
      {
        path:"/pokemon/:id",
        element:<Pokemon/>
      },
      //para links antigo
      {
        path: "pokedex-regional",
        element:<Navigate to="/pokedex"/>
      }
    ]
  }
])
export default routerApp;