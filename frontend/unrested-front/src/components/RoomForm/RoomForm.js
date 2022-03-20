import React,  { useEffect, useState }  from 'react';
import PropTypes from 'prop-types';
import './RoomForm.scss';
import M from 'materialize-css';
import axios from 'axios';
import { useNavigate } from "react-router-dom";

const timeFormatter = (hour, minutes) => {
   return `${hour}:${minutes}`;
}
//2022-03-19 19:56:21
const dateTimeParser = (dateTime) => {
   const [date, timeUgly] = dateTime.split();
   const [hour, minute, second] = time.split(":");
   const time = timeFormatter(hour, minute);
   return {date, time};
}

const toApiTimeParser = (date, time) => {
  // console.log("datePicker: ");
   const year = date.getYear();
   const month = date.getMonth();


}

const RoomForm = () => {

  const navigate = useNavigate();

  useEffect(() => {

    var elems = document.querySelectorAll('.datepicker');
    var timePick1 = document.getElementById('timepicker1');
    var timePick2 = document.getElementById('timepicker2');
    M.Datepicker.init(elems, {
      defaultDate: new Date(),
      container: "body",
      onSelect: function(date) {
         toApiTimeParser(date);
        setMyDate(date);
      },
      autoClose: true
    });

    M.Timepicker.init(timePick1, {
      defaultDate: new Date(),
      container: "body",
      twelveHour: false,
      onSelect: function(hour, minute) {
         console.log(hour, minute);
        setTimeStart(timeFormatter(hour, minute));
      },
      autoClose: true
    });

    M.Timepicker.init(timePick2, {
      defaultDate: new Date(),
      container: "body",
      twelveHour: false,
      onSelect: function(hour, minute) {
         console.log(hour, minute)
        setTimeEnd(timeFormatter(hour, minute));
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
  const [timeStart, setTimeStart] = useState('start');
  const [timeEnd, setTimeEnd] = useState('end');

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
          id="timepicker1"
          className="timepicker"
          name="time-start"
          value={timeStart}
          onChange={()=>{}}
        />
        <i className="material-icons icon">remove</i>
      <input
        type="text"
        id="timepicker2"
        className="timepicker"
        name="time-end"
        value={timeEnd}
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
