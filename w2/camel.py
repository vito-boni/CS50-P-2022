# A variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName
# Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase.
# For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

def camel2snake():
    name = input('camelCase: ').strip()
    snake_case = ''
    for char in name:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    print(f'snake_case: {snake_case}')
    return snake_case

camel2snake()
