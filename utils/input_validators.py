def check_empty_string(value: str):
    if not value or not value.strip():
        return False
    return True

def check_empty_list(value: list):
    if value is None or not isinstance(value, list) or not value or len(value) == 0:
        return False

    for item in value:
        if not item or not item.strip():
            return False
    return True
