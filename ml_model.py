import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def prepare_ml_data(laps_df):
    df = laps_df.dropna(subset=["LapTime", "Compound"]).copy()
    df["LapTimeSeconds"] = df["LapTime"].dt.total_seconds()
    compound_map = {
        "SOFT": 0,
        "MEDIUM": 1,
        "HARD": 2
    }
    df["CompoundEncoded"] = df["Compound"].map(compound_map)

    features = df[["LapNumber", "CompoundEncoded"]]
    target = df["LapTimeSeconds"]

    return features, target

def train_lap_time_model(laps_df):
    X, y = prepare_ml_data(laps_df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    return model, mae

import pandas as pd


def predict_lap_time(model, lap_number, tyre):
    """
    Predict lap time using the trained ML model
    """
    compound_map = {
        "Soft": 0,
        "Medium": 1,
        "Hard": 2
    }

    X = pd.DataFrame([{
        "LapNumber": lap_number,
        "CompoundEncoded": compound_map[tyre]
    }])

    return model.predict(X)[0]
