def count_possible_triangles(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):

                if arr[i] + arr[j] > arr[k] and arr[i] + arr[k] > arr[j] and arr[j] + arr[k] > arr[i]:
                    count += 1
    return count

arr = [4, 6, 3, 7]
print("Кількість можливих трикутників:", count_possible_triangles(arr))
