
import json
from diamondops.models import Team, Field
from diamondops.scheduler import assign_fields
from diamondops.report import print_assignments

teams = [Team(**x) for x in json.load(open('data/teams.json'))]
fields = [Field(**x) for x in json.load(open('data/fields.json'))]

print_assignments(assign_fields(teams, fields))
