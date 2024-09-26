print('Введите целое число')
first = input()
print('Введите целое число')
second = input()
print('Введите целое число')
third = input()
if first == second == third :
    print(3)
elif first == second != third or first != second == third or first == third != second :
    print(2)
elif first != second != third :
    print(0)