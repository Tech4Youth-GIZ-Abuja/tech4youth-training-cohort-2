# Lesson 5 · Variables: named boxes that remember values
# The = sign means "store the value on the right in the box on the left".
# Run it:  python 05_variables.py

name = "Amina"
age = 22
is_student = True

print(name)
print(age)
print(is_student)

# A variable can change. The new value replaces the old one.
score = 0
print("Start:", score)
score = score + 5
print("After one right answer:", score)
score = score + 5
print("After two right answers:", score)

# Good names say what is inside the box:
monthly_rent = 150000
favourite_food = "jollof rice"
print(favourite_food, "costs less than", monthly_rent)

# ── TRY IT YOURSELF ──
# 1. Make variables for your first name, your city and your age. Print each one.
# 2. Make a variable steps = 0. Add 1000 to it three times. Print it after each step.
# 3. Which names are NOT allowed?  2nd_place   my-name   first name   class   total_2   (Try them!)
