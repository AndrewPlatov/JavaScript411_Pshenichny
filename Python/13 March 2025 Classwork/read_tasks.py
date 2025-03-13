f = open('my_tasks2.txt')

my_tasks = []
for line in f:
    my_tasks.append(line)
print(my_tasks)