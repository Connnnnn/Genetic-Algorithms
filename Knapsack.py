# All items i have a weight wi and a value vi

def knapSack(knapSize, wt, val, numItems):
    K = [[0 for x in range(knapSize + 1)] for x in range(numItems + 1)]

    for i in range(numItems + 1):
        for weight in range(knapSize + 1):
            if i == 0 or weight == 0:
                K[i][weight] = 0
            elif wt[i - 1] <= weight:
                K[i][weight] = max(val[i - 1] + K[i - 1][weight - wt[i - 1]], K[i - 1][weight])
            else:
                K[i][weight] = K[i - 1][weight]
    return K[numItems][knapSize]


if __name__ == '__main__':

    vi = [78, 35, 89, 36, 94, 75, 74, 79, 80, 16]
    wi = [18, 9, 23, 20, 59, 61, 70, 75, 76, 30]
    knapCapacity = 103
    lenItems = len(vi)

    print(knapSack(knapCapacity, wi, vi, lenItems))
