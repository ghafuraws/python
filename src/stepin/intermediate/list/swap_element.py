x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x)

x[0], x[1], x[2] = x[2], x[1], x[0]
print(x)


"""
$ python swap_element.py
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8, 7, 3, 4, 5, 6, 7, 8, 9]
"""
