values = [3, 4, 3, 3, 3, 7, 6, 6, 6, True, 'wow', 'cool', 'wow', True, 'bad', 69.420, '%', 'of all statistic', 'is', False]
new_arr = [[item for item in values if values.count(item) == count] for count in sorted(set([values.count(n) for n in values]), reverse=True)]
print(new_arr)
