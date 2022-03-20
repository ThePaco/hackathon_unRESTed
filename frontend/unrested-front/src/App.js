import './App.scss';
import Homepage from './components/Homepage/Homepage';
import RoomForm from './components/RoomForm/RoomForm';
import Logo from './components/Logo/Logo';
import LogoLarge from './components/LogoLarge/LogoLarge';
import Login from './components/Login/Login'

import { useNavigate } from "react-router-dom";

import {
   BrowserRouter as Router,
   Route,
   Link,
   Routes,
   Navigate
} from "react-router-dom";
import Floor from './components/Floor/Floor';
import { useState } from 'react';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
   return (
      <div className='App'>
          <Router>
            <Logo />
            <div className='wrapper'>
              <Routes>
                <Route path='/' element={isAuthenticated ? <Homepage /> : <Navigate to="/login" />} />
              </Routes>
              <Routes>
                <Route path='/floor/:id' element={<Floor sceneId='22e32ff5-ba13-48ff-8eeb-2c82341ac23d'/>} />
              </Routes>
              <Routes>
                <Route path='/login' element={<Login setIsAuthenticated={setIsAuthenticated}/>} />
              </Routes>
              <Routes>
                <Route path='/logo' element={<LogoLarge/>} />
              </Routes>
              <Routes>
                <Route
                  path='/room-form'
                  element={
                    <RoomForm />
                  }
                />
              </Routes>
            </div>
          </Router>

      </div>

   );
}

export default App;
