// import React from 'react';
import Footer from './components/footer';
import Header from './components/header';
// import MiddleView from './components/middle';
// import Home from './screens/home';
import MobileView from './screens/mobile-view'
// import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
function App() {
  return (
      <div className="App">
          <Header/>
          {/* <MiddleView/> */}
          <main>
            <MobileView/>
            {/* <Routes> */}
              {/* <Route path="/" element={<Home/>} /> */}
            {/* </Routes> */}
          </main> 
          <Footer/>
      </div>
  );
}

export default App;
