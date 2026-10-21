# JARVIS History Alignment Fix

This fixes the fragmented/dotted history lines introduced by the previous update.

## Cause

Each Pico is polled a few seconds apart. The previous frontend merged readings
using their exact timestamps while `connectNulls={false}` was enabled.

That meant one room might have a point at 20:01:03 and another at 20:01:07.
Those became separate chart rows, so every room appeared to have missing data
between most samples.

## Fix

All readings are now snapped onto the common graph bucket:

- 1 minute through 24h
- 3 minutes for 3d
- 5 minutes for 1w
- 15 minutes for 1mo

Real long gaps still create a break in the line.

## Copy

Replace:

`frontend/src/components/HistoryPage.jsx`

No backend or CSS change is needed for this correction.

No npm install is required.
