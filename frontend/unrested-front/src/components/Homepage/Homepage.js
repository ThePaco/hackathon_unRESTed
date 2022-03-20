import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './Homepage.scss';
import axios from 'axios';
import { useNavigate } from "react-router-dom";

import image1 from "./connect4 -1.png";
import image2 from "./connect4 -2.png";
import image3 from "./connect4 -3.png";

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
         <div className="buildingContainer">
            <img src={image1} alt="building roof" onClick={floorList}></img>
            {floors.map((floor)  => {
               return (
                  <img src={image2} alt="building roof" class="connet4" className="connet4" onClick={() => {navigate(`floor/${floor.id}`)}} ></img>
               )
            })}
            <img src={image3} alt="building roof"></img>
         </div>
      </div>
   )};

Homepage.propTypes = {};

Homepage.defaultProps = {};

export default Homepage;
