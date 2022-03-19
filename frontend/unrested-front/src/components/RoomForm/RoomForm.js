import React,  { useState }  from 'react';
import PropTypes from 'prop-types';
import './RoomForm.css';
import DatePicker from "react-datepicker";
import M from 'materialize-css';

// import "materialize-css/dist/css/materialize.min.css";
// import "materialize-css/dist/js/materialize.min.js";

// import { Container, DatePicker } from "react-materialize";

const RoomForm = () => { 

   let timeNow = new Date().toLocaleDateString();
   console.log("Trenutni datum: " + timeNow);

   const [myDate, setMyDate] = useState("");
   console.log("myDate: " + myDate);

   function handleChange(event) {
      setMyDate(event.target.value);
      console.log("Spremljeni datum " + event.target.value);
   }

   return(
      <div className='RoomForm'> 
         <input 
            onChange={handleChange}
            type="date" 
            id="myDateID" 
            name="trip-start"
            value={myDate} 
         ></input>
         <button>
        Submit
      </button>
      <table>
         <tr>
            <th>From</th>
            <th>To</th>

         </tr>
         <tr>
            <td>{timeNow}</td>
            <td>{myDate}</td>

         </tr>
      </table>
      {/* <Container>
        <p className="flow-text">Date: {this.state.date}</p>
        <DatePicker
          onChange={({ target: { value: date } }) => {
            this.setState({
              date
            });
          }}
        />
      </Container> */}
      </div>

   );
}
   

export default RoomForm;
