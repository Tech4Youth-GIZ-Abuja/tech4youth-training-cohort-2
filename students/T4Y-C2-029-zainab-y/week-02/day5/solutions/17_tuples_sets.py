# Solutions · Lesson 17 · Tuples and sets
# 1.
birthday = (14, 3, 2004)
day, month, year = birthday
print(day, month, year)
# 2.
colours = ["red", "blue", "red", "green", "blue", "yellow"]
print(set(colours))               # each colour once (order may differ)
# 3.
mine = {"suya", "jollof", "akara"}
friend = {"akara", "pounded yam", "suya"}
print(mine & friend)              # the foods you both like
