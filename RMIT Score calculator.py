def calculate_course_grade():
    num_assignments = int(input("Enter the number of assignments: "))

    assignment_weights = []
    assignment_scores = []

    # Input the assignment weights and scores
    for i in range(num_assignments):
        weight = float(input(f"Enter the weight (percentage) for Assignment {i+1}: "))
        while weight > 100 or sum(assignment_weights) + weight > 100:
            print("Invalid weight! Total weight cannot exceed 100 or each score cannot exceed 100.")
            weight = float(input(f"Enter the weight (percentage) for Assignment {i+1}: "))

        score = float(input(f"Enter the score (percentage) for Assignment {i+1}: "))
        while score > 100:
            print("Invalid score! Each score cannot exceed 100.")
            score = float(input(f"Enter the score (percentage) for Assignment {i+1}: "))

        assignment_weights.append(weight)
        assignment_scores.append(score)

    # Calculate the weighted average
    total_weighted_score = 0
    total_weight = sum(assignment_weights)

    for weight, score in zip(assignment_weights, assignment_scores):
        total_weighted_score += (weight * score) / 100

    # Calculate the course grade
    course_grade = (total_weighted_score / total_weight) * 100

    return course_grade


# Call the function to calculate the course grade
grade = calculate_course_grade()

# Display the result
print(f"\nThe course grade is: {grade}%")

# Apply the grading scale
if grade >= 80:
    print("Grade: HD - High Distinction")
elif grade >= 70:
    print("Grade: DI - Distinction")
elif grade >= 60:
    print("Grade: CR - Credit")
elif grade >= 50:
    print("Grade: PA - Pass")
else:
    print("Grade: NN - Fail")
