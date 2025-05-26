import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, Link } from 'react-router-dom';

import AssetListPage from './pages/AssetList';
import CreateAsset from './pages/CreateAsset';
import Users from './pages/Users';
import Transactions from './pages/Transactions';
import Dashboard from './pages/Dashboard';

const App: React.FC = () => {
  return (
    <Router>
      <nav className="bg-gray-800 text-white p-4 flex space-x-4">
        <Link to="/dashboard" className="hover:underline">Dashboard</Link>
        <Link to="/assets" className="hover:underline">Assets</Link>
        <Link to="/assets/create" className="hover:underline">Create Asset</Link>
        <Link to="/users" className="hover:underline">Users</Link>
        <Link to="/transactions" className="hover:underline">Transactions</Link>
      </nav>

      <div className="p-4">
        <Routes>
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/assets" element={<AssetListPage />} />
          <Route path="/assets/create" element={<CreateAsset />} />
          <Route path="/users" element={<Users />} />
          <Route path="/transactions" element={<Transactions />} />
          {/* Add more routes as needed */}
        </Routes>
      </div>
    </Router>
  );
};

export default App;
