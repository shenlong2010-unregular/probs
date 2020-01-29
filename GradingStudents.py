def gradingStudents(grades):
    lst = []
    for i in grades:
        # grade < 38 will failed
        if i < 38:
            lst.append(i)
        # grade > 38
        else:
            # total <= 2
            if (i - round(i / 5) * 5) < 2:
                lst.append(round(i / 5) * 5)

            # when total >= 3
            else:
                lst.append(i)
    return lst
result = gradingStudents([73, 67, 38, 33, 84])
print("\n".join(map(str, result)))