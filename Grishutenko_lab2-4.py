"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	
    Задача 1:
        В илиндрический сосуд налили v1 воды. Уровень воды при этом достигает 
        высоты h1 см. В жидкость полностью погрузили деталь. При этом уровень 
        жидкости в сосуде поднялся на h2 см. Чему равен объем детали? Ответ 
        запишите в переменную v2. Решение задачи оформите в виде функции 
        volume(v1,h1,h2), которая будет возвращать результат v2 Например, при
        значениях v1=2000; h1=12; h2=9 volume(2000,12,9) вернет значение 
        переменной v2=1500.
"""
def volume(v1, h1, h2):
    return 2000*9/12

print('Введите v1: ', end='')
v1 = input()
print('Введите h1: ', end='')
h1 = input()
print('Введите h2: ', end='')
h2 = input()
result = volume(v1, h1, h2)
print(result)