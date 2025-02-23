import React, { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState(""); // user input
  const [output, setOutput] = useState("output message"); // encoded message
  const [metric, setMetric] = useState(0.5); // metric message
  const [keyData, setKeyData] = useState(null); // key data message
  const [showOutput, setShowOutput] = useState(false); // show output message

  const sendMessage = async () => {
    if (!message.trim()) return;
  
    try {
      const response = await fetch("http://localhost:5000/api/encode", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: message }), // Send user input as JSON
      });
  
      const data = await response.json();
      console.log("Response from backend:", data);
  
      // Set output, metric, and key data from the backend response
      setOutput(data.encoded || "No response"); 
      setMetric(data.metric || 0); 
      setKeyData(data.key || null);
      setShowOutput(true);
  
    } catch (error) {
      console.error("Error sending message:", error);
      setOutput("Error connecting to backend");
      setShowOutput(true);
    }
  
    setMessage(""); // Clear the input field
  };
  

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      sendMessage();
    }
  };

  const downloadKey = () => {
    if (!keyData) return;

    const blob = new Blob([JSON.stringify(keyData, null, 2)], { type: "application/json" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "key.json";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="container">
      {/* Left Panel */}
      <div className="left-panel">
        <div className="title-container">
        <img src="/logo.png" alt="Logo" className="w-40 h-auto mb-4" />
          <h2 className="subtitle">Where natural language processing (NLP) meets cryptography.</h2>
          <p>Cipher AI converts encoded messages into seemingly-normal natural language text. <br></br>
          We NEVER share your message data with AI platform companies like OpenAI.</p>
        </div>
       </div>

      <div className="vertical-bar"></div>
      
      {/* Right Panel */}
      <div className="right-panel">
        <div className="input-container">
          <h2 className="input-title">Enter your message below:</h2>
          <input
            type="text"
            placeholder="Enter input message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyDown} 
            className="input-box"
          />
          {/* Output Box - Only Show if Input is Entered */}
          {showOutput && <div className="output-box">{output}</div>}

          {/* Progress Bar - Only Show if Input is Entered */}
          {showOutput && (
            <div className="progress-bar-container">
              <div className="progress-bar">
                <div className="progress-fill" style={{ width: `${metric * 100}%` }}></div>
              </div>
              <p className="metric-value">{metric.toFixed(2)}</p>
              <p className="cipher-eff-label">Naturalness Index</p>
            </div>
          )}

          {/* Download Button - Only Show if Input is Entered */}
          {showOutput && (
            <button className="download-btn" onClick={downloadKey} disabled={!keyData}>
              Download key as JSON -- keep this secure!
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
