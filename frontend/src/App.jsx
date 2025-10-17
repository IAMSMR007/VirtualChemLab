import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import AuthPage from './Features/Auth/AuthPage';
import HeroPage from './Features/Hero/HeroPage';
import LabPage from './Features/LabInterface/LabInterfacePage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HeroPage />} />
        <Route path="/auth" element={<AuthPage />} />
        <Route path="/lab" element={<LabPage />} />
      </Routes>
    </Router>
  );
}

export default App;
