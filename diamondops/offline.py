
def take_field_offline(fields, field_name):
    for field in fields:
        if field.name == field_name:
            field.active = False
            return field
    return None
