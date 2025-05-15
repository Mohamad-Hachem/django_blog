def f():
    list1, list2, list3 = [], [True], [False]
    return list1 or list2 or list3

print(f())