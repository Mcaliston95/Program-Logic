salary = 1250.0
numDependents = 2

stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = salary * 0.025 * numDependents

totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

print("State tax: $", stateTax)
print("Federal tax: $", federalTax)
print("Depends: $", dependentDeduction)
print("Salary: $", salary)
print("Take-home pay: $", takeHomePay)
