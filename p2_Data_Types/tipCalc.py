#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to Tip calculator.")
inputTotal = input("What was the total of the bill? ")
inputTip = input("What percentage tip would you like to give? 10, 12, or 15? ")
inputPeople = input("How many people will split the bill? ")

total = round(float(inputTotal),2)
tipPercent = int(inputTip)
people = int(inputPeople)


if(tipPercent < 10):
  print("Why are you even eating out? ")
if(tipPercent > 15):
  print("Wow, you are generous ")

tip = (1+(.01*tipPercent)) * total / people 



print("Each person should pay: $" + str(tip))