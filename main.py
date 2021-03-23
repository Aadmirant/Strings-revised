# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1

Scorer_1 = 'Ruud Gullit'
Scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = f"{Scorer_1} " + f"{goal_0}, " + f"{Scorer_2} " + f"{goal_1} "
print(scorers)

report = f'{Scorer_1} scored in the {goal_0}nd minute\n{Scorer_2} scored in the {goal_1}th minute'
print(report)

# Part 2

player = 'Ronald Koeman'
first_name = player[:player.find(' ')]
last_name_len = len(player[player.find(' ')+1:])
print(first_name)
print(last_name_len)
name_short = player[:1] +'.' + player[player.find(' '):]
print(name_short)
chant = len(first_name) * (first_name + '! ')
print(chant.lstrip())
good_chant = (first_name+'!'+' ') * 6
print(good_chant)
print(good_chant != chant)
