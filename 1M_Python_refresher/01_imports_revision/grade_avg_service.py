def calcualte_homework(homework_arg):
    sum_of_grade=0
    for homework in homework_arg.values():
        sum_of_grade=sum_of_grade +homework
        final_grade= round(sum_of_grade/len(homework_arg),2)

    print(final_grade)
