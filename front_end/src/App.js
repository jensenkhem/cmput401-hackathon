import logo from './logo.svg';
import './App.css';
import ulogo from './ua_logo_green_rgb.png';
import plogo from './profile_logo.png';
import clogo from './car_logo.png';
import d_karma from './driver_karma.jpg'
import r_rating from './rider_rating.png'
import o_ride from './offer_ride.png'
import s_ride from './scheduled_ride.png'
import h_logo from './history_logo.png'




function App() {

  return (
    <div className="App">
      <header className="App-header">

        <h2>
          <img style={{width: '15%' ,float:'left'}} src = {ulogo} alt="logo"/>
          Ride pooling to campus
        </h2>

        
      
      </header>
      <div className='container'>

        <header className='App-profile'>
          <h2>
            
            <img style={{width: '20%' }} src = {plogo} alt="profile picture"/>
            Profile
          </h2>
        </header>

        <header className='App-profile'>
          <h2>
            
            <img style={{width: '20%' }} src = {clogo} alt="profile picture"/>
            Find Ride
          </h2>
        </header>

        <header className='App-profile'>
          <h2>
            
            <img style={{width: '20%' }} src = {o_ride} alt="profile picture"/>
            Offer Ride
          </h2>
        </header>

        <header className='App-profile'>
          <h2>
            
            <img style={{width: '20%' }} src = {d_karma} alt="driver karma"/>
            Driver karma
          </h2>
        </header>

        <header className='App-profile'>
          <h2>
            
            <img style={{width: '10%' }} src = {r_rating} alt="rider rating"/>
            Rider rating
          </h2>
        </header>

        <header className='App-profile'>
          <h2>
            
            <img style={{width: '10%' }} src = {s_ride} alt="Scheduled ride"/>
            Scheduled rides
          </h2>
        </header>

        <header className='App-profile'>
          <h2>
            
            <img style={{width: '10%' }} src = {h_logo} alt="Ride history"/>
            Ride history
          </h2>
        </header>

      </div>
      
    </div>

    
  );
}

export default App;
