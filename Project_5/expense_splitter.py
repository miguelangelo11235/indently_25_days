print("Welcome to Expense Splitter")

bill: float = float(input("Enter the Bill: $"))

people: list[str] = []

while True:
    name: str = input("Enter name: ")
    if name.strip() == "":
        break

    if name.lower() in people:
        print("Name already exists")
    else:
        people.append(name.lower())

print("Enter percentage for each person. Type 'even' at any time to split equally.")

people_dict: dict[str, float] = {}
total_percentage: float = 100.0
for person in people:
    percentage_input: str = input(f"[{total_percentage:.1f}% Remaining] {person.capitalize()}: ").strip()
    if percentage_input == "":
        percentage_input = '0'
    if percentage_input == "even":
        people_dict[person] = (1 / len(people)) * bill
        break

    people_dict[person] = float(percentage_input) * bill / 100
    total_percentage -= float(percentage_input)

print("\nSummary: ")
for person, share in people_dict.items():
    print(f"{person.capitalize():10}: ${share:>10,.2f}")