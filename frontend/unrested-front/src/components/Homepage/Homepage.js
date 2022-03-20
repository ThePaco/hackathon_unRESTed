import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './Homepage.scss';
import axios from 'axios';
import { useNavigate } from "react-router-dom";

const Homepage = () => {
  const navigate = useNavigate();
   useEffect(() => {
     axios.get('http://localhost:4000/floor').then((val) => setFloors(val.data));
   }, [])
   const [floors, setFloors] = useState([1, 2, 3, 4]);
   const floorList = floors.map((floor) => {
      return (
         <button
          key={floor.floorNumber}
          className="button-slanted button-default waves-light btn"
          onClick={() => {navigate(`floor/${floor.id}`)}}
          >
            {floor.floorNumber}
          </button>
      )
   })
   return (
      <div className="Homepage">
         <div className="buildingContainer ">
            {floorList}
         </div>
      </div>
   )};

Homepage.propTypes = {};

Homepage.defaultProps = {};

export default Homepage;
