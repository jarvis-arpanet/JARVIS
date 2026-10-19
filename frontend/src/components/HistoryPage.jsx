import { useEffect, useMemo, useState } from "react";

import {
  CartesianGrid,
  Legend,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

import "./HistoryPage.css";

const ROOMS = {
  main_room: {
    name: "Main Room",
    colour: "#7F56D9",
  },

  kitchen: {
    name: "Kitchen",
    colour: "#F79009",
  },

  front_room: {
    name: "Front Room",
    colour: "#2E90FA",
  },

  gym: {
    name: "Gym",
    colour: "#12B76A",
  },

  arthurs_room: {
    name: "Arthur's Room",
    colour: "#EE46BC",
  },

  lilys_room: {
    name: "Lily's Room",
    colour: "#6172F3",
  },

  main_bedroom: {
    name: "Main Bedroom",
    colour: "#F04438",
  },

  bar: {
    name: "Bar",
    colour: "#06AED4",
  },
};

const RANGE_OPTIONS = {
  "6h": 360,
  "24h": 1440,
  "3d": 4320,
};

function formatTime(timestamp) {
  return new Date(timestamp).toLocaleString([], {
    day: "2-digit",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
  });
}

export default function HistoryPage() {
  const roomIds = Object.keys(ROOMS);

  const [selectedRooms, setSelectedRooms] = useState(roomIds);
  const [range, setRange] = useState("24h");
  const [history, setHistory] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadHistory() {
      setLoading(true);
      setError(null);

      try {
        const limit = RANGE_OPTIONS[range];

        const responses = await Promise.all(
          roomIds.map(async (roomId) => {
            const response = await fetch(
              `/api/history/${roomId}?limit=${limit}`
            );

            if (!response.ok) {
              throw new Error(
                `${ROOMS[roomId].name} returned HTTP ${response.status}`
              );
            }

            const data = await response.json();

            return [
              roomId,
              data.reverse(),
            ];
          })
        );

        setHistory(
          Object.fromEntries(responses)
        );
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    loadHistory();
  }, [range]);

  function toggleRoom(roomId) {
    setSelectedRooms((current) => {
      if (current.includes(roomId)) {
        return current.filter(
          (id) => id !== roomId
        );
      }

      return [
        ...current,
        roomId,
      ];
    });
  }

  const chartData = useMemo(() => {
    const buckets = new Map();

    for (const roomId of roomIds) {
      const readings = history[roomId] ?? [];

      for (const reading of readings) {
        const date = new Date(
          reading.collected_at
        );

        date.setSeconds(0, 0);

        const timestamp = date.getTime();

        if (!buckets.has(timestamp)) {
          buckets.set(timestamp, {
            timestamp,
          });
        }

        const row = buckets.get(timestamp);

        row[`${roomId}_temp`] =
          reading.temperature_c;

        row[`${roomId}_humidity`] =
          reading.humidity_pct;
      }
    }

    return Array.from(
      buckets.values()
    ).sort(
      (a, b) =>
        a.timestamp - b.timestamp
    );
  }, [history]);

  return (
    <div className="history-page">

      <div className="history-page__heading">
        <div>
          <p className="history-page__eyebrow">
            Environmental history
          </p>

          <h1>Room comparison</h1>

          <p>
            Compare temperature and relative humidity
            across JARVIS room nodes.
          </p>
        </div>

        <div className="history-range">
          {Object.keys(RANGE_OPTIONS).map(
            (option) => (
              <button
                key={option}
                type="button"
                className={
                  range === option
                    ? "history-range__button history-range__button--active"
                    : "history-range__button"
                }
                onClick={() =>
                  setRange(option)
                }
              >
                {option}
              </button>
            )
          )}
        </div>
      </div>

      <section className="room-selector">
        <div className="room-selector__header">
          <div>
            <strong>Rooms</strong>

            <span>
              {selectedRooms.length} selected
            </span>
          </div>

          <div className="room-selector__actions">
            <button
              type="button"
              onClick={() =>
                setSelectedRooms(roomIds)
              }
            >
              Select all
            </button>

            <button
              type="button"
              onClick={() =>
                setSelectedRooms([])
              }
            >
              Clear
            </button>
          </div>
        </div>

        <div className="room-selector__grid">
          {roomIds.map((roomId) => (
            <label
              key={roomId}
              className="room-toggle"
            >
              <input
                type="checkbox"
                checked={
                  selectedRooms.includes(
                    roomId
                  )
                }
                onChange={() =>
                  toggleRoom(roomId)
                }
              />

              <span
                className="room-toggle__swatch"
                style={{
                  backgroundColor: ROOMS[roomId].colour,
                }}
                aria-hidden="true"
              />

              <span>
                {ROOMS[roomId].name}
              </span>
            </label>
          ))}
        </div>
      </section>

      {loading && (
        <div className="history-page__message">
          Loading room history…
        </div>
      )}

      {error && (
        <div className="history-page__message history-page__message--error">
          {error}
        </div>
      )}

      {!loading && !error && (
        <>
          <section className="comparison-chart">
            <div className="comparison-chart__heading">
              <div>
                <h2>Temperature</h2>

                <p>
                  Calibrated room temperature
                </p>
              </div>

              <strong>°C</strong>
            </div>

            <ResponsiveContainer
              width="100%"
              height={500}
            >
              <LineChart data={chartData}>
                <CartesianGrid
                  strokeDasharray="3 3"
                />

                <XAxis
                  dataKey="timestamp"
                  type="number"
                  domain={[
                    "dataMin",
                    "dataMax",
                  ]}
                  tickFormatter={(value) =>
                    new Date(
                      value
                    ).toLocaleTimeString(
                      [],
                      {
                        hour: "2-digit",
                        minute: "2-digit",
                      }
                    )
                  }
                />

                <YAxis
                  domain={["auto", "auto"]}
                  width={50}
                  unit="°"
                />

                <Tooltip
                  labelFormatter={(value) =>
                    formatTime(value)
                  }
                  formatter={(
                    value,
                    name
                  ) => [
                    `${value} °C`,
                    name,
                  ]}
                />

                <Legend />

                {selectedRooms.map(
                  (roomId) => (
                    <Line
                      key={roomId}
                      type="linear"
                      dataKey={`${roomId}_temp`}
                      name={ROOMS[roomId].name}
                      stroke={ROOMS[roomId].colour}
                      dot={false}
                      connectNulls={false}
                      strokeWidth={2}
                      isAnimationActive={false}
                    />
                  )
                )}
              </LineChart>
            </ResponsiveContainer>
          </section>

          <section className="comparison-chart">
            <div className="comparison-chart__heading">
              <div>
                <h2>Relative humidity</h2>

                <p>
                  Calibrated room humidity
                </p>
              </div>

              <strong>% RH</strong>
            </div>

            <ResponsiveContainer
              width="100%"
              height={500}
            >
              <LineChart data={chartData}>
                <CartesianGrid
                  strokeDasharray="3 3"
                />

                <XAxis
                  dataKey="timestamp"
                  type="number"
                  domain={[
                    "dataMin",
                    "dataMax",
                  ]}
                  tickFormatter={(value) =>
                    new Date(
                      value
                    ).toLocaleTimeString(
                      [],
                      {
                        hour: "2-digit",
                        minute: "2-digit",
                      }
                    )
                  }
                />

                <YAxis
                  domain={["auto", "auto"]}
                  width={50}
                  unit="%"
                />

                <Tooltip
                  labelFormatter={(value) =>
                    formatTime(value)
                  }
                  formatter={(
                    value,
                    name
                  ) => [
                    `${value} % RH`,
                    name,
                  ]}
                />

                <Legend />

                {selectedRooms.map(
                  (roomId) => (
                    <Line
                      key={roomId}
                      type="linear"
                      dataKey={`${roomId}_humidity`}
                      name={ROOMS[roomId].name}
                      stroke={ROOMS[roomId].colour}
                      dot={false}
                      connectNulls={false}
                      strokeWidth={2}
                      isAnimationActive={false}
                    />
                  )
                )}
              </LineChart>
            </ResponsiveContainer>
          </section>
        </>
      )}
    </div>
  );
}
