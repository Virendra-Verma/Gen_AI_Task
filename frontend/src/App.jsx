import { useState } from "react";

export default function App() {
  const [data, setData] = useState("");

  const callAPI = async (url) => {
    const res = await fetch(url);
    const result = await res.json();
    setData(JSON.stringify(result, null, 2));
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: "linear-gradient(135deg, #0f2027, #203a43, #2c5364)",
      padding: "30px",
      fontFamily: "Arial, sans-serif",
      color: "white"
    }}>

      <h1 style={{
        textAlign: "center",
        fontSize: "36px",
        marginBottom: "30px"
      }}>
        🚀 Gen AI Dashboard
      </h1>

      <div style={{
        display: "flex",
        justifyContent: "center",
        gap: "15px",
        flexWrap: "wrap"
      }}>

        <button
          style={buttonStyle}
          onClick={() => callAPI("http://127.0.0.1:8000/generate-video")}
        >
          🎥 Generate Video
        </button>

        <button
          style={buttonStyle}
          onClick={() => callAPI("http://127.0.0.1:8000/generate-blog")}
        >
          📝 Generate Blog
        </button>

        <button
          style={buttonStyle}
          onClick={() => callAPI("http://127.0.0.1:8000/generate-architecture")}
        >
          🏗 Generate Architecture
        </button>

      </div>

      <div style={{
        marginTop: "40px",
        maxWidth: "900px",
        marginLeft: "auto",
        marginRight: "auto",
        background: "rgba(255,255,255,0.1)",
        backdropFilter: "blur(12px)",
        padding: "20px",
        borderRadius: "15px",
        boxShadow: "0 10px 25px rgba(0,0,0,0.4)"
      }}>
        <pre style={{
          whiteSpace: "pre-wrap",
          fontSize: "14px"
        }}>
          {data || "👉 Click a button to generate AI output..."}
        </pre>
      </div>

    </div>
  );
}

// 🔥 Stylish button CSS
const buttonStyle = {
  padding: "12px 20px",
  borderRadius: "10px",
  border: "none",
  cursor: "pointer",
  fontSize: "16px",
  fontWeight: "bold",
  background: "linear-gradient(135deg, #ff7e5f, #feb47b)",
  color: "white",
  boxShadow: "0 4px 15px rgba(0,0,0,0.3)",
  transition: "all 0.3s ease"
};