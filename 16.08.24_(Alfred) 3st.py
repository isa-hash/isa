af = 'Второе домашнее задание: '
def out_red(text):
    print("\033[36m{}".format(text))
out_red(af)

total_tasks = ( 12 )
Number_of_hours_spent = ( 1.5 )
course_name = ( 'Python' )
Time_per_task = ( Number_of_hours_spent / total_tasks )
print ( ' Курс:' ,course_name , ', всего задач:' ,total_tasks , 'затрачено часов:' ,  Number_of_hours_spent , ', среднее время выполнения ' , Time_per_task )

# Вариант с отдельными запятыми в тексте(что не обязательно)
total_tasks = ( 12 )
Number_of_hours_spent = ( 1.5 )
course_name = ( 'Python' )
Time_per_task = ( Number_of_hours_spent / total_tasks )
print ( ' Курс:' ,course_name ,"," , 'всего задач:' ,total_tasks , 'затрачено часов:' ,  Number_of_hours_spent , ',', 'среднее время выполнения ' , Time_per_task )

# Вариант только с переменными
a = ' Курс:'
b = ','
c = 'всего задач:'
d = 'затрачено часов:'
e = 'среднее время выполнения '

total_tasks = ( 12 )
Number_of_hours_spent = ( 1.5 )
course_name = ( 'Python' )
Time_per_task = ( Number_of_hours_spent / total_tasks )
print ( a ,course_name ,b , c ,total_tasks , d ,  Number_of_hours_spent , b, e , Time_per_task )
