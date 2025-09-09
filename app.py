import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from route import nearest_neighbor, two_opt, total_route_distance

st.set_page_config(page_title="Delivery Route Optimizer", layout="centered")
st.title("Delivery Route Optimizer — Greedy (Nearest Neighbor)")

st.sidebar.header("Input options")
uploaded = st.sidebar.file_uploader("Upload CSV (columns: id,x,y)", type=['csv'])
use_sample = st.sidebar.checkbox("Use sample points (included)", value=True)
apply_2opt = st.sidebar.checkbox("Apply 2-opt local improvement (optional)", value=True)
return_to_start = st.sidebar.checkbox("Return to warehouse (closed route)", value=True)

SAMPLE_PATH = "sample_locations.csv"

def load_df():
    if uploaded is not None:
        try:
            df = pd.read_csv(uploaded)
        except Exception as e:
            st.error(f"Couldn't read uploaded CSV: {e}")
            st.stop()
    elif use_sample:
        df = pd.read_csv(SAMPLE_PATH)
    else:
        st.info("Upload a CSV or enable sample points from the sidebar.")
        st.stop()
    df.columns = [c.strip().lower() for c in df.columns]
    if not set(['id','x','y']).issubset(set(df.columns)):
        st.error("CSV must contain columns: id, x, y (case-insensitive)")
        st.stop()
    df = df[['id','x','y']].copy()
    df['x'] = df['x'].astype(float)
    df['y'] = df['y'].astype(float)
    df['id'] = df['id'].astype(str)
    return df

df = load_df()
st.subheader("Input points")
st.dataframe(df.reset_index(drop=True))

warehouse_row = df[df['id'].str.upper() == 'W']
if not warehouse_row.empty:
    wh = warehouse_row.iloc[0]
else:
    wh = df.iloc[0]
warehouse = (str(wh['id']), float(wh['x']), float(wh['y']))

deliveries = []
for _, r in df.iterrows():
    if str(r['id']) == warehouse[0] and float(r['x']) == warehouse[1] and float(r['y']) == warehouse[2]:
        continue
    deliveries.append((str(r['id']), float(r['x']), float(r['y'])))

st.markdown(f"**Warehouse:** {warehouse[0]} at ({warehouse[1]}, {warehouse[2]}) — {len(deliveries)} deliveries")

if st.button("Compute optimized route"):
    route_nn = nearest_neighbor(warehouse, deliveries)
    dist_nn = total_route_distance(route_nn, return_to_start)
    if apply_2opt:
        route_opt = two_opt(route_nn)
        dist_opt = total_route_distance(route_opt, return_to_start)
    else:
        route_opt = route_nn
        dist_opt = dist_nn

    st.subheader("Route (order of IDs)")
    route_ids = [p[0] for p in route_opt]
    if return_to_start and route_ids[-1] != warehouse[0]:
        route_ids = route_ids + [warehouse[0]]
    st.write(" -> ".join(route_ids))

    st.write(f"**Total distance:** {dist_opt:.3f} (Euclidean units)")

    st.subheader("Route table (CSV)")
    out_df = pd.DataFrame(route_opt, columns=['id','x','y'])
    if return_to_start:
        out_df = out_df.append({'id':warehouse[0],'x':warehouse[1],'y':warehouse[2]}, ignore_index=True)
    st.dataframe(out_df.reset_index(drop=True))

    fig, ax = plt.subplots(figsize=(6,6))
    xs = list(out_df['x'])
    ys = list(out_df['y'])
    ax.plot(xs, ys, marker='o', linewidth=1)
    for idx, row in out_df.iterrows():
        ax.annotate(str(row['id']), (row['x'], row['y']), textcoords='offset points', xytext=(4,4))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Delivery Route (Greedy)')
    ax.grid(True)
    st.pyplot(fig)

    csv = out_df.to_csv(index=False)
    st.download_button('Download route CSV', data=csv, file_name='route.csv', mime='text/csv')

st.markdown('---')
st.markdown('**Sample CSV format (id,x,y)** — warehouse id "W" is recommended in the first row or use first row as warehouse.')
st.code('id,x,y\nW,50,50\nP1,20,30\nP2,60,20', language='csv')
st.markdown('You can upload your own CSV (columns id,x,y). Coordinate units can be simple X/Y positions (Euclidean). For lat/lon use Haversine — not implemented in this demo.')
