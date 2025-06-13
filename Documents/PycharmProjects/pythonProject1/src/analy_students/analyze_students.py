import csv

# Load CSV data
with open("coursedata.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    students = list(reader)

def get_students_by_qualification(qual):
    return [s for s in students if s['Qualification'].lower() == qual.lower()]

def count_students_by_qualification():
    counts = {}
    for s in students:
        q = s['Qualification']
        counts[q] = counts.get(q, 0) + 1
    return counts

def count_placed():
    return sum(1 for s in students if s['Placed'] == 'Y')

def count_completed_not_placed():
    return sum(1 for s in students if s['Completed'] == 'Y' and s['Placed'] == 'N')

def count_placed_and_not_placed():
    placed = sum(1 for s in students if s['Placed'] == 'Y')
    not_placed = sum(1 for s in students if s['Placed'] == 'N')
    return placed, not_placed

def search_by_name(name):
    return [s for s in students if name.lower() in s['Name'].lower()]

def average_success_rate(batch):
    batch_students = [s for s in students if s['Batch'] == batch]
    if not batch_students:
        return 0
    placed = sum(1 for s in batch_students if s['Placed'] == 'Y')
    return (placed / len(batch_students)) * 100

def max_score_student():
    return max(students, key=lambda s: float(s['Score']))

def all_student_names():
    return [s['Name'] for s in students]

def all_names_qualification_score():
    return [(s['Name'], s['Qualification'], s['Score']) for s in students]

# Menu
print("Enter a number (1-10):")
choice = int(input())

if choice == 1:
    q = input("Enter Qualification: ")
    print(get_students_by_qualification(q))
elif choice == 2:
    print(count_students_by_qualification())
elif choice == 3:
    print("Placed count:", count_placed())
elif choice == 4:
    print("Completed but not placed:", count_completed_not_placed())
elif choice == 5:
    placed, not_placed = count_placed_and_not_placed()
    print(f"Placed: {placed}, Not Placed: {not_placed}")
elif choice == 6:
    name = input("Enter Name to search: ")
    print(search_by_name(name))
elif choice == 7:
    batch = input("Enter Batch: ")
    print("Average Success Rate:", average_success_rate(batch))
elif choice == 8:
    print("Top Scorer:", max_score_student())
elif choice == 9:
    print("Student Names:", all_student_names())
elif choice == 10:
    print("Name, Qualification, Score:")
    for row in all_names_qualification_score():
        print(row)
else:
    print("Invalid choice.")
