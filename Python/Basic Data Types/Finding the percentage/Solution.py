if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_list = student_marks[query_name]
    #print(query_list)
    print('%0.2f' % (sum(query_list)/3))
    
