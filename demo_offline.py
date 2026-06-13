
import json

from diamondops.models import Field
from diamondops.offline import take_field_offline

fields = [Field(**x) for x in json.load(open('data/fields.json'))]

field = take_field_offline(
    fields,
    'Championship Complex'
)

print('Field Offline:', field.name)

for f in fields:
    print(f.name, f.active)
