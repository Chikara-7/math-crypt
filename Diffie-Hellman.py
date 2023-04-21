def power(Base, Exponent, Modulo):
        res = 1
        Base = Base % Modulo
        if (Base == 0):
            return 0
        while (Exponent > 0):
            if (Exponent & 1):
                res = (res * Base) % Modulo
            Exponent = Exponent >> 1
            Base = (Base * Base) % Modulo
        return res
print("Enter P: ")
P = int(input())
print("Enter G: ")
G = int(input())
print("Enter Key #1: ")
k1 = int(input())
print("Enter Key #2: ")
k2 = int(input())
x1 = power(G, k1, P)
x2 = power(G, k2, P)
y1 = power(x2, k1, P)
y2 = power(x1, k2, P)
print(y1, y2)
