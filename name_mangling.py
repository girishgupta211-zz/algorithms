class Org(object):
    __employees = []
    _employees = []


Org._Org__employees.append('Eric')
print(Org._Org__employees)
print(Org._employees)

print(dir(Org))


class Gog(Org):
    __employees = []


print(dir(Gog))
