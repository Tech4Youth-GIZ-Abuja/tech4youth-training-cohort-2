# Solutions · Lesson 3 · Python errors
# 1. Error names: NameError, TypeError, ValueError, ZeroDivisionError, SyntaxError
# 2. Fixed versions:
name = "Amina"
print(name)              # NameError fixed: make the variable first, and spell it the same
print("Age:", 25)        # TypeError fixed: use a comma (or str(25), or an f-string)
print(int("20"))         # ValueError fixed: give int() digits, not words
print(10 / 2)            # ZeroDivisionError fixed: don't divide by zero
print("Hello")           # SyntaxError fixed: close the bracket
