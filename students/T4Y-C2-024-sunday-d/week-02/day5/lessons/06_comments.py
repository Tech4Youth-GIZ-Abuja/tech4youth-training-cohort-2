# Lesson 6 · Comments: notes for humans
# Everything after a # is ignored by Python.
# Run it:  python 06_comments.py

# Good comments explain WHY, not WHAT.
vat_rate = 0.075  # Nigeria's VAT is 7.5%

price = 10000
vat = price * vat_rate
print("VAT to pay:", vat)

"""
Text inside three quotes can cover many lines.
People use it for longer notes, like a description at the top of a file.
"""

# You can "switch off" a line by putting # in front of it (called commenting out):
# print("This line will not run")

print("Done")

# ── TRY IT YOURSELF ──
# 1. Add a comment at the top of your 05_variables.py file that says what the file does.
# 2. Comment out the print("Done") line. Run the file. What changed?
# 3. VS Code shortcut: select some lines and press Ctrl + / (Mac: Cmd + /). What happens?
