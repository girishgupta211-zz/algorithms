my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list):
    print(counter)
    print(value)

for c, value in enumerate(my_list, 100):
    print(c, value)
