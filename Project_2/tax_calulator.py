base_income: float = float(input("Enter your base income: "))
tax_rate: float = float(input("Enter your tax rate: ")) / 100
taxed: float = base_income * tax_rate

print("=" * 40)
print("Income Tax Calculator")
print("=" * 40)
print(f"Base Income:            ${base_income:.2f}")
print(f"Tax Rate:               {tax_rate:.1%}")
print("." * 40)
print(f"Taxed:                  ${taxed:.2f}")
