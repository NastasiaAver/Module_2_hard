import random
numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
c = random.choice(numbers)
print('Случайное число: ',c)
list_num = []
for i in range(1, c):
    for j in range(1, c):
            summa = (i+j)
            if c % summa == 0 and i!=j :
                list_num.append([i,j]) #создаем список из возможных пар
def remove(list_num):
    return ([list(k) for k in {*[tuple(sorted(k)) for k in list_num]}]) #удаляем дубликаты пар списка
result = sorted(remove(list_num)) #сортируем список
result_str = str(result) #переводим список в строку
resultat = "".join(c for c in result_str if  c.isdecimal()) #удаляем все элементы, кроме чисел
print(resultat)
