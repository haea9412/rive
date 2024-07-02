import { BrowserRouter } from "react-router-dom";

import Header from "./app/Header";
import AuthProvider from "./context/AuthProvider"
import HttpHeadersProvider from "./context/HttpHeadersProvider"
import Nav from "./app/Nav"
import Body from "./app/Body"
import Footer from "./app/Footer"

import "../css/style.css"

const Main =()=>{
return (
  <div className="main-background">
    <BrowserRouter>
      <Header />
      <AuthProvider>
        <HttpHeadersProvider>
          <Nav />
          <Body />
        </HttpHeadersProvider>
      </AuthProvider>
      <Footer />
    </BrowserRouter>
  </div>
  );
}

export default Main;
