invalid_values = ["none", "не знаю", "неа", "нет", "хз", "None", ""]

user_states = {}

def is_valid(value):
    value = value.lower()
    if value in invalid_values:
        return False
    return True