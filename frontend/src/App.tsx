import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, Link } from 'react-router-dom';

import Dashboard from './pages/Dashboard';
import Assets from './pages/Assets';
import Users from './pages/Users';
import Transactions from './pages/Transactions';

const App = () => {
  return (
    <Router>
      {/* Simple NavBar */}
      <nav className="bg-gray-800 text-white p-4 flex space-x-4">
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/assets">Assets</Link>
        <Link to="/users">Users</Link>
        <Link to="/transactions">Transactions</Link>
      </nav>

      <div className="p-4">
        <Routes>
          <Route path="/" element={<Navigate to="/dashboard" />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/assets" element={<Assets />} />
          <Route path="/users" element={<Users />} />
          <Route path="/transactions" element={<Transactions />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
