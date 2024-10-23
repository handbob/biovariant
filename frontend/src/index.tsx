import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/index.css';
import axios from 'axios';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { VariantList } from './components/VariantList';
import { VariantDetails } from './components/VariantDetail';

axios.defaults.baseURL = 'http://localhost:5001';

const routes = [
  { path: '/', element: <VariantList /> },
  { path: '/variant/:position', element: <VariantDetails /> },
];

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <Router>
      <Routes>
        {routes.map((route, index) => (
          <Route
            key={index}
            path={route.path}
            element={route.element}
          />
        ))}
      </Routes>
    </Router>
  </React.StrictMode>
);
