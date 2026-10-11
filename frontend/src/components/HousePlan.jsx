import "./HousePlan.css";

function Room({ name, device, className = "", external = false }) {
  const monitored = Boolean(device);
  const online = Boolean(device?.online);

  return (
    <article
      className={[
        "room-card",
        monitored ? (online ? "room-card--online" : "room-card--offline") : "room-card--empty",
        external ? "room-card--external" : "",
        className,
      ].join(" ")}
    >
      <div className="room-card__top">
        <div>
          <p className="room-card__eyebrow">{external ? "External" : "Room"}</p>
          <h3>{name}</h3>
        </div>

        <span
          className={[
            "room-status",
            monitored ? (online ? "room-status--online" : "room-status--offline") : "room-status--empty",
          ].join(" ")}
        >
          <span className="room-status__dot" />
          {monitored ? (online ? "Online" : "Offline") : "No sensor"}
        </span>
      </div>

      {monitored ? (
        <div className="room-card__metrics">
          <div>
            <span className="metric-label">Temperature</span>
            <strong>
              {device.temperature_c ?? "—"}
              <small>°C</small>
            </strong>
          </div>

          <div>
            <span className="metric-label">Humidity</span>
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
          <span>Wi-Fi {device.wifi_rssi ?? "—"} dBm</span>
          <span>Uptime {device.uptime_s ?? "—"} s</span>
        </div>
      )}
    </article>
  );
}

export default function HousePlan({ devices = {} }) {
  return (
    <div className="house-layout">
      <section className="floor-panel">
        <div className="section-heading">
          <div>
            <p className="section-heading__eyebrow">House</p>
            <h2>Ground floor</h2>
          </div>
          <span className="section-heading__meta">5 spaces</span>
        </div>

        <div className="ground-floor">
          <Room name="Rear Sitting Room" className="rear-sitting" />
          <Room name="Kitchen" device={devices.kitchen} className="kitchen" />
          <Room name="Dining Room" className="dining" />
          <Room name="Front Room" device={devices.front_room} className="front-room" />
          <Room name="Garage" className="garage" />
        </div>
      </section>

      <section className="floor-panel">
        <div className="section-heading">
          <div>
            <p className="section-heading__eyebrow">House</p>
            <h2>First floor</h2>
          </div>
          <span className="section-heading__meta">4 spaces</span>
        </div>

        <div className="first-floor">
          <Room name="Arthur's Room" device={devices.arthurs_room} className="arthurs-room" />
          <Room name="Bedroom 2" className="bedroom-two" />
          <Room name="Bathroom" className="bathroom" />
          <Room name="Main Bedroom" device={devices.main_bedroom} className="main-bedroom" />
        </div>
      </section>

      <section className="floor-panel floor-panel--external">
        <div className="section-heading">
          <div>
            <p className="section-heading__eyebrow">Garden</p>
            <h2>External rooms</h2>
          </div>
          <span className="section-heading__meta">2 spaces</span>
        </div>

        <div className="external-grid">
          <Room name="Bar" device={devices.bar} external />
          <Room name="Shed" device={devices.shed} external />
        </div>
      </section>
    </div>
  );
}
