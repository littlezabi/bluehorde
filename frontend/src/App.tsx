import Footer from './components/footer';
import Header from './components/header';
import Home from './screens/home';
import MobileView from './screens/mobile-view'
import {  Route, Routes } from "react-router-dom";
import Products from './screens/products';
function App() {
  return (
      <div className="App">
          <Header/>
          <main>
            <Routes>
              <Route path="/" element={<Home/>} />
              <Route path="/categories/" element={<Products/>} />
              <Route path="/category/:slug" element={<Products/>} />
              <Route path="/mobile/:slug" element={<MobileView/>} />
            </Routes>
          </main> 
          <Footer/>
      </div>
  );
}

export default App;
