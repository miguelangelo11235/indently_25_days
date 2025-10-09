print("Welcome to Expense Splitter")

bill: float = 0
bill_input: str
people: list[str] = []
name: str = ""
people_dict: dict[str, float] = {}
total_percentage: float = 100.0
percentage_input: str

while True:
    bill_input = input("Enter the Bill: $")

    if bill_input.strip() == '':
        print("\nEnter value for the bill!")
        continue

    if float(bill_input) < 0:
        print("\nOnly positive bill values!")
        continue

    bill = float(bill_input)
    break

while True:
    name = input("Enter name: ")
    if name.strip() == "":
        if len(people) > 0:
            break
        else:
            print("People list is empty")

    if name.lower() in people:
        print("Name already exists")
    elif name == "":
        print("Name is empty")
    else:
        people.append(name.lower())


print("Enter percentage for each person. Type 'even' at any time to split equally.")

for person in people:
    percentage_input = input(f"[{total_percentage:.1f}% Remaining] {person.capitalize()}: ").strip()

    if percentage_input == "":
        percentage_input = '0'
    if percentage_input == "even":
        people_dict[person] = (1 / len(people)) * bill
        break

    while float(percentage_input) >= total_percentage:
        print("Incorrect percentage input. Please try again. Cannot split with a value higher than remaining")
        percentage_input = input(f"[{total_percentage:.1f}% Remaining] {person.capitalize()}: ").strip()
    else:
        people_dict[person] = float(percentage_input) * bill / 100
        total_percentage -= float(percentage_input)

print("\nSummary: ")
print('=' * 20)
for person, share in people_dict.items():
    print(f"{person.capitalize():10}: ${share:>10,.2f}")
print('=' * 20)