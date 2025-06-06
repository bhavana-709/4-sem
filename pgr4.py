
import timeit
import random
import matplotlib.pyplot as plt
def Input(Array, n):
    for i in range(0, n):
        ele = random.randrange(1, 50)
        Array.append(ele)
def selectionSort(Array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if Array[j] < Array[min_index]:
                min_index = j
        (Array[ind]), Array[min_index] = (Array[min_index], Array[ind])
N = []
CPU = []
trail = int(input("Enter no. of trails: "))
for t in range(0, trail):
    Array = []
    print("-----> TRAIL NO:", t + 1)
    n = int(input("Enter number of elements: "))
    Input(Array, n)
    start = timeit.default_timer()
    selectionSort(Array, n)
    times = timeit.default_timer() - start
    print("Sorted Array:")
    print(Array)
    N.append(n)
    CPU.append(round (float(times)* 1000000, 2))
print("N CPU")
for t in range(0, trail):
    print(N[t], CPU[t])
plt.plot(N, CPU)
plt.scatter(N, CPU, color="red", marker="*", s=50)
plt.xlabel('Array Size-N')
plt.ylabel('CPU Processing Time')
plt.title('Selection Sort Time efficiency')
plt.show()

