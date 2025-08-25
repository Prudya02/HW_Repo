import json
import timeit
import sorting
try:
    with open('Input.json') as fin:
        objects = json.load(fin)
except Exception as e:
    print(e)
Marks = [0.0 for i in range(len(objects))]
for i in range(len(objects)):
    Marks[i] = sum(objects[i].get('Marks'))/len(objects[i].get('Marks'))
print(Marks)
print(timeit.timeit(lambda: sorted(Marks), number= 1000000))
print(timeit.timeit(lambda: sorting.MergeSort(Marks), number=1000000))
Mas1 = sorting.MergeSort(Marks)
print(Mas1)


