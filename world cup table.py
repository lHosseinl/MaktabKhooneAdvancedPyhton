wins = dict()
points = dict()
draws = dict()
loses = dict()
goals = dict()
goals2 = dict()
goal_difference = dict()
x = str(input())
Iran = int(x[0])
Spain = int(x[2])
if Iran > Spain:
    wins['Iran'] = wins.get('Iran', 0) + 1
    points['Iran'] = points.get('Iran', 0) + 3
    draws['Iran'] = draws.get('Iran', 0)
    loses['Iran'] = loses.get('Iran', 0)
    goals['Iran'] = goals.get('Iran', 0) + Iran
    goals2['Iran'] = goals2.get('Iran', 0) + Spain
    wins['Spain'] = wins.get('Spain', 0)
    points['Spain'] = points.get('Spain', 0)
    draws['Spain'] = draws.get('Spain', 0)
    loses['Spain'] = loses.get('Spain', 0) + 1
    goals['Spain'] = goals.get('Spain', 0) + Spain
    goals2['Spain'] = goals2.get('Spain', 0) + Iran
elif Iran == Spain:
    wins['Iran'] = wins.get('Iran', 0)
    points['Iran'] = points.get('Iran', 0) + 1
    draws['Iran'] = draws.get('Iran', 0) + 1
    loses['Iran'] = loses.get('Iran', 0)
    goals['Iran'] = goals.get('Iran', 0) + Iran
    goals2['Iran'] = goals2.get('Iran', 0) + Spain
    wins['Spain'] = wins.get('Spain', 0)
    points['Spain'] = points.get('Spain', 0) + 1
    draws['Spain'] = draws.get('Spain', 0) + 1
    loses['Spain'] = loses.get('Spain', 0)
    goals['Spain'] = goals.get('Spain', 0) + Spain
    goals2['Spain'] = goals2.get('Spain', 0) + Iran
else:
    wins['Iran'] = wins.get('Iran', 0)
    points['Iran'] = points.get('Iran', 0)
    draws['Iran'] = draws.get('Iran', 0)
    loses['Iran'] = loses.get('Iran', 0) + 1
    goals['Iran'] = goals.get('Iran', 0) + Iran
    goals2['Iran'] = goals2.get('Iran', 0) + Spain
    wins['Spain'] = wins.get('Spain', 0) + 1
    points['Spain'] = points.get('Spain', 0) + 3
    draws['Spain'] = draws.get('Spain', 0)
    loses['Spain'] = loses.get('Spain', 0)
    goals['Spain'] = goals.get('Spain', 0) + Spain
    goals2['Spain'] = goals2.get('Spain', 0) + Iran
x = str(input())
Iran = int(x[0])
Portugal = int(x[2])
if Iran > Portugal:
    wins['Iran'] = wins.get('Iran', 0) + 1
    points['Iran'] = points.get('Iran', 0) + 3
    draws['Iran'] = draws.get('Iran', 0)
    loses['Iran'] = loses.get('Iran', 0)
    goals['Iran'] = goals.get('Iran', 0) + Iran
    goals2['Iran'] = goals2.get('Iran', 0) + Portugal
    wins['Portugal'] = wins.get('Portugal', 0)
    points['Portugal'] = points.get('Portugal', 0)
    draws['Portugal'] = draws.get('Portugal', 0)
    loses['Portugal'] = loses.get('Portugal', 0) + 1
    goals['Portugal'] = goals.get('Portugal', 0) + Portugal
    goals2['Portugal'] = goals2.get('Portugal', 0) + Iran
elif Iran == Portugal:
    wins['Iran'] = wins.get('Iran', 0)
    points['Iran'] = points.get('Iran', 0) + 1
    draws['Iran'] = draws.get('Iran', 0) + 1
    loses['Iran'] = loses.get('Iran', 0)
    goals['Iran'] = goals.get('Iran', 0) + Iran
    goals2['Iran'] = goals2.get('Iran', 0) + Portugal
    wins['Portugal'] = wins.get('Portugal', 0)
    points['Portugal'] = points.get('Portugal', 0) + 1
    draws['Portugal'] = draws.get('Portugal', 0) + 1
    loses['Portugal'] = loses.get('Portugal', 0)
    goals['Portugal'] = goals.get('Portugal', 0) + Portugal
    goals2['Portugal'] = goals2.get('Portugal', 0) + Iran
else:
    wins['Iran'] = wins.get('Iran', 0)
    points['Iran'] = points.get('Iran', 0)
    draws['Iran'] = draws.get('Iran', 0)
    loses['Iran'] = loses.get('Iran', 0) + 1
    goals['Iran'] = goals.get('Iran', 0) + Iran
    goals2['Iran'] = goals2.get('Iran', 0) + Portugal
    wins['Portugal'] = wins.get('Portugal', 0) + 1
    points['Portugal'] = points.get('Portugal', 0) + 3
    draws['Portugal'] = draws.get('Portugal', 0)
    loses['Portugal'] = loses.get('Portugal', 0)
    goals['Portugal'] = goals.get('Portugal', 0) + Portugal
    goals2['Portugal'] = goals2.get('Portugal', 0) + Iran
x = str(input())
Iran = int(x[0])
Morocco = int(x[2])
if Iran > Morocco:
    wins['Iran'] = wins.get('Iran', 0) + 1
    points['Iran'] = points.get('Iran', 0) + 3
    draws['Iran'] = draws.get('Iran', 0)
    loses['Iran'] = loses.get('Iran', 0)
    goals['Iran'] = goals.get('Iran', 0) + Iran
    goals2['Iran'] = goals2.get('Iran', 0) + Morocco
    wins['Morocco'] = wins.get('Morocco', 0)
    points['Morocco'] = points.get('Morocco', 0)
    draws['Morocco'] = draws.get('Morocco', 0)
    loses['Morocco'] = loses.get('Morocco', 0) + 1
    goals['Morocco'] = goals.get('Morocco', 0) + Morocco
    goals2['Morocco'] = goals2.get('Morocco', 0) + Iran
elif Iran == Morocco:
    wins['Iran'] = wins.get('Iran', 0)
    points['Iran'] = points.get('Iran', 0) + 1
    draws['Iran'] = draws.get('Iran', 0) + 1
    loses['Iran'] = loses.get('Iran', 0)
    goals['Iran'] = goals.get('Iran', 0) + Iran
    goals2['Iran'] = goals2.get('Iran', 0) + Morocco
    wins['Morocco'] = wins.get('Morocco', 0)
    points['Morocco'] = points.get('Morocco', 0) + 1
    draws['Morocco'] = draws.get('Morocco', 0) + 1
    loses['Morocco'] = loses.get('Morocco', 0)
    goals['Morocco'] = goals.get('Morocco', 0) + Morocco
    goals2['Morocco'] = goals2.get('Morocco', 0) + Iran
else:
    wins['Iran'] = wins.get('Iran', 0)
    points['Iran'] = points.get('Iran', 0)
    draws['Iran'] = draws.get('Iran', 0)
    loses['Iran'] = loses.get('Iran', 0) + 1
    goals['Iran'] = goals.get('Iran', 0) + Iran
    goals2['Iran'] = goals2.get('Iran', 0) + Morocco
    wins['Morocco'] = wins.get('Morocco', 0) + 1
    points['Morocco'] = points.get('Morocco', 0) + 3
    draws['Morocco'] = draws.get('Morocco', 0)
    loses['Morocco'] = loses.get('Morocco', 0)
    goals['Morocco'] = goals.get('Morocco', 0) + Morocco
    goals2['Morocco'] = goals2.get('Morocco', 0) + Iran
x = str(input())
Spain = int(x[0])
Portugal = int(x[2])
if Spain > Portugal:
    wins['Spain'] = wins.get('Spain', 0) + 1
    points['Spain'] = points.get('Spain', 0) + 3
    draws['Spain'] = draws.get('Spain', 0)
    loses['Spain'] = loses.get('Spain', 0)
    goals['Spain'] = goals.get('Spain', 0) + Spain
    goals2['Spain'] = goals2.get('Spain', 0) + Portugal
    wins['Portugal'] = wins.get('Portugal', 0)
    points['Portugal'] = points.get('Portugal', 0)
    draws['Portugal'] = draws.get('Portugal', 0)
    loses['Portugal'] = loses.get('Portugal', 0) + 1
    goals['Portugal'] = goals.get('Portugal', 0) + Portugal
    goals2['Portugal'] = goals2.get('Portugal', 0) + Spain
elif Spain == Portugal:
    wins['Spain'] = wins.get('Spain', 0)
    points['Spain'] = points.get('Spain', 0) + 1
    draws['Spain'] = draws.get('Spain', 0) + 1
    loses['Spain'] = loses.get('Spain', 0)
    goals['Spain'] = goals.get('Spain', 0) + Spain
    goals2['Spain'] = goals2.get('Spain', 0) + Portugal
    wins['Portugal'] = wins.get('Portugal', 0)
    points['Portugal'] = points.get('Portugal', 0) + 1
    draws['Portugal'] = draws.get('Portugal', 0) + 1
    loses['Portugal'] = loses.get('Portugal', 0)
    goals['Portugal'] = goals.get('Portugal', 0) + Portugal
    goals2['Portugal'] = goals2.get('Portugal', 0) + Spain
else:
    wins['Spain'] = wins.get('Spain', 0)
    points['Spain'] = points.get('Spain', 0)
    draws['Spain'] = draws.get('Spain', 0)
    loses['Spain'] = loses.get('Spain', 0) + 1
    goals['Spain'] = goals.get('Spain', 0) + Spain
    goals2['Spain'] = goals2.get('Spain', 0) + Portugal
    wins['Portugal'] = wins.get('Portugal', 0) + 1
    points['Portugal'] = points.get('Portugal', 0) + 3
    draws['Portugal'] = draws.get('Portugal', 0)
    loses['Portugal'] = loses.get('Portugal', 0)
    goals['Portugal'] = goals.get('Portugal', 0) + Portugal
    goals2['Portugal'] = goals2.get('Portugal', 0) + Spain
x = str(input())
Spain = int(x[0])
Morocco = int(x[2])
if Spain > Morocco:
    wins['Spain'] = wins.get('Spain', 0) + 1
    points['Spain'] = points.get('Spain', 0) + 3
    draws['Spain'] = draws.get('Spain', 0)
    loses['Spain'] = loses.get('Spain', 0)
    goals['Spain'] = goals.get('Spain', 0) + Spain
    goals2['Spain'] = goals2.get('Spain', 0) + Morocco
    wins['Morocco'] = wins.get('Morocco', 0)
    points['Morocco'] = points.get('Morocco', 0)
    draws['Morocco'] = draws.get('Morocco', 0)
    loses['Morocco'] = loses.get('Morocco', 0) + 1
    goals['Morocco'] = goals.get('Morocco', 0) + Morocco
    goals2['Morocco'] = goals2.get('Morocco', 0) + Spain
elif Spain == Morocco:
    wins['Spain'] = wins.get('Spain', 0)
    points['Spain'] = points.get('Spain', 0) + 1
    draws['Spain'] = draws.get('Spain', 0) + 1
    loses['Spain'] = loses.get('Spain', 0)
    goals['Spain'] = goals.get('Spain', 0) + Spain
    goals2['Spain'] = goals2.get('Spain', 0) + Morocco
    wins['Morocco'] = wins.get('Morocco', 0)
    points['Morocco'] = points.get('Morocco', 0) + 1
    draws['Morocco'] = draws.get('Morocco', 0) + 1
    loses['Morocco'] = loses.get('Morocco', 0)
    goals['Morocco'] = goals.get('Morocco', 0) + Morocco
    goals2['Morocco'] = goals2.get('Morocco', 0) + Spain
else:
    wins['Spain'] = wins.get('Spain', 0)
    points['Spain'] = points.get('Spain', 0)
    draws['Spain'] = draws.get('Spain', 0)
    loses['Spain'] = loses.get('Spain', 0) + 1
    goals['Spain'] = goals.get('Spain', 0) + Spain
    goals2['Spain'] = goals2.get('Spain', 0) + Morocco
    wins['Morocco'] = wins.get('Morocco', 0) + 1
    points['Morocco'] = points.get('Morocco', 0) + 3
    draws['Morocco'] = draws.get('Morocco', 0)
    loses['Morocco'] = loses.get('Morocco', 0)
    goals['Morocco'] = goals.get('Morocco', 0) + Morocco
    goals2['Morocco'] = goals2.get('Morocco', 0) + Spain
x = str(input())
Portugal = int(x[0])
Morocco = int(x[2])
if Portugal > Morocco:
    wins['Portugal'] = wins.get('Portugal', 0) + 1
    points['Portugal'] = points.get('Portugal', 0) + 3
    draws['Portugal'] = draws.get('Portugal', 0)
    loses['Portugal'] = loses.get('Portugal', 0)
    goals['Portugal'] = goals.get('Portugal', 0) + Portugal
    goals2['Portugal'] = goals2.get('Portugal', 0) + Morocco
    wins['Morocco'] = wins.get('Morocco', 0)
    points['Morocco'] = points.get('Morocco', 0)
    draws['Morocco'] = draws.get('Morocco', 0)
    loses['Morocco'] = loses.get('Morocco', 0) + 1
    goals['Morocco'] = goals.get('Morocco', 0) + Morocco
    goals2['Morocco'] = goals2.get('Morocco', 0) + Portugal
elif Portugal == Morocco:
    wins['Portugal'] = wins.get('Portugal', 0)
    points['Portugal'] = points.get('Portugal', 0) + 1
    draws['Portugal'] = draws.get('Portugal', 0) + 1
    loses['Portugal'] = loses.get('Portugal', 0)
    goals['Portugal'] = goals.get('Portugal', 0) + Portugal
    goals2['Portugal'] = goals2.get('Portugal', 0) + Morocco
    wins['Morocco'] = wins.get('Morocco', 0)
    points['Morocco'] = points.get('Morocco', 0) + 1
    draws['Morocco'] = draws.get('Morocco', 0) + 1
    loses['Morocco'] = loses.get('Morocco', 0)
    goals['Morocco'] = goals.get('Morocco', 0) + Morocco
    goals2['Morocco'] = goals2.get('Morocco', 0) + Portugal
else:
    wins['Portugal'] = wins.get('Portugal', 0)
    points['Portugal'] = points.get('Portugal', 0)
    draws['Portugal'] = draws.get('Portugal', 0)
    loses['Portugal'] = loses.get('Portugal', 0) + 1
    goals['Portugal'] = goals.get('Portugal', 0) + Portugal
    goals2['Portugal'] = goals2.get('Portugal', 0) + Morocco
    wins['Morocco'] = wins.get('Morocco', 0) + 1
    points['Morocco'] = points.get('Morocco', 0) + 3
    draws['Morocco'] = draws.get('Morocco', 0)
    loses['Morocco'] = loses.get('Morocco', 0)
    goals['Morocco'] = goals.get('Morocco', 0) + Morocco
    goals2['Morocco'] = goals2.get('Morocco', 0) + Portugal
goal_difference['Spain'] = (goals['Spain']-goals2['Spain'])
goal_difference['Iran'] = (goals['Iran']-goals2['Iran'])
goal_difference['Portugal'] = (goals['Portugal']-goals2['Portugal'])
goal_difference['Morocco'] = (goals['Morocco']-goals2['Morocco'])

Spain_list = ['Spain', wins['Spain'], loses['Spain'], draws['Spain'], goal_difference['Spain'], points['Spain']]
Iran_list = ['Iran', wins['Iran'], loses['Iran'], draws['Iran'], goal_difference['Iran'], points['Iran']]
Portugal_list = ['Portugal', wins['Portugal'], loses['Portugal'], draws['Portugal'], goal_difference['Portugal'], points['Portugal']]
Morocco_list = ['Morocco', wins['Morocco'], loses['Morocco'], draws['Morocco'], goal_difference['Morocco'], points['Morocco']]
countries_list = [Spain_list, Iran_list, Portugal_list, Morocco_list]

countries_list.sort(key = lambda x: x[0])
countries_list.sort(key = lambda x: x[1])
countries_list.reverse()
countries_list.sort(key = lambda x: x[5])
countries_list.reverse()
print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' % (countries_list[0][0], countries_list[0][1], countries_list[0][2], countries_list[0][3], countries_list[0][4], countries_list[0][5]))
print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' % (countries_list[1][0], countries_list[1][1], countries_list[1][2], countries_list[1][3], countries_list[1][4], countries_list[1][5]))
print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' % (countries_list[2][0], countries_list[2][1], countries_list[2][2], countries_list[2][3], countries_list[2][4], countries_list[2][5]))
print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' % (countries_list[3][0], countries_list[3][1], countries_list[3][2], countries_list[3][3], countries_list[3][4], countries_list[3][5]))