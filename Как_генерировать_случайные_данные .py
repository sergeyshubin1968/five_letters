from faker import Faker

mosk = Faker('ru_RU')
lst = []
for i in range(10):
    j = (mosk.name(), mosk.email(), mosk.address(), mosk.job(),)
    lst.append(j)
for i in lst:
    print(i)
