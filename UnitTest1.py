salary = 60000.0
numDependents = 3

stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = salary * 0.025 * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

print("State Tax: $", stateTax)
print("Federal Tax: $", federalTax)
print("Dependents: $", dependentDeduction)
print("Salary: $", salary)
print("Take Home Pay: $", takeHomePay)