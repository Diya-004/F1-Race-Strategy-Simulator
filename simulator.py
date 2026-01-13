from ml_model import predict_lap_time


def simulate_race(laps_df, pit_lap, tyre, model):
    race_output = []

    # Tyre wear rate (% per lap)
    tyre_wear_rate = {
        "Soft": 1.8,
        "Medium": 1.2,
        "Hard": 0.8
    }

    tyre_life = 100

    for lap in range(1, 71):
        # ML-based lap time prediction
        lap_time = predict_lap_time(model, lap, tyre)

        # Tyre degradation
        tyre_life -= tyre_wear_rate[tyre]

        # Pit stop logic
        if lap == pit_lap:
            lap_time += 22  # pit stop penalty (seconds)
            tyre_life = 100

        race_output.append({
            "Lap": lap,
            "LapTime": lap_time,
            "TyreLife": max(tyre_life, 0)
        })

    return race_output


def estimate_position_change(total_time_diff):
    """
    Estimate position change based on total race time difference.
    Rough assumption: 1 position ~ 5 seconds
    """
    positions = int(abs(total_time_diff) // 5)

    if total_time_diff < 0:
        return f"Gain ~{positions} positions"
    elif total_time_diff > 0:
        return f"Lose ~{positions} positions"
    else:
        return "No position change"
