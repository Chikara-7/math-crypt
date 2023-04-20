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
print("Enter Base")
Base = int(input())
print("Enter Exponent")
Exponent = int(input())
print("Enter Modulo")
Modulo = int(input())

print(power(Base, Exponent, Modulo))

exit = input("press Enter to close")