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
  main_room: { name: "Main Room", colour: "#7F56D9" },
  kitchen: { name: "Kitchen", colour: "#F79009" },
  front_room: { name: "Front Room", colour: "#2E90FA" },
  gym: { name: "Gym", colour: "#12B76A" },
  arthurs_room: { name: "Arthur's Room", colour: "#EE46BC" },
  lilys_room: { name: "Lily's Room", colour: "#6172F3" },
  main_bedroom: { name: "Main Bedroom", colour: "#F04438" },
  bar: { name: "Bar", colour: "#06AED4" },
};

const RANGE_OPTIONS = {
  "1h": { label: "1h", hours: 1, bucketMinutes: 1 },
  "2h": { label: "2h", hours: 2, bucketMinutes: 1 },
  "4h": { label: "4h", hours: 4, bucketMinutes: 1 },
  "8h": { label: "8h", hours: 8, bucketMinutes: 1 },
  "12h": { label: "12h", hours: 12, bucketMinutes: 1 },
  "24h": { label: "24h", hours: 24, bucketMinutes: 1 },
  "3d": { label: "3d", hours: 72, bucketMinutes: 3 },
  "1w": { label: "1w", hours: 168, bucketMinutes: 5 },
  "1mo": { label: "1mo", hours: 24 * 30, bucketMinutes: 15 },
};

function formatTime(timestamp, hours) {
  const date = new Date(timestamp);

  if (hours <= 24) {
    return date.toLocaleString([], {
      hour: "2-digit",
      minute: "2-digit",
    });
  }

  if (hours <= 168) {
    return date.toLocaleString([], {
      weekday: "short",
      hour: "2-digit",
      minute: "2-digit",
    });
  }

  return date.toLocaleDateString([], {
    day: "2-digit",
    month: "short",
  });
}

function formatTooltipTime(timestamp) {
  return new Date(timestamp).toLocaleString([], {
    day: "2-digit",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
  });
}

/*
 * Snap readings from every Pico onto one shared time grid.
 *
 * The poller contacts rooms a few seconds apart. Without this,
 * e.g. Kitchen 20:01:03 and Front Room 20:01:07 become two
 * independent chart rows. connectNulls={false} then sees missing
 * values between almost every reading and draws tiny disconnected
 * dashes.
 *
 * Rounding them all to the selected graph bucket fixes that while
 * retaining genuine missing-data gaps.
 */
function snapToBucket(timestamp, bucketMinutes) {
  const bucketMs = bucketMinutes * 60 * 1000;

  return Math.round(timestamp / bucketMs) * bucketMs;
}

export default function HistoryPage() {
  const roomIds = Object.keys(ROOMS);

  const [selectedRooms, setSelectedRooms] = useState(roomIds);
  const [range, setRange] = useState("24h");
  const [history, setHistory] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [windowEnd, setWindowEnd] = useState(Date.now());

  const rangeConfig = RANGE_OPTIONS[range];

  useEffect(() => {
    let cancelled = false;

    async function loadHistory() {
      setLoading(true);
      setError(null);

      const requestEnd = Date.now();
      setWindowEnd(requestEnd);

      try {
        const responses = await Promise.all(
          roomIds.map(async (roomId) => {
            const params = new URLSearchParams({
              hours: String(rangeConfig.hours),
              bucket_minutes: String(rangeConfig.bucketMinutes),
            });

            const response = await fetch(
              `/api/history/${roomId}?${params.toString()}`
            );

            if (!response.ok) {
              throw new Error(
                `${ROOMS[roomId].name} returned HTTP ${response.status}`
              );
            }

            const data = await response.json();

            return [roomId, data];
          })
        );

        if (!cancelled) {
          setHistory(Object.fromEntries(responses));
        }
      } catch (err) {
        if (!cancelled) {
          setError(err.message);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    loadHistory();

    return () => {
      cancelled = true;
    };
  }, [range]);

  function toggleRoom(roomId) {
    setSelectedRooms((current) => {
      if (current.includes(roomId)) {
        return current.filter((id) => id !== roomId);
      }

      return [...current, roomId];
    });
  }

  const windowStart =
    windowEnd - rangeConfig.hours * 60 * 60 * 1000;

  const chartData = useMemo(() => {
    const buckets = new Map();

    const ensureBucket = (timestamp) => {
      if (!buckets.has(timestamp)) {
        buckets.set(timestamp, { timestamp });
      }

      return buckets.get(timestamp);
    };

    for (const roomId of roomIds) {
      const readings = [...(history[roomId] ?? [])]
        .map((reading) => {
          const rawTimestamp =
            new Date(reading.collected_at).getTime();

          if (!Number.isFinite(rawTimestamp)) {
            return null;
          }

          return {
            ...reading,
            snappedTimestamp: snapToBucket(
              rawTimestamp,
              rangeConfig.bucketMinutes
            ),
          };
        })
        .filter(Boolean)
        .sort(
          (a, b) =>
            a.snappedTimestamp - b.snappedTimestamp
        );

      let previousTimestamp = null;

      for (const reading of readings) {
        const timestamp = reading.snappedTimestamp;

        if (previousTimestamp !== null) {
          const expectedGapMs =
            rangeConfig.bucketMinutes * 60 * 1000;

          /*
           * Normal adjacent buckets remain connected.
           * Only a genuinely missing stretch of at least three
           * graph buckets gets an explicit null break.
           */
          if (
            timestamp - previousTimestamp >
            expectedGapMs * 2.5
          ) {
            const breakTimestamp = snapToBucket(
              previousTimestamp +
                (timestamp - previousTimestamp) / 2,
              rangeConfig.bucketMinutes
            );

            const breakRow = ensureBucket(breakTimestamp);

            breakRow[`${roomId}_temp`] = null;
            breakRow[`${roomId}_humidity`] = null;
          }
        }

        const row = ensureBucket(timestamp);

        row[`${roomId}_temp`] =
          reading.temperature_c;

        row[`${roomId}_humidity`] =
          reading.humidity_pct;

        previousTimestamp = timestamp;
      }
    }

    /*
     * These empty rows force the axis to cover the full selected
     * period. They do not join any room lines.
     */
    ensureBucket(windowStart);
    ensureBucket(windowEnd);

    return Array.from(buckets.values()).sort(
      (a, b) => a.timestamp - b.timestamp
    );
  }, [
    history,
    rangeConfig.bucketMinutes,
    windowStart,
    windowEnd,
  ]);

  return (
    <div className="history-page">
      <div className="history-page__heading">
        <div>
          <p className="history-page__eyebrow">
            Environmental history
          </p>

          <h1>Room comparison</h1>

          <p>
            Compare temperature and relative humidity across
            JARVIS room nodes.
          </p>
        </div>

        <div className="history-range">
          {Object.entries(RANGE_OPTIONS).map(
            ([key, option]) => (
              <button
                key={key}
                type="button"
                className={
                  range === key
                    ? "history-range__button history-range__button--active"
                    : "history-range__button"
                }
                onClick={() => setRange(key)}
              >
                {option.label}
              </button>
            )
          )}
        </div>
      </div>

      <section className="room-selector">
        <div className="room-selector__header">
          <div>
            <strong>Rooms</strong>
            <span>{selectedRooms.length} selected</span>
          </div>

          <div className="room-selector__actions">
            <button
              type="button"
              onClick={() => setSelectedRooms(roomIds)}
            >
              Select all
            </button>

            <button
              type="button"
              onClick={() => setSelectedRooms([])}
            >
              Clear
            </button>
          </div>
        </div>

        <div className="room-selector__grid">
          {roomIds.map((roomId) => (
            <label key={roomId} className="room-toggle">
              <input
                type="checkbox"
                checked={selectedRooms.includes(roomId)}
                onChange={() => toggleRoom(roomId)}
              />

              <span
                className="room-toggle__swatch"
                style={{
                  backgroundColor: ROOMS[roomId].colour,
                }}
                aria-hidden="true"
              />

              <span>{ROOMS[roomId].name}</span>
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
                <p>Calibrated room temperature</p>
              </div>

              <strong>°C</strong>
            </div>

            <ResponsiveContainer width="100%" height={500}>
              <LineChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />

                <XAxis
                  dataKey="timestamp"
                  type="number"
                  scale="time"
                  domain={[windowStart, windowEnd]}
                  tickFormatter={(value) =>
                    formatTime(value, rangeConfig.hours)
                  }
                  minTickGap={45}
                />

                <YAxis
                  domain={["auto", "auto"]}
                  width={50}
                  unit="°"
                />

                <Tooltip
                  labelFormatter={(value) =>
                    formatTooltipTime(value)
                  }
                  formatter={(value, name) => [
                    value == null ? "No data" : `${value} °C`,
                    name,
                  ]}
                />

                <Legend />

                {selectedRooms.map((roomId) => (
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
                ))}
              </LineChart>
            </ResponsiveContainer>
          </section>

          <section className="comparison-chart">
            <div className="comparison-chart__heading">
              <div>
                <h2>Relative humidity</h2>
                <p>Calibrated room humidity</p>
              </div>

              <strong>% RH</strong>
            </div>

            <ResponsiveContainer width="100%" height={500}>
              <LineChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />

                <XAxis
                  dataKey="timestamp"
                  type="number"
                  scale="time"
                  domain={[windowStart, windowEnd]}
                  tickFormatter={(value) =>
                    formatTime(value, rangeConfig.hours)
                  }
                  minTickGap={45}
                />

                <YAxis
                  domain={["auto", "auto"]}
                  width={50}
                  unit="%"
                />

                <Tooltip
                  labelFormatter={(value) =>
                    formatTooltipTime(value)
                  }
                  formatter={(value, name) => [
                    value == null ? "No data" : `${value} % RH`,
                    name,
                  ]}
                />

                <Legend />

                {selectedRooms.map((roomId) => (
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
                ))}
              </LineChart>
            </ResponsiveContainer>
          </section>
        </>
      )}
    </div>
  );
}
