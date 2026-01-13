

# F1 Race Strategy Simulator
## Machine Learning • Data Engineering • Simulation • Web Deployment

An end-to-end Formula 1 race strategy simulation platform that uses real F1 telemetry data and
machine learning to analyze the impact of tyre choices and pit stop timing on race outcomes.

The application enables interactive comparison of race strategies and demonstrates applied data
science, ML modeling, and production-ready deployment.

 Live Application: https://f1-race-strategy-simulator-xenyappdkdsqzbrqxtbgngp.streamlit.app/

## Problem Statement
Race strategy decisions in Formula 1—such as tyre compound selection and pit stop timing—
have a significant impact on lap times and final race position.

This project explores:

•How different strategies influence race performance

•How machine learning can model lap-time behavior using real telemetry

•How simulation results can be visualized interactively for decision analysis

## Key Features
•Real Formula 1 Telemetry Integration: 
Loads official race data using the FastF1 API.

•Machine Learning–Driven Lap Time Prediction:
Trains a regression model to predict lap times based on race context.

•Strategy Comparison Engine:
Compare two race strategies (Plan A vs Plan B) with different tyres and pit laps.

•Tyre Degradation Modeling:
Visual representation of tyre wear progression during the race.

•Race Outcome Estimation:
Estimates position gain or loss based on total race time differences.

•Interactive Visualization Dashboard:
Dynamic charts and lap-by-lap replay using Streamlit and Plotly.

•Production Deployment:
Deployed as a live, publicly accessible web application.

## Machine Learning Details

Model: Random Forest Regressor

Training Data: Real F1 race lap telemetry

Features:

Lap number

Tyre compound (encoded)

Target Variable:

Lap time (seconds)

Evaluation Metric:

Mean Absolute Error (MAE)

Performance:

MAE ≈ 1.57 seconds

The model is trained once and cached to ensure efficient inference during simulation runs.

## Technical Architecture
f1-race-strategy-simulator/

── app.py               # Streamlit UI & orchestration

── simulator.py         # Race simulation and strategy logic

── ml_model.py          # ML training and prediction functions

── data_loader.py       # FastF1 data ingestion

── requirements.txt     # Project dependencies

└── cache/               # Local FastF1 cache

## Technology Stack

Python

FastF1 – Official Formula 1 telemetry data

Scikit-learn – Machine learning

Pandas / NumPy – Data processing

Plotly – Interactive data visualization

Streamlit – Web application framework

Streamlit Community Cloud – Deployment

## Results & Impact
• Built an end-to-end race strategy simulator using real Formula 1 telemetry data

• Implemented a machine learning pipeline to train and evaluate a lap-time prediction model (MAE ≈ 1.6s)

• Integrated ML predictions into a race simulation to compare tyre and pit stop strategies

• Designed an interactive dashboard to visualize lap-time evolution, tyre degradation, and race
outcomes

• Deployed the application as a live web app, making the project accessible for real-time experimentation

This project reflects practical experience in data processing, applied machine learning,
simulation logic, and deployment, similar to real-world data science and ML engineering
workflows.

## Author
Joginipally Diya Rao

## Disclaimer
This project is intended for educational and analytical purposes only.
It is not an official Formula 1 prediction or strategy system.
