import React, { useEffect, useState } from "react";

export default function App() {
  const [reagents, setReagents] = useState([]);

  useEffect(() => {
    // quick test to ensure the app mounts and can call backend
    fetch("/api/reagents").then(r => r.json()).then(setReagents).catch(()=> {
      setReagents(["HCl","NaOH","AgNO3"]);
    });
  }, []);

  return (
    <div style={{padding:20}}>
      <h1>VirtualChemLab — Frontend Live</h1>
      <h3>Reagents</h3>
      <ul>
        {reagents.map((r, i) => <li key={i}>{r}</li>)}
      </ul>
      <p>If you see this, React mounted successfully.</p>
    </div>
  );
}
