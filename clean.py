import re

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result



states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia',
          'FlOrIda', 'south   carolina##', 'West virginia?']

print(clean_strings(states))
