import fastf1

def load_race_data():
    fastf1.Cache.enable_cache("cache")

    year = 2023
    race_name = "British Grand Prix"

    session = fastf1.get_session(
        year,
        race_name,
        "R",
        backend="ergast"
    )

    session.load()
    return session.laps
