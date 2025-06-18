import React, { useState } from "react";

function PortfolioGenerator() {
  const [riskLevel, setRiskLevel] = useState("Moderate");
  const [amount, setAmount] = useState(10000);

  const handleSubmit = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          risk_level: riskLevel,
          amount: amount,
          // Remove thematic_investing field from the request body
        }),
      });
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error("Error generating portfolio:", error);
    }
  };

  return (
    <div>
      <h1>Portfolio Generator</h1>
      <label>
        Select Risk Level:
        <select value={riskLevel} onChange={(e) => setRiskLevel(e.target.value)}>
          <option value="Conservative">Conservative</option>
          <option value="Moderately Conservative">Moderately Conservative</option>
          <option value="Moderate">Moderate</option>
          <option value="Moderately Aggressive">Moderately Aggressive</option>
          <option value="Aggressive">Aggressive</option>
        </select>
      </label>
      <br />
      <label>
        Investment Amount ($):
        <input
          type="number"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
      </label>
      <br />
      {/* Remove or comment out the thematic investing dropdown */}
      {/* <label>
        Select Thematic Investing Theme (Optional):
        <select>
          <option value="No Theme">No Theme</option>
          <option value="Green Energy">Green Energy</option>
          <option value="Technology">Technology</option>
        </select>
      </label> */}
      <br />
      <button onClick={handleSubmit}>Generate Portfolio</button>
    </div>
  );
}

export default PortfolioGenerator;