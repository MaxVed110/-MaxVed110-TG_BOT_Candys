
def get_a_token(name_file: str):
    res = ''
    with open(name_file, 'r') as file:
        for line in file:
            res += line
    return res