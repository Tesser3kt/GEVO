import React, { useEffect } from 'react';
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { GoogleOAuthProvider } from '@react-oauth/google';

import './index.css';

import Index from "./pages/Index";
import Login from "./pages/Login";
import Error from "./pages/Error";
import Dashboard from "./pages/Dashboard";
import EditThesis from "./pages/EditThesis";
import NotFound from "./pages/NotFound";


export default function App() {
  useEffect(() => {
    document.title = "RP GEVO";
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<Index />} />
        <Route path="/login" element={<Login />} />
        <Route path="/error" element={<Error />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/edit/*" element={<EditThesis />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter >
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <GoogleOAuthProvider clientId="236865910793-d0gr4u2sinbaqk5emcem912av6kq8m0d.apps.googleusercontent.com">
      <App />
  </GoogleOAuthProvider>
);