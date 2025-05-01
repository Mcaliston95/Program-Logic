def admission_decision(testScore, classRank):
    if testScore >= 90 and classRank >= 25:
        return "Accept"
    elif testScore >= 80 and classRank >= 50:
        return "Accept"
    elif testScore >= 70 and classRank >= 75:
        return "Accept"
    else:
        return "Reject"

# Unit Test #2
print(admission_decision(87, 60))  # Expected outcome: Accept