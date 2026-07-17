n = 3
student_marks = {
    "ram": [20, 30, 40],
    "sita": [30, 40, 50],
    "gita": [40, 50, 60]}
'''def get_percentage(query_name):
    for _ in range(student_marks):
        if student_marks[i]== query_name:
            for i in range(n):
                for j in range(n):
                   Total_score = Total_score+student_marks[i][j]
                   percentage = Total_score/n
    return percentage'''
def get_percentage(query_name):
    if query_name in student_marks:
        scores = student_marks[query_name]
        print(scores)
        total_score = sum(scores)
        percentage = total_score / len(scores)
        return percentage
    else:
        return "Student not found"


query_name = input()
print(get_percentage(query_name))
'''for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    query_name = input()'''
