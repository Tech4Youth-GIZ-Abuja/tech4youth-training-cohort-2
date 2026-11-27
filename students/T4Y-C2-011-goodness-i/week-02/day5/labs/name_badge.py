# Lab 6 · Name badge maker: string manipulation
# Example answers: chioma | NWANKWO | software developer

first = input("First name: ").strip().title()
last = input("Last name: ").strip().title()
role = input("Your dream job: ").strip()

initials = first[0] + last[0]
username = (first + "." + last).lower()
line = "=" * 30

print(line)
print(f"{first} {last} ({initials})".center(30))
print(role.upper().center(30))
print(line)
print(f"Username: {username}")
print(f"Your name has {len(first + last)} letters.")
if "developer" in role.lower() or "engineer" in role.lower():
    print("Tech job! You're in the right class.")
