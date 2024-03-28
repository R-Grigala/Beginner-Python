import { useEffect, useState } from 'react';
import './App.css';
import Deploy from './Component/Deploy/Deploy';
import Heloo from './Component/Deploy/Heloo';

function App() {
  const [state, setState] = useState({})
  
  useEffect(() => {
    fetch("/api").then(response => {
      if(response.status === 200){
        return response.json()
      }
    }).then(data => setState(data))
    .then(error => console.log(error))
  },[])
  return (
    <div className="App">
      <Heloo />
      <Deploy prop={state}/>
    </div>
  );
}

export default App;
