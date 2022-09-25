// import React from 'react';
import Footer from './components/footer';
import Header from './components/header';
import Home from './screens/home';
import MobileView from './screens/mobile-view'
import {  Route, Routes } from "react-router-dom";
import MobilePhones from './screens/mobile';
function App() {
  return (
      <div className="App">
          <Header/>
          <main>
            <Routes>
              <Route path="/" element={<Home/>} />
              <Route path="/mobile/" element={<MobilePhones/>} />
              <Route path="/mobile/:slug" element={<MobileView/>} />
            </Routes>
          </main> 
          <Footer/>
      </div>
  );
}

export default App;
