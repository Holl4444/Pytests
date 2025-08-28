def read_file(filename):
    try:
        with open(filename) as file:
            contents = file.read()
            return contents
    except Exception:
        raise