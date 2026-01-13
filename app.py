import streamlit as st
import pandas as pd
import plotly.express as px
import time

from data_loader import load_race_data
from simulator import simulate_race, estimate_position_change
from ml_model import train_lap_time_model

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="F1 Race Strategy Simulator",
    layout="wide"
)

st.title("🏎️ F1 Race Strategy Simulator")
st.caption(
    "An interactive Formula 1 race strategy tool using real telemetry data and machine learning "
    "to compare tyre strategies, pit timing, and race outcomes."
)

st.info(
    "Lap times are predicted using a machine learning regression model trained on real Formula 1 race data. "
    "Predictions vary based on lap number and tyre compound."
)

# ------------------ SIDEBAR ------------------
st.sidebar.header("🧠 Strategy Comparison")

st.sidebar.subheader("Plan A")
tyre_a = st.sidebar.selectbox("Plan A Tyre", ["Soft", "Medium", "Hard"])
pit_a = st.sidebar.slider("Plan A Pit Lap", 10, 60, 25)

st.sidebar.subheader("Plan B")
tyre_b = st.sidebar.selectbox("Plan B Tyre", ["Soft", "Medium", "Hard"], index=1)
pit_b = st.sidebar.slider("Plan B Pit Lap", 10, 60, 40)

# ------------------ LOAD DATA ------------------
laps = load_race_data()

# ------------------ LOAD & CACHE ML MODEL ------------------
@st.cache_resource
def load_ml_model(_laps_df):
    model, mae = train_lap_time_model(_laps_df)
    return model, mae


model, mae = load_ml_model(laps)
st.caption(f"🧠 ML Model Mean Absolute Error (MAE): ~{mae:.2f} seconds")

# ------------------ SIMULATE STRATEGIES ------------------
race_a = simulate_race(laps, pit_lap=pit_a, tyre=tyre_a, model=model)
race_b = simulate_race(laps, pit_lap=pit_b, tyre=tyre_b, model=model)

df_a = pd.DataFrame(race_a)
df_b = pd.DataFrame(race_b)

df_a["Strategy"] = "Plan A"
df_b["Strategy"] = "Plan B"

df = pd.concat([df_a, df_b])

# ------------------ STRATEGY COMPARISON PLOT ------------------
fig = px.line(
    df,
    x="Lap",
    y="LapTime",
    color="Strategy",
    title="🧠 Strategy Comparison: Lap Time Evolution",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# ------------------ TOTAL RACE TIME ------------------
total_a = df_a["LapTime"].sum()
total_b = df_b["LapTime"].sum()

st.subheader("🏁 Total Race Time Comparison")

col1, col2 = st.columns(2)

with col1:
    st.metric("Plan A Total Time (s)", f"{total_a:.2f}")

with col2:
    st.metric("Plan B Total Time (s)", f"{total_b:.2f}")

# ------------------ POSITION IMPACT ------------------
time_diff = total_a - total_b

st.subheader("📈 Estimated Position Impact")
st.info(f"Plan A vs Plan B: {estimate_position_change(time_diff)}")

# ------------------ TYRE WEAR ------------------
st.subheader("🛞 Tyre Degradation Analysis")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### Plan A Tyre Life")
    tyre_life_a = df_a["TyreLife"].iloc[-1]
    st.progress(int(tyre_life_a))
    st.caption(f"Remaining Tyre Life: {tyre_life_a:.1f}%")

with col_b:
    st.markdown("### Plan B Tyre Life")
    tyre_life_b = df_b["TyreLife"].iloc[-1]
    st.progress(int(tyre_life_b))
    st.caption(f"Remaining Tyre Life: {tyre_life_b:.1f}%")

# ------------------ INTERACTIVE REPLAY ------------------
st.subheader("🎥 Interactive Lap-by-Lap Replay")

replay_strategy = st.radio(
    "Replay Strategy",
    ["Plan A", "Plan B"],
    horizontal=True
)

replay_df = df_a if replay_strategy == "Plan A" else df_b
max_lap = int(replay_df["Lap"].max())

current_lap = st.slider(
    "Select Lap",
    min_value=1,
    max_value=max_lap,
    value=1
)

current_state = replay_df[replay_df["Lap"] == current_lap]

lap_time = current_state["LapTime"].values[0]
tyre_life = current_state["TyreLife"].values[0]

progress = int((current_lap / max_lap) * 100)

st.progress(progress)

col_r1, col_r2 = st.columns(2)

with col_r1:
    st.metric("Lap Time (s)", f"{lap_time:.2f}")

with col_r2:
    st.metric("Remaining Tyre Life (%)", f"{tyre_life:.1f}")
