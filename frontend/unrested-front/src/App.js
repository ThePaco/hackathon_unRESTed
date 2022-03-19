import './App.scss';
import Homepage from './components/Homepage/Homepage';

import {
   BrowserRouter as Router,
   Switch,
   Route,
   Link,
   Routes,
   Navigate
} from "react-router-dom";

function App() {
   return (
      <div className='App'>
         <Router>
            <Routes>
               <Route path='/' element={true ? <Homepage /> : <Navigate to="/login" />} />
            </Routes>
         </Router>
      </div>

   );
}

export default App;
