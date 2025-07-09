
# Dustin Dunbar
# July 5, 2025
# P4HW1
# Calculates Average grade numerical and alphabet output. 


# Prompts user to enter the number of scores they wish to enter.
num_scores = int(input('How many scores do you want to enter? '))
print()

# Creates an empty list to store the scores.
scores_list = []

# Collecting the entered scores with a loop.
for scores in range(num_scores):
    score = float(input('Enter Score #' + str(scores + 1) + ': '))

    # only entered integer thats between 0 to 100.
    while score < 0 or score > 100:
        print()
        print('INVALID Score entered!!!! \nScore should be between 0 and 100')
        score = float(input('Enter Score #' + str(scores + 1) + ' again: '))
        
    # Enters the valid entered scores to the list    
    scores_list.append(score)

# Calculates the lowest entered score and stores it into a variable.
lowest_score = min(scores_list)

# Removes the lowest score from the modified list.
scores_list.remove(lowest_score)

# Calculates the average of the entered scores.
average_score = sum(scores_list) / len(scores_list)

# Determines the letter grade for the average score.
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display the results
print('\n')
print('--------------Results-----------')
print(f'Lowest score  : {lowest_score}') # Lowest score entered.
print(f'Modified List : {scores_list}') # Score List after dropping lowest score.
print(f'Scores Average: {average_score:.2f}') # The average of scores in modified list.
print(f'Grade         : {grade}') # Determine the letter grade for the calculated average.
print('----------------------------------')
