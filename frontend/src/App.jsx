import { useEffect, useMemo, useState } from "react";
import HousePlan from "./components/HousePlan";
import RoomHistoryModal from "./components/RoomHistoryModal";
import "./App.css";

function average(values) {
  const valid = values.filter((value) => Number.isFinite(Number(value))).map(Number);
  if (!valid.length) return "—";
  return (valid.reduce((total, value) => total + value, 0) / valid.length).toFixed(1);
}

function App() {
  const [devices, setDevices] = useState({});
  const [error, setError] = useState(null);
  const [lastUpdated, setLastUpdated] = useState(null);
  const [selectedRoom, setSelectedRoom] = useState(null);

  async function loadDevices() {
    try {
      const response = await fetch("/api/devices");

      if (!response.ok) {
        throw new Error(`API returned HTTP ${response.status}`);
      }

      const data = await response.json();
      setDevices(data);
      setError(null);
      setLastUpdated(new Date());
    } catch (err) {
      setError(err.message);
    }
  }

  useEffect(() => {
    loadDevices();
    const timer = setInterval(loadDevices, 5000);
    return () => clearInterval(timer);
  }, []);

  const stats = useMemo(() => {
    const values = Object.values(devices);
    const online = values.filter((device) => device?.online).length;

    return {
      total: values.length,
      online,
      avgTemp: average(values.map((device) => device?.temperature_c)),
      avgHumidity: average(values.map((device) => device?.humidity_pct)),
    };
  }, [devices]);

  return (
    <div className="app-shell">
      <header className="top-nav">
        <div className="top-nav__inner">
          <div className="brand">
            <div className="brand__mark">J</div>
            <span>JARVIS</span>
          </div>

          <nav className="nav-links" aria-label="Main navigation">
            <button className="nav-link nav-link--active">Overview</button>
            <button className="nav-link">Rooms</button>
            <button className="nav-link">History</button>
            <button className="nav-link">Devices</button>
          </nav>

          <div className={`system-pill ${error ? "system-pill--error" : ""}`}>
            <span />
            {error ? "API offline" : "System online"}
          </div>
        </div>
      </header>

      <main className="page">
        <div className="page-heading">
          <div>
            <p className="page-heading__eyebrow">Home automation</p>
            <h1>Home overview</h1>
            <p>Live room conditions and JARVIS node status.</p>
          </div>

          <div className="last-updated">
            Last refreshed{" "}
            {lastUpdated
              ? lastUpdated.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" })
              : "—"}
          </div>
        </div>

        {error && (
          <div className="error-banner">
            <strong>Unable to contact the JARVIS API.</strong>
            <span>{error}</span>
          </div>
        )}

        <section className="metric-grid" aria-label="Home summary">
          <div className="summary-card">
            <span>Nodes online</span>
            <strong>{stats.online}<small> / {stats.total || "—"}</small></strong>
          </div>

          <div className="summary-card">
            <span>Average temperature</span>
            <strong>{stats.avgTemp}<small>°C</small></strong>
          </div>

          <div className="summary-card">
            <span>Average humidity</span>
            <strong>{stats.avgHumidity}<small>%</small></strong>
          </div>

          <div className="summary-card">
            <span>Collector interval</span>
            <strong>60<small>s</small></strong>
          </div>
        </section>

        <HousePlan
          devices={devices}
          onRoomClick={(id, name) => {
            setSelectedRoom({
              id,
              name,
            });
          }}
        />

        <RoomHistoryModal
          room={selectedRoom}
          onClose={() => setSelectedRoom(null)}
        />
      </main>
    </div>
  );
}

export default App;
