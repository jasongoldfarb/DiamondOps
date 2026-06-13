
from math import ceil, log2

def calculate_byes(teams):
    bracket = 2 ** ceil(log2(teams))
    return bracket - teams

def total_games(teams, guarantee):
    return ceil((teams * guarantee) / 2)

def suggest_game_duration(
    teams,
    guarantee,
    fields,
    days,
    start_hour,
    end_hour,
    buffer=10
):
    games = total_games(teams, guarantee)

    minutes = (
        (end_hour - start_hour)
        * 60
        * days
        * fields
    )

    slot = minutes / games

    return {
        'games': games,
        'byes': calculate_byes(teams),
        'recommended_game_length': round(slot - buffer),
        'buffer': buffer
    }

def stress_test(
    teams,
    guarantee,
    fields,
    days,
    start_hour,
    end_hour
):
    results = []

    for count in range(teams, max(3, teams - 10), -1):
        games = total_games(count, guarantee)

        capacity = round(
            games / (
                fields * days * (end_hour - start_hour)
            ) * 100,
            1
        )

        results.append({
            'teams': count,
            'games': games,
            'byes': calculate_byes(count),
            'capacity': capacity
        })

    return results
