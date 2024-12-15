def calculate_homework(homework_assignment_arg):
    sum = 0
    for i in homework_assignment_arg.values():
        sum += i
    final = round(sum / len(homework_assignment_arg),2)
    print(final)
