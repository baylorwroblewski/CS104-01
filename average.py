#variables
howManyEntered = int(0)
total = float(0)
average = float(0)

howMany = int(input("How many test scores would you like to average? "))
#gets test scores from user
while (howMany > howManyEntered):
    testScore = input("Enter Test Score: ")
    total = float(testScore) + float(total)
    howManyEntered = 1 + howManyEntered
#calculates average
average = float(total)/float(howMany)
print(float(average))
