import React from "react";
import Login from "./components/Login";
import FaceLogin from "./components/FaceLogin";

function App() {
  return (
    <div style={{ fontFamily: "Arial, sans-serif", textAlign: "center", padding: "20px" }}>
      <h1 style={{ color: "#e50914" }}>🎬 Welcome to Netflix Clone</h1>

      <div style={{ display: "flex", justifyContent: "center", gap: "50px", marginTop: "40px" }}>
        <div style={{ border: "1px solid #ccc", borderRadius: "12px", padding: "20px", width: "300px" }}>
          <h2>🔐 Manual Login</h2>
          <Login />
        </div>

        <div style={{ border: "1px solid #ccc", borderRadius: "12px", padding: "20px", width: "300px" }}>
          <h2>📸 Face Login</h2>
          <FaceLogin />
        </div>
      </div>
    </div>
  );
}

export default App;
