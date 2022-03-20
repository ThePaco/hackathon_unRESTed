import React,  { useEffect, useState }  from 'react';
import PropTypes from 'prop-types';
import './RoomForm.scss';
import M from 'materialize-css';
import axios from 'axios';
import { useNavigate } from "react-router-dom";

const timeFormatter = (date, hour, minutes) => {
   return new Date(date.getYear(), date.getMonth(), date.getDate(), hour, minutes, 0)
}
//2022-03-19 19:56:21
const dateTimeParser = (dateTime) => {
  console.log(dateTime);
   const [date, timeUgly] = dateTime.split('');
   const [hour, minute, second] = timeUgly.split(":");
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

    axios.get('http://localhost:4000/reservation').then( (val) => setReservations(val.data))

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
        setTimeStart(timeFormatter(myDate ,hour, minute));
      },
      autoClose: true
    });

    M.Timepicker.init(timePick2, {
      defaultDate: new Date(),
      container: "body",
      twelveHour: false,
      onSelect: function(hour, minute) {
        setTimeEnd(timeFormatter(myDate ,hour, minute));

        console.log(timeEnd, timeStart)
        console.log(new Date(timeEnd)-new Date(timeStart))
        if((timeEnd-timeStart) > 8640000) {
          console.log((timeEnd-timeStart) > 8640000)
          setErrorTime('Yikes')
        }
      },
      autoClose: true
    });

    axios.get('http://localhost:4000/reservation').then((res) => console.log(res))

  }, [])

  const [myDate, setMyDate] = useState(new Date().toLocaleDateString());
  const [timeStart, setTimeStart] = useState('start');
  const [timeEnd, setTimeEnd] = useState('end');
  const [reservations, setReservations] = useState([]);
  const [errorTime, setErrorTime] = useState();

  const submitReservation = () => {
    axios.post(`http://localhost:4000/reservation/${"d4aabcba-9b87-4721-af9a-3d53dad13bc3"}`, {
      roomId: "d4aabcba-9b87-4721-af9a-3d53dad13bc3",
      reservationStart: timeStart,
      reservationEnd: timeEnd,
    })
  }
  function handleChange(event) {
    console.log(event)
      setMyDate(event.target.value);
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

      {reservations.filter((res)=> {
        const resDate = new Date(res.reservationStart);
        const newDate = new Date(myDate);
        return (resDate.toLocaleDateString()) === newDate.toLocaleDateString()
      }).map((reservation)=>{
        const resStart = new Date(reservation.reservationStart)
        const resEnd = new Date(reservation.reservationEnd)
        return (
          <div className="card reservation">
            <div className="car">{reservation.owner}</div>
            {resStart.toTimeString().split(' ')[0]} - {resEnd.toTimeString().split(' ')[0]}
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
      {errorTime}
      <div>

      </div>
    </div>
      <br/>
      <br />
      <button className="waves-effect waves-light btn" onClick={submitReservation}>
        Submit
      </button>

      </div>

  );
}


export default RoomForm;
