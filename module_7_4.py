print('------\nДомашнее задание по теме "Форматирование строк"\n------')

team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 8
team2_num = 9
score_1 = 48
score_2 = 52
team1_time = 1852.625
team2_time = 2353.375

tasks_total = score_1 + score_2

time_avg = (team1_time + team2_time) / tasks_total

# challenge_result
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# Использование %
print('В команде %s участников: %s !' % (team1_name, team1_num))
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s !' % {'team1_num': 8, 'team2_num': 9})

# Использование format()
print('Команда {team2_name} решила задач: {score_2} !'.format(team2_name='Волшебники данных', score_2=52))
print('{team2_name} решили задачи за {team2_time} !'.format(team2_name='Волшебники данных', team2_time=2353.375))

# Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

print('------')