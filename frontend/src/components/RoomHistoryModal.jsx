import { useEffect, useMemo, useState } from "react";

import {
  CartesianGrid,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

import "./RoomHistoryModal.css";

const RANGE_OPTIONS = {
  "6h": 360,
  "24h": 1440,
  "3d": 4320,
  "7d": 10080,
};

function formatTime(value) {
  const date = new Date(value);

  return date.toLocaleString([], {
    day: "2-digit",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
  });
}

export default function RoomHistoryModal({ room, onClose }) {
  const [history, setHistory] = useState([]);
  const [range, setRange] = useState("24h");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!room) return;

    async function loadHistory() {
      setLoading(true);

      try {
        const limit = RANGE_OPTIONS[range];
        const response = await fetch(
          `/api/history/${room.id}?limit=${limit}`
        );

        if (!response.ok) {
          throw new Error(`API returned HTTP ${response.status}`);
        }

        const data = await response.json();
        data.reverse();

        setHistory(data);
        setError(null);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    loadHistory();
  }, [room, range]);

  const chartData = useMemo(() => {
    return history.map((reading) => ({
      ...reading,
      timestamp: new Date(reading.collected_at).getTime(),
    }));
  }, [history]);

  if (!room) return null;

  return (
    <div
      className="history-overlay"
      onMouseDown={(event) => {
        if (event.target === event.currentTarget) {
          onClose();
        }
      }}
    >
      <div
        className="history-modal"
        role="dialog"
        aria-modal="true"
        aria-labelledby="room-history-title"
      >
        <div className="history-modal__header">
          <div>
            <p className="history-modal__eyebrow">JARVIS history</p>
            <h2 id="room-history-title">{room.name}</h2>
            <p>Temperature and humidity history</p>
          </div>

          <button
            className="history-modal__close"
            onClick={onClose}
            aria-label="Close"
            type="button"
          >
            ×
          </button>
        </div>

        <div className="history-range">
          {Object.keys(RANGE_OPTIONS).map((option) => (
            <button
              key={option}
              type="button"
              className={
                range === option
                  ? "history-range__button history-range__button--active"
                  : "history-range__button"
              }
              onClick={() => setRange(option)}
            >
              {option}
            </button>
          ))}
        </div>

        {loading && (
          <div className="history-message">Loading history…</div>
        )}

        {error && (
          <div className="history-message history-message--error">
            {error}
          </div>
        )}

        {!loading && !error && (
          <>
            <div className="history-chart">
              <div className="history-chart__heading">
                <span>Temperature</span>
                <strong> °C</strong>
              </div>

              <ResponsiveContainer width="100%" height={280}>
                <LineChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis
                    dataKey="timestamp"
                    type="number"
                    domain={["dataMin", "dataMax"]}
                    tickFormatter={(value) =>
                      new Date(value).toLocaleTimeString([], {
                        hour: "2-digit",
                        minute: "2-digit",
                      })
                    }
                  />
                  <YAxis domain={["auto", "auto"]} width={45} />
                  <Tooltip
                    labelFormatter={(value) => formatTime(value)}
                    formatter={(value) => [
                      `${value} °C`,
                      "Temperature",
                    ]}
                  />
                  <Line
                    type="monotone"
                    dataKey="temperature_c"
                    dot={false}
                    strokeWidth={2}
                    isAnimationActive={false}
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>

            <div className="history-chart">
              <div className="history-chart__heading">
                <span>Relative humidity</span>
                <strong> % RH</strong>
              </div>

              <ResponsiveContainer width="100%" height={280}>
                <LineChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis
                    dataKey="timestamp"
                    type="number"
                    domain={["dataMin", "dataMax"]}
                    tickFormatter={(value) =>
                      new Date(value).toLocaleTimeString([], {
                        hour: "2-digit",
                        minute: "2-digit",
                      })
                    }
                  />
                  <YAxis domain={["auto", "auto"]} width={45} />
                  <Tooltip
                    labelFormatter={(value) => formatTime(value)}
                    formatter={(value) => [
                      `${value} % RH`,
                      "Humidity",
                    ]}
                  />
                  <Line
                    type="monotone"
                    dataKey="humidity_pct"
                    dot={false}
                    strokeWidth={2}
                    isAnimationActive={false}
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>

            <div className="history-modal__footer">
              {chartData.length.toLocaleString()} readings
              {chartData.some((reading) => reading.calibrated) &&
                " • Calibrated"}
            </div>
          </>
        )}
      </div>
    </div>
  );
}
