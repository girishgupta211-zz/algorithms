import re


def camelcase_to_underscore(key):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', key)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def underscore_to_camelcase(key):
    return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), key)


my_dict = {'firstName': 'Girish', 'lastName': 'Gupta', 'address': 'Gurgaon'}
underscore_dict = {}
for key, value in my_dict.items():
    underscore_dict[camelcase_to_underscore(key)] = value

print(underscore_dict)

camelcase_dict = {}
for key, value in underscore_dict.items():
    camelcase_dict[underscore_to_camelcase(key)] = value

print(camelcase_dict)
