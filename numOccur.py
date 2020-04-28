def find_k(a, b, k):
    num = 0
    for i in range(a,b+1):
        num += str(i).count(str(k))
        print(i)
    return num
k = 2
a = 212
b = 250

print("The number of digit %d from %d to %d is: \t\t %d" %(k,a,b,find_k(a,b,k)))