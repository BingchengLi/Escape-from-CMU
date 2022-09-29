hwAverage = 99.6
quizAverage = 96.9
midtermAverage = 97.7
final = midtermAverage
tp = 60

grade = (0.3 * hwAverage) + (0.1 * quizAverage) + (0.2 * midtermAverage) + (0.2 * final) + (0.2 * tp)

if grade >= 89.5: 
    print("A", grade)
elif grade >= 79.5:
    print("B", grade)
elif grade >= 69.5:
    print("C", grade)
elif grade >= 59.5:
    print("D", grade)
else:
    print("R", grade)