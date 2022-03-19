import './App.scss';
import Homepage from './components/Homepage/Homepage';
import RoomForm from './components/RoomForm/RoomForm';

import {
   BrowserRouter as Router,
   Route,
   Link,
   Routes,
   Navigate
} from "react-router-dom";
import Floor from './components/Floor/Floor';

function App() {
   return (
      <div className='App'>
         <Router>

            <Routes>
               <Route path='/' element={true ? <Homepage /> : <Navigate to="/login" />} />
            </Routes>
            <Routes>
               <Route path='/floor' element={<Floor sceneId='22e32ff5-ba13-48ff-8eeb-2c82341ac23d'/>} />
            </Routes>
            <Routes>
               <Route path='/room-form' element={<RoomForm />} />
            </Routes>
         </Router>
      </div>

   );
}

export default App;
