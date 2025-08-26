# def solution (string: str, sub_string: str) -> bool:
#     if not isinstance(string, str) or not isinstance(sub_string, str):
#         raise TypeError('String inputs only')
#     string_end = string[-len(sub_string):]
#     return True if sub_string == string_end else False

def solution (string: str, sub_string: str) -> bool:
    if not isinstance(string, str) or not isinstance(sub_string, str):
        raise TypeError('String inputs only')
    return string.endswith(sub_string)