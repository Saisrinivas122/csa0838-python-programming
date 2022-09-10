principal = float(input('Enter principal amount: '))
rate = float(input('Enter rate of interest: '))
time = float(input('Enter time in number of years: '))
Simple_interest = (principal*rate*time)/100
Compound_interest = principal * ((1+rate/100)**time - 1)
print("Simple interest is:", Simple_interest)
print("Compound interest is:", Compound_interest)
