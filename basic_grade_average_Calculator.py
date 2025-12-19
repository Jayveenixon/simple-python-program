# Ask how many subjects
num_subjects = int(input("Enter number of subjects: "))

total = 0

# Loop to get grades
for i in range(1, num_subjects + 1):
    grade = float(input(f"Enter grade for subject {i}: "))
    total += grade

# Calculate average
average = total / num_subjects

# Display average
print("\nYour Average Grade is:", round(average, 2))

# Determine remark
if average >= 90:
    print("Remark: Excellent")
elif average >= 85:
    print("Remark: Very Good")
elif average >= 80:
    print("Remark: Good")
elif average >= 75:
    print("Remark: Passed")
else:
    print("Remark: Failed")

print("=========================================")