# MODULE 5

ans_yr = ' '
while ans_yr.isdigit() is False or int(ans_yr) != 1799:
    ans_yr = input('Укажите год рождения А.С. Пушкина: ')

ans_dm = ' '
while not (ans_dm == '06.06' or ans_dm == '6.06' or ans_dm == '6.6' or ans_dm == '06/06' or ans_dm == '6/06' or
       ans_dm == '6/6' or ans_dm == '06 июня' or ans_dm == '6 июня'):
    ans_dm = input('Укажите дату рождения А.С. Пушкина: ')
    if (ans_dm == '26.05' or ans_dm == '26.5' or ans_dm == '26/05' or ans_dm == '26/5' or ans_dm == '05/26' or
            ans_dm == '5/26' or ans_dm == '26 мая'):
        print('Вы указали день рождения по юлианскому календарю, но это тоже...')
        break

print('Верно')