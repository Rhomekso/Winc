# Do not modify these lines
__winc_id__ = "71dd124b4a6e4d268f5973db521394ee"
__human_name__ = "strings"

# Add your code after this line

# This is part one

scorer_name1 = "Ruud Gullit"
scorer_name2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = f"{scorer_name1} {goal_0.__str__()}, {scorer_name2} {goal_1.__str__()}"

report = f"{scorer_name1} scored in the {str(goal_0)}nd minute\n{scorer_name2} scored in the {str(goal_1)}th minute"

# report = f"{scorer_name1} scored in the {goal_0}nd minute\n{scorer_name2} scored in the {goal_1}th minute"

print(report)

# This is Part two
"""
player = "Marco van Basten"
first_name = player[:5]
last_name_len = len(player[6:16])
name_short = f"{player[:1]}. {player[6:16]}"
chant = (f"{first_name}! " * 5).strip()
good_chant = chant != " "

print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)"""

# after this code implement the universial version of the code as intended.
# Make sure to double check the new code with the wincpy check "strings"

player = "Lionel Messi"
first_name = player[0 : player.find(" ")]
last_name_len = len(player[player.find(" ") :][:-1])
# name_short = f"{player[:1]}. {player.find()[+ 1:]}"
name_short = player[:1] + "." + " " + player[player.find(" ") + 1 :]
chant = (f"{first_name}! " * len(first_name))[:-1]
good_chant = chant[-1] != " "

print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)


# example 2
"""
player = "Lionel Messi"
space = player.find(" ")
first_name = player[:space]
last_name_len = len(player[space + 1:])
name_short = f"{player[:1]}. {player[space + 1:]}"
chant = (f"{first_name}! " * len(first_name)).strip()
good_chant = chant != " "

print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)"""
