
def assign_fields(teams, fields):
    ranked = sorted(teams, key=lambda t: t.seed)
    active = sorted(
        [f for f in fields if f.active],
        key=lambda f: f.name
    )

    assignments = []

    for team, field in zip(ranked, active):
        assignments.append({
            'team': team.name,
            'seed': team.seed,
            'field': field.name
        })

    return assignments
