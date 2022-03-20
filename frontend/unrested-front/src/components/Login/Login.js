import React from 'react';
import PropTypes from 'prop-types';
import './Login.scss';
import { useFormik } from 'formik';

const Login = () => {
  const formik = useFormik({
    initialValues: {
      email: '',
      password: ''
    },
    onSubmit: values => {
      alert(JSON.stringify(values, null, 2));
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
