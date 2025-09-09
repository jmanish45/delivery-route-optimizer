# Delivery Route Optimizer (Greedy Nearest Neighbor)

Simple, ready-made mini-project demonstrating a Greedy Nearest-Neighbor delivery route optimizer with an optional 2-opt local improvement.

## What you get
- `app.py` — Streamlit interface (upload CSV / use sample).
- `route.py` — Core algorithm (nearest neighbor + 2-opt).
- `sample_locations.csv` — Example data.
- `requirements.txt` — Python dependencies.
- `README.md` — This file.

## How to run (no admin password required if Python is already installed)
1. Open Terminal and go to the project folder (where you extracted files).
   ```
   cd ~/Downloads/delivery-route-optimizer
   ```
2. Install required packages **for your user** (no sudo):
   ```
   pip3 install --user -r requirements.txt
   ```
   *If `pip3` not found, try `pip --version` or ask your admin to install Python3/pip.*

3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
   After starting, Streamlit will show a local URL (like `http://localhost:8501`) in the terminal. Open that address in the browser to see the interface.

## If you cannot install packages
- Use the `sample_locations.csv` and `route.py` logic in a local Python environment (no Streamlit) — open `route.py` and import functions into a simple script.

## How to publish to GitHub (without Git on PC)
1. Go to https://github.com and sign in.
2. Create a new repository (green "New" button).
3. Choose repository name (e.g., `delivery-route-optimizer`), make it Public or Private.
4. After repo is created, click **Add file → Upload files** and drag & drop the project files (`app.py`, `route.py`, `sample_locations.csv`, `requirements.txt`, `README.md`).
5. Commit the upload.
6. Share the repo URL with your teacher.

## Notes & Extensions
- This demo uses Euclidean distance (X/Y). For real lat/lon coordinates use Haversine distance.
- You can extend: add capacity, time windows, or integrate maps (folium) later.
