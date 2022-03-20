import React from 'react';
import PropTypes from 'prop-types';
import './LogoLarge.css';
import image from "./iconCircle.png";
import { useNavigate } from 'react-router-dom';

const LogoLarge = () => {
   const navigate = useNavigate();
   return (
  <div className="LogoLarge" onClick={()=> navigate('/login')}>
    <img src={image} alt="logo"/>
  </div>
)};

LogoLarge.propTypes = {};

LogoLarge.defaultProps = {};

export default LogoLarge;
