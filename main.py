# create the initial variables below
#Age in years
age = 28
#Sex: 0 for female, 1 for male
sex = 0
#bmi: body mass index
bmi = 26.2
#num_of_children
num_of_children = 3
#smoker: 0 for non-smoker, 1 for a smoker
smoker = 0

# Add insurance estimate formula below
insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425*num_of_children) + (24000 * smoker) - 12500

print("This person's insurance cost is " + str(insurance_cost) + "dollars")

# Age Factor
age += 4

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425*num_of_children) + (24000 * smoker) - 12500

print("This person's insurance cost is " + str(new_insurance_cost) + "dollars")

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + "dollars")

# BMI Factor

#refine age to original value
age = 28

bmi += 3.1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425*num_of_children) + (24000 * smoker) - 12500

print("This person's insurance cost is " + str(new_insurance_cost) + "dollars")

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + "dollars")

# Male vs. Female Factor

#redefine BMI to its original value
bmi = 26.2
#changing sex to male (1) from female (0)
sex = 1

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425*num_of_children) + (24000 * smoker) - 12500

print("This person's insurance cost is " + str(new_insurance_cost) + "dollars")

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + "dollars")

# Extra Practice

#what if person is a female (sex = 0) smoker (smoker = 1)
#remember to return sex to 0
sex = 0

smoker = 1

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425*num_of_children) + (24000 * smoker) - 12500

print("This person's insurance cost is " + str(new_insurance_cost) + "dollars")

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for smoker instead of a non-smoker is " + str(change_in_insurance_cost) + "dollars")