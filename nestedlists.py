nested = [
    'x',
    [10, 20, 30],
    ['a', 'b', ['c', 'd', ['e', 'f']]],
    [1, 2, [3, 4, [5, 6, 7]]]
]
print(nested[1][2])
print(nested[2][2][1])
print(nested[2][2][2][0])
print(nested[3][2][2][1])
print(nested[3][2][2][2])
