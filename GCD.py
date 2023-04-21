print("Enter number of elements")
n = int(input())
a = [0]*n
for i in range(len(a)):
    i = str(i + 1)
    print("Element #" + i)
    i = int(i)
    i = i - 1
    a[i] = int(input())

def gcd(a, b):
        if (a == 0):
            return b
        return gcd(b % a, a)
  
def findGCD(a, n):
        result = a[0]
        for i in range(len(a)):
            result = gcd(a[i], result)
            if (result == 1):
                return 1
        return result 
print(findGCD(a, n))

exit = input("press Enter to close")