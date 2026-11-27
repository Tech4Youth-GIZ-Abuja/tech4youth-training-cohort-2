# Solutions · Lesson 10 · Converting types
# Example answers: 5 | 5 | 30
# 1.
a = int(input("First number: "))
b = int(input("Second number: "))
print(a + b)                      # 10, not 55, because we converted with int()
# 2.
c = float(input("Temperature in °C: "))
f = c * 9 / 5 + 32
print(f"{c}°C is {f}°F")          # 30.0°C is 86.0°F
# 3. Typing "abc" gives: ValueError: invalid literal for int() with base 10: 'abc'
