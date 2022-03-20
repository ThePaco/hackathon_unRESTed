import React from 'react';
import PropTypes from 'prop-types';
import './Login.scss';
import { useFormik } from 'formik';
import axios from 'axios';
import { useNavigate } from "react-router-dom";

const Login = (props) => {
   const navigate = useNavigate();
  const formik = useFormik({
    initialValues: {
      email: '',
      password: ''
    },
    onSubmit: values => {
     props.setIsAuthenticated(true);
     navigate('../');
    },
    validate: (values) => {
      const errors = {};
      if (!values.email) {
        errors.email = 'Required';
      } else if (
        !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)
      ) {
        errors.email = 'Invalid email address';
      }
      return errors;
    }
  });

  return (
  <div className="Login card">
    <p className="login-title">Login</p>
    <form onSubmit={formik.handleSubmit}>
      <div className="col input">
        <div className="input-field">
          <input
            id="email"
            name="email"
            type="email"
            required
            onChange={formik.handleChange}
            value={formik.values.email}
          />
          <label htmlFor="email">Email</label>
        </div>
      </div>
      <div className="col input">
        <div className="input-field col s12">
          <input
            id="password"
            name="password"
            type="password"
            required
            onChange={formik.handleChange}
            value={formik.values.password}
          />
          <label htmlFor="password">Password</label>
        </div>
      </div>
      <button
        type="submit"
        className="waves-effect waves-light btn"
      >
        Log in
      </button>
    </form>
  </div>
)};

Login.propTypes = {};

Login.defaultProps = {};

export default Login;
