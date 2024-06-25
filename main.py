#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = (1, 2.5, True, 'Hello',)
print(immutable_var)
#1.Попытайтесь изменить элементы кортежа
#Ответ элементы кортежа не изменяемы! В случае если только,
#внутри кортежа не содержится элемент "список"
immutable_var = (1, [2.5, True], 'Hello',4,)
immutable_var[1][1] = 'Замена'
print(immutable_var)
#Создание изменяемых структур данных:
mutable_list = [3, False, 3.2, 'good']
print(mutable_list)
#1 вариант
mutable_list.append('real')
print(mutable_list)
#2 вариант
mutable_list[3] = True
print(mutable_list)
#так же мы можем в список добавить кортеж внутри которого список
mutable_list = [3, False, 3.2, 'good', immutable_var]
print(mutable_list)

