# Given the names and grades for each student in a class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    
    alunos = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        alunos.append([name, score])
           
    segunda_menor_nota = sorted(set(score for name, score in alunos))[1]
    alunos_segunda_menor_nota = sorted(name for name, score in alunos if score == segunda_menor_nota)
    
    for name in alunos_segunda_menor_nota:
        print(name)