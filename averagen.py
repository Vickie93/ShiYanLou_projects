N = 10
sum = 0
count = 0
print("Please input 10 numbers: ")
while count < N:
    numner = float(input())
    sum = sum + numner
    count = count + 1
average = sum / N
print("N = {}, Sum = {}".format(N, sum))
print("Average = {:.2f}".format(average))
