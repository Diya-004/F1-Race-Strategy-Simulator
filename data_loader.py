import fastf1
import pandas as pd

# Enable cache (required for FastF1)
fastf1.Cache.enable_cache("cache")

def load_race_data(year=2023, race_name="British Grand Prix"):
    session = fastf1.get_session(year, race_name, "R")
    session.load()

    laps = session.laps
    return laps
