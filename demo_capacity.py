
from diamondops.planner import suggest_game_duration, stress_test

print(suggest_game_duration(
    18,4,4,2,8,20
))

for row in stress_test(
    18,4,4,2,8,20
):
    print(row)
