
def search(inp, target):
    start = 0
    end = len(inp) - 1

    while(start <= end):
        mid = int((start + end) / 2)

        if target < inp[mid]:
            end = mid - 1
        elif target > inp[mid]:
            start = mid + 1
        else:
            return mid

    return -1


s = search([2,5,9,12,15,65,102], 65)
print(s)