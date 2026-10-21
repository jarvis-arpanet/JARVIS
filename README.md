# JARVIS History Range Update

Files included:

- `frontend/src/components/HistoryPage.jsx`
- `frontend/src/components/HistoryPage.css`
- `backend/apply_history_range_update.py`

The frontend adds `1h`, `2h`, `4h`, `8h`, `12h`, `24h`, `3d`, `1w`, and `1mo`.
It fixes the X-axis so the whole selected period is shown and explicitly breaks lines across missing-data gaps.

The backend is supplied as a one-time updater rather than a replacement `main.py`, so your existing calibration settings and other backend code are preserved.

After copying/pulling the files to the Pi, from `~/JARVIS` run:

```bash
python backend/apply_history_range_update.py
python -m py_compile backend/main.py
```

The updater creates this backup first:

`backend/main.py.before-history-range-update`

Then restart the backend and frontend normally.

No `npm install` is required.
