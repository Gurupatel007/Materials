import logo from './logo.svg';
import logo1 from './guni.png';
import './App.css';

function App() {
  return (
    <div classname="App">
      <header>
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <img src={logo1} alt="logo" width='100px' style={{align:'center'}}/>
      </header>
      <form>
        <label for="fname">First name:</label><br/>
        <input type="text" id="fname" name="fname"/><br/>
        <label for="lname">Last name:</label><br/>
        <input type="text" id="lname" name="lname"/><br/><br/>
        <input type="submit" value="Submit"/>
      </form>
      <h1>Guru</h1>
    </div>
    
  );
}

export default App;
