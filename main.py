#1-misol
roy_tup = (1, 2, 3, 4, 5)
print(roy_tup)

new = list(roy_tup)
roy_tup = sum(new)

print(f'Jami summa: {roy_tup}')

#2-misol
son = input('Sonni kiriting: ')
new = tuple(map(int, son.split(',')))
eng_katta = max(new)

print(f'eng katta son: {eng_katta}')

#3-misol
roy_tuple1 = (1, 2, 3, 4, 5)
roy_tuple2 = (6, 7, 8, 9, 10)

print('Tuple royhati1:', roy_tuple1)
print('Tuple royhati2:', roy_tuple2)

new1 = list(roy_tuple1)
new2 = list(roy_tuple2)

new3 = new1 + new2

print('Jami tuple royhati:', tuple(new3))

#4-misol
roy_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

new_roy = list(roy_tuple)
juft_son = []

for i in new_roy:
    if i % 2 == 0:
        juft_son.append(i)
print(juft_son)
print(tuple(juft_son))

#5-misol
roy_tuple = (14, 35, 75, 54)
print(roy_tuple)

new_roy = list(roy_tuple)
roy = new_roy[::-1]
print(tuple(roy))
