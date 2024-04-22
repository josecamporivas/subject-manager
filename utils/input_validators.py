def check_empty_string(value: str):
    if not value or not value.strip():
        return False
    return True
