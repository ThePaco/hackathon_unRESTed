import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './Homepage.scss';
import axios from 'axios';

const Homepage = () => {
   useEffect(() => {
     axios.get('http://localhost:4000/floor').then((val) => setFloors(val.data));
   }, [])
   const [floors, setFloors] = useState([1, 2, 3, 4]);
   const floorList = floors.map((floor) => {
      return (
         <button key={floor.id} className="button-slanted button-default waves-light btn">{floor.floorNumber}</button>
      )
   })
   return (
      <div className="Homepage">
         <a className="waves-effect waves-light btn">button</a>
         <h1>Hello</h1>

         <div className="buildingContainer ">
            {floorList}
         </div>
      </div>
   )};

Homepage.propTypes = {};

Homepage.defaultProps = {};

export default Homepage;
