# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores.
# Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    new_arr = list(set(arr))
    lista_decrescente = sorted(new_arr, reverse = True)
    
    print(lista_decrescente[1])