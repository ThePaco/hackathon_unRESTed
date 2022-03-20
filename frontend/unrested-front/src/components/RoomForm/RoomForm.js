import React,  { useEffect, useState }  from 'react';
import PropTypes from 'prop-types';
import './RoomForm.scss';
import M from 'materialize-css';
import axios from 'axios';
import { useNavigate } from "react-router-dom";
// import "materialize-css/dist/css/materialize.min.css";
// import "materialize-css/dist/js/materialize.min.js";

// import { Container, DatePicker } from "react-materialize";

const RoomForm = (props) => {

  const navigate = useNavigate();

  useEffect(() => {

    var elems = document.querySelectorAll('.datepicker');
    var elems2 = document.querySelectorAll('.timepicker');
    M.Datepicker.init(elems, {
      defaultDate: new Date(),
      container: "body",
      onSelect: function(date) {
        setMyDate(date);
      },
      autoClose: true
    });

    M.Timepicker.init(elems2, {
      defaultDate: new Date(),
      container: "body",
      onSelect: function(time) {
        setTimeStart(time);
      },
      autoClose: true
    });

    axios.get('http://localhost:4000/reservation').then((res) => console.log(res))

  }, [])

  const reservationsForDay = [
    {owner:'Tere', start: '12:30', end: '13:30'},
    {owner:'Ana', start: '13:30', end: '14:30'},
    {owner:'Netko', start: '15:30', end: '15:30'},
  ]
  let timeNow = new Date().toLocaleDateString();

  const [myDate, setMyDate] = useState(timeNow);
  const [timeStart, setTimeStart] = useState();

  function handleChange(event) {
    console.log(event)
      setMyDate(event.target.value);
      console.log("Spremljeni datum " + event.target.value);
  }

  return(
      <div className='RoomForm card'>
        <div
        className="right exit"
        onClick={()=>{navigate('../floor/1')}}
        >
          <i className="material-icons right">close</i>
        </div>
        <div className="card-title">
          Reservations
        </div>
        <br />
        <div className="date-wrapper">
          <label className="label" htmlFor="trip-start">Pick Date:</label>
          <input
              className='datepicker daypicker'
              onSelect={handleChange}
              onChange={(ev)=>{setMyDate(ev.target.value)}}
              onClose={(cev)=>{console.log(cev)}}
              type="text"
              name="trip-start"
              value={myDate}
          />
        </div>

      {reservationsForDay.map((reservation)=>{
        return (
          <div className="card reservation">
            <div className="car">{reservation.owner}</div>
            {reservation.start} - {reservation.end}
          </div>
        )
      })}

      <label className="label" htmlFor="time-start">Pick Time:</label>
      <div className="time-wrapper">
        <input
          type="text"
          className="timepicker"
          name="time-start"
          value={timeStart}
          onChange={()=>{}}
        />
        <i className="material-icons icon">remove</i>
      <input
        type="text"
        className="timepicker"
        name="time-start"
        value={timeStart}
        onChange={()=>{}}
      />
    </div>
      <br/>
      <br />
      <button className="waves-effect waves-light btn">
        Submit
      </button>

      </div>

  );
}


export default RoomForm;
