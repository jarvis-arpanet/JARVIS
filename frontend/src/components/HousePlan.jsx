import "./HousePlan.css";

function Room({
  name,
  device,
  deviceId,
  onSelect,
  className = "",
  external = false,
}) {
  const monitored = Boolean(device);
  const online = Boolean(device?.online);

  function selectRoom() {
    if (monitored && onSelect) {
      onSelect(deviceId, name);
    }
  }

  return (
    <article
      className={[
        "room-card",
        monitored
          ? online
            ? "room-card--online"
            : "room-card--offline"
          : "room-card--empty",
        external ? "room-card--external" : "",
        monitored ? "room-card--clickable" : "",
        className,
      ].join(" ")}
      onClick={selectRoom}
      onKeyDown={(event) => {
        if (
          monitored &&
          (event.key === "Enter" || event.key === " ")
        ) {
          event.preventDefault();
          selectRoom();
        }
      }}
      role={monitored ? "button" : undefined}
      tabIndex={monitored ? 0 : undefined}
    >
      <div className="room-card__top">
        <div>
          <p className="room-card__eyebrow">
            {external ? "External" : "Room"}
          </p>

          <h3>{name}</h3>
        </div>

        <span
          className={[
            "room-status",
            monitored
              ? online
                ? "room-status--online"
                : "room-status--offline"
              : "room-status--empty",
          ].join(" ")}
        >
          <span className="room-status__dot" />

          {monitored
            ? online
              ? "Online"
              : "Offline"
            : "No sensor"}
        </span>
      </div>

      {monitored ? (
        <div className="room-card__metrics">
          <div>
            <span className="metric-label">
              Temperature
            </span>

            <strong>
              {device.temperature_c ?? "—"}
              <small>°C</small>
            </strong>
          </div>

          <div>
            <span className="metric-label">
              Humidity
            </span>

            <strong>
              {device.humidity_pct ?? "—"}
              <small>%</small>
            </strong>
          </div>
        </div>
      ) : (
        <div className="room-card__empty-state">
          Ready for a JARVIS room node
        </div>
      )}

      {monitored && (
        <div className="room-card__footer">
          <span>
            Wi-Fi {device.wifi_rssi ?? "—"} dBm
          </span>

          <span>
            Uptime {device.uptime_s ?? "—"} s
          </span>
        </div>
      )}
    </article>
  );
}

export default function HousePlan({
  devices = {},
  onRoomClick,
}) {
  return (
    <div className="house-layout">
      <section className="floor-panel">
        <div className="section-heading">
          <div>
            <p className="section-heading__eyebrow">
              House
            </p>

            <h2>Ground floor</h2>
          </div>

          <span className="section-heading__meta">
            5 spaces
          </span>
        </div>

        <div className="ground-floor">
          <Room
            name="Main Room"
            deviceId="main_room"
            device={devices.main_room}
            onSelect={onRoomClick}
            className="main-room"
          />

          <Room
            name="Kitchen"
            deviceId="kitchen"
            device={devices.kitchen}
            onSelect={onRoomClick}
            className="kitchen"
          />

          <Room
            name="Dining Room"
            className="dining"
          />

          <Room
            name="Front Room"
            deviceId="front_room"
            device={devices.front_room}
            onSelect={onRoomClick}
            className="front-room"
          />

          <Room
            name="Gym"
            deviceId="gym"
            device={devices.gym}
            onSelect={onRoomClick}
            className="gym"
          />
        </div>
      </section>

      <section className="floor-panel">
        <div className="section-heading">
          <div>
            <p className="section-heading__eyebrow">
              House
            </p>

            <h2>First floor</h2>
          </div>

          <span className="section-heading__meta">
            4 spaces
          </span>
        </div>

        <div className="first-floor">
          <Room
            name="Arthur's Room"
            deviceId="arthurs_room"
            device={devices.arthurs_room}
            onSelect={onRoomClick}
            className="arthurs-room"
          />

          <Room
            name="Lily's Room"
            deviceId="lilys_room"
            device={devices.lilys_room}
            onSelect={onRoomClick}
            className="lilys-room"
          />

          <Room
            name="Bathroom"
            className="bathroom"
          />

          <Room
            name="Main Bedroom"
            deviceId="main_bedroom"
            device={devices.main_bedroom}
            onSelect={onRoomClick}
            className="main-bedroom"
          />
        </div>
      </section>

      <section className="floor-panel floor-panel--external">
        <div className="section-heading">
          <div>
            <p className="section-heading__eyebrow">
              Garden
            </p>

            <h2>External rooms</h2>
          </div>

          <span className="section-heading__meta">
            1 space
          </span>
        </div>

        <div className="external-grid">
          <Room
            name="Bar"
            deviceId="bar"
            device={devices.bar}
            onSelect={onRoomClick}
            external
          />
        </div>
      </section>
    </div>
  );
}