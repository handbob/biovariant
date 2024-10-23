import React from 'react';
import { Outlet } from 'react-router-dom';

import './App.css';

function App() {
  return (
    <div id="app">
      <h1>Allele Frequency Viewer</h1>
      <Outlet />
    </div>
  );
}

export default App;
