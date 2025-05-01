testScore = int(input("Enter the student's test score: "))
classRank = int(input("Enter the student's class rank: "))

if testScore >= 90 and classRank >= 25:
    print("Accept")
elif testScore >= 80 and classRank >= 50:
    print("Accept")
elif testScore >= 70 and classRank >= 75:
    print("Accept")
else:
    print("Reject")
