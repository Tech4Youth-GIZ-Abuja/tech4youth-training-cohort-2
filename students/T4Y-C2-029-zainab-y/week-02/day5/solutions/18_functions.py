# Solutions · Lesson 18 · Functions
# 1.
def square(n):
    return n * n

print(square(4), square(9))       # 16 81

# 2.
def is_adult(age):
    return age >= 18

print(is_adult(20), is_adult(15)) # True False

# 3.
def naira_to_dollars(naira, rate=1500):
    return round(naira / rate, 2)

print(naira_to_dollars(10000))    # 6.67
print(naira_to_dollars(10000, rate=1600))
