
def mergeLogic(l1, l2):
    i1 =0
    i2 =0
    l = []
    n = len(l1) + len(l2)

    for ctr in range(n):

        # added as a afterthought after seeing error
        if i1 == len(l1):
            l = l + l2[i2:]
            break
        if i2 == len(l2):
            l = l + l1[i1:]
            break

        # writen in frst iteration
        if l1[i1] < l2[i2]:
            l.append(l1[i1])
            i1 += 1
        else :
            l.append(l2[i2])
            i2 += 1

    return l

def mergeSort(l):
    mid =  int(len(l) / 2)
    l_left = l[:mid]
    l_right = l[mid:]

    if len(l_left) > 1:
        x_l = mergeSort(l_left)
    else:
        x_l = l_left

    if len(l_right) > 1:
        x_r = mergeSort(l_right)
    else:
        x_r = l_right

    return mergeLogic(x_l, x_r)

if __name__ == '__main__':
    x = mergeSort([5,2,1,3,7,4])
    print(x)