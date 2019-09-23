def bubbleSort(lst):
    global nth_recursion
    n_len_lst = len(lst)
    b_changes_made = False

    for i in range(n_len_lst - 1):
        if lst[i] < lst[i+1]:
            x = lst[i]
            lst[i] =  lst[i+1]
            lst[i+1] = x
            b_changes_made = True

    if b_changes_made:
        nth_recursion = nth_recursion + 1
        bubbleSort(lst)

    return lst

global nth_recursion
if __name__ == '__main__':
    
    nth_recursion = 1
    #l_input = ['p','y','t','h','o','n']
    l_input = [5,1,4,2,8]
    print(bubbleSort(l_input))
