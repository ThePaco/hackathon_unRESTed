import React from 'react';
import PropTypes from 'prop-types';
import image from "./iconCircle.png";
import './Logo.scss';
import { useNavigate } from 'react-router';
import { Link } from 'react-router-dom';

const Logo = () => {
  return (
  <Link className="Logo" to='../'>
    <img src={image} alt="logo"/>
    <p className="title">  unRESTed </p>
  </Link>
)};

Logo.propTypes = {};

Logo.defaultProps = {};

export default Logo;
