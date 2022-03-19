import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './Homepage.scss';

const Homepage = () => {
   const [floors, setFloors] = useState([1, 2, 3, 4]);
   const floorList = floors.map((i) => {
      return (
         <button key={i} className="button-slanted button-default waves-light btn">Slanted Button with super long text</button>
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
