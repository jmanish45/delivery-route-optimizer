# Delivery Route Optimizer (Greedy Nearest Neighbor)

Simple, ready-made mini-project demonstrating a Greedy Nearest-Neighbor delivery route optimizer with an optional 2-opt local improvement.

## What you get
- `app.py` — Streamlit interface (upload CSV / use sample).
- `route.py` — Core algorithm (nearest neighbor + 2-opt).
- `sample_locations.csv` — Example data.
- `requirements.txt` — Python dependencies.
- `README.md` — This file.



## Notes & Extensions
- This demo uses Euclidean distance (X/Y). For real lat/lon coordinates use Haversine distance.
- You can extend: add capacity, time windows, or integrate maps (folium) later.
