
def print_assignments(assignments):
    print('\nTRAVEL REPORT')
    print('=' * 40)

    for row in assignments:
        print(
            f"Seed #{row['seed']} -> "
            f"{row['team']} -> {row['field']}"
        )
