list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
print('Lista przed posortowaniem: ', list_to_sort)
print('Lista po posortowaniu: ', sorted(list_to_sort, key=lambda x: (x[1], x[2])))
