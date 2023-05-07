print('#1 P(x^3) = x^3 + x + 1')
print('#2 P(x^3) = x^3 + x^2 + 1')
print('#3 P(x^4) = x^4 + x^3 + 1')
print('#4 P(x^5) = x^5 + x + 1')
print('#5 P(x^5) = x^5 + x^2 + 1')
print('')
field_elements = []
invers_elemets = []
n = int(input('Выберите вариант: '))
if n == 1:
    field_elements = [0, 2, 4, 3, 6, 7, 5, 1]
    invers_elemets = [0, 6, 5, 4, 3, 2, 1, 7]
elif n == 2:
    field_elements = [0, 2, 4, 3, 6, 7, 5, 1]
    invers_elemets = [0, 6, 5, 4, 3, 2, 1, 7]
elif n == 3:
    field_elements = [0, 2, 4, 8, 3, 6, 12, 11, 5, 10, 7, 14, 15, 13, 9, 1]
    invers_elemets = [0, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15]
elif n == 4:
    field_elements = [0, 2, 4, 8, 16, 3, 6, 12, 24, 19, 11, 22, 15, 30, 29, 27, 23, 7, 14, 28, 25, 17, 9, 18, 13, 26,
                      21, 5, 10, 20, 31, 1]
    invers_elemets = [0, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6,
                      5, 4, 3, 2, 1, 31]
elif n == 5:
    field_elements = [0, 2, 4, 8, 16, 3, 6, 12, 24, 19, 11, 22, 15, 30, 29, 27, 23, 7, 14, 28, 25, 17, 9, 18, 13, 26,
                      21, 5, 10, 20, 31, 1]
    invers_elemets = [0, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6,
                      5, 4, 3, 2, 1, 31]


for i in range(1, len(field_elements)):
    print('α^' + str(i) + ' = ' + str(bin(field_elements[i])) + ' = ' + str(field_elements[i]))
print('')

for i in range(1, len(invers_elemets)):
    print('α^-' + str(i) + ' = α^' + str(invers_elemets[i]))
print('')

K = []
K_list = str(input('Введите ключи через пробелы: '))
for k in K_list.split():
    K.append(bin(int(k)))
print('K =', K)

Px1 = int(input('Введите Px1: '))
Px0 = int(input('Введите Px0: '))
S_list = [bin(Px0)]

for i in range(1, len(invers_elemets)):
    S = invers_elemets[i] + field_elements.index(Px1)
    if S > (len(field_elements) - 1):
        S = S - (len(field_elements) - 1)
    S = bin(field_elements[S] ^ Px0)
    S_list.append(S)

for i in range(len(S_list)):
    print('S(α^' + str(i) + ') = ' + str(S_list[i]))
print('')

for i in range(len(S_list)):
    print('S^-1 (' + str(S_list[i]) + ') = α^' + str(i) + ' = ' + bin(field_elements[i]))
print('')

C1 = int(input('Введите С1: '))
C2 = int(input('Введите С2: '))

text = str(input('Введите ваш текст: ').upper())
P_words = list(text)
P = []
alphabet = [0, 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
P_temp = [alphabet.index(letter) for letter in P_words]
for i in P_temp:
    P.append(bin(i))
print('P =', P_words, '=', P_temp, '=', P)
print('')

print('C[ ] = верх низ')
print('C[2] =', bin(field_elements[1]), bin(0))
print('C[4] =', bin(field_elements[2]), bin(0))
print('C[6] =', bin(field_elements[5]), bin(0))
print('')


W0 = []
W1 = []
W2 = []
W3 = []
W4 = []
W5 = []
W6 = []

# W0
W0.append(K[0])
W0.append(K[1])

# W1
W1.append(K[2])
W1.append(K[3])

# W2
W2.append(bin(int(W0[0], 2) ^ int(S_list[field_elements.index(int(W1[1], 2))], 2) ^ field_elements[1]))
W2.append(bin(int(W0[1], 2) ^ int(S_list[field_elements.index(int(W1[0], 2))], 2) ^ field_elements[0]))

# W3
W3.append(bin(int(W1[0], 2) ^ int(W2[0], 2)))
W3.append(bin(int(W1[1], 2) ^ int(W2[1], 2)))

# W4
W4.append(bin(int(W2[0], 2) ^ int(S_list[field_elements.index(int(W3[1], 2))], 2) ^ field_elements[2]))
W4.append(bin(int(W2[1], 2) ^ int(S_list[field_elements.index(int(W3[0], 2))], 2) ^ field_elements[0]))

# W5
W5.append(bin(int(W3[0], 2) ^ int(W4[0], 2)))
W5.append(bin(int(W3[1], 2) ^ int(W4[1], 2)))

# W6
W6.append(bin(int(W4[0], 2) ^ int(S_list[field_elements.index(int(W5[1], 2))], 2) ^ field_elements[5]))
W6.append(bin(int(W4[1], 2) ^ int(S_list[field_elements.index(int(W5[0], 2))], 2) ^ field_elements[0]))

print('W[ ] = верх низ')
print('W[0] = Key[0] =', W0[0], '\n\t\t\t   ', W0[1])
print('')
print('W[1] = Key[1] =', W1[0], '\n\t\t\t   ', W1[1])
print('')
print('W[2] = W[0] + SB(R(W[1])) + C[2] =', bin(int(W0[0], 2)), '+', bin(int(S_list[field_elements.index(int(W1[1], 2))], 2)), '+', bin(field_elements[1]), '=', W2[0])
print('                                  ', bin(int(W0[1], 2)), '+', bin(int(S_list[field_elements.index(int(W1[0], 2))], 2)), '+', bin(field_elements[0]), '=', W2[1])
print('')
print('W[3] = W[1] + W[2] =', bin(int(W1[0], 2)), '+', bin(int(W2[0], 2)), '=', W3[0])
print('                    ', bin(int(W1[1], 2)), '+', bin(int(W2[1], 2)), '=', W3[1])
print('')
print('W[4] = W[2] + SB(R(W[3])) + C[4] =', bin(int(W2[0], 2)), '+', bin(int(S_list[field_elements.index(int(W3[1], 2))], 2)), '+', bin(field_elements[2]), '=', W4[0])
print('                                  ', bin(int(W2[1], 2)), '+', bin(int(S_list[field_elements.index(int(W3[0], 2))], 2)), '+', bin(field_elements[0]), '=', W4[1])
print('')
print('W[5] = W[3] + W[4] =', bin(int(W3[0], 2)), '+', bin(int(W4[0], 2)), '=', W5[0])
print('                    ', bin(int(W3[1], 2)), '+', bin(int(W4[1], 2)), '=', W5[1])
print('')
print('W[6] = W[4] + SB(R(W[5])) + C[6] =', bin(int(W4[0], 2)), '+', bin(int(S_list[field_elements.index(int(W5[1], 2))], 2)), '+', bin(field_elements[5]), '=', W6[0])
print('                                  ', bin(int(W4[1], 2)), '+', bin(int(S_list[field_elements.index(int(W5[0], 2))], 2)), '+', bin(field_elements[0]), '=', W6[1])
print('')

X = []
tmp = [0, 0]
X_tmp = []
print('1. шифрование\n2. расшифровка')
k = int(input('Выберите: '))
if k == 1:
    X.append(bin(int(P[0], 2) ^ int(W0[0], 2)))
    X.append(bin(int(P[1], 2) ^ int(W0[1], 2)))
    X.append(bin(int(P[2], 2) ^ int(W1[0], 2)))
    X.append(bin(int(P[3], 2) ^ int(W1[1], 2)))
    print('Шифрование')
    print('0) X = (', P[0], P[2], ') ⨁ (', W0[0], W1[0], ') = (', X[0], X[2], ')')
    print('       (', P[1], P[3], ') ⨁ (', W0[1], W1[1], ') = (', X[1], X[3], ')')
    print('')

    print('1.1) SubBytes')
    print('X = S(', X[0], ') S(', X[2], ') = (', S_list[field_elements.index(int(X[0], 2))], S_list[field_elements.index(int(X[2], 2))], ')')
    print('    S(', X[1], ') S(', X[3], ') = (', S_list[field_elements.index(int(X[1], 2))], S_list[field_elements.index(int(X[3], 2))], ')')
    X[0] = S_list[field_elements.index(int(X[0], 2))]
    X[1] = S_list[field_elements.index(int(X[1], 2))]
    X[2] = S_list[field_elements.index(int(X[2], 2))]
    X[3] = S_list[field_elements.index(int(X[3], 2))]
    print('')

    print('1.2) ShiftRow')
    print('X = (', X[0], X[2], ') -> (', X[0], X[2], ')')
    print('    (', X[1], X[3], ') -> (', X[3], X[1], ')')
    X[1], X[3] = X[3], X[1]
    print('')

    print('1.3) MixColumn\n(x) =', bin(C1), '* x +', bin(C2))
    print('(y0) = (', bin(C1), bin(C2), ') * (X[0])')
    print('(y1) = (', bin(C2), bin(C1), ') * (X[1])')
    # X[0]
    tmp[0] = field_elements.index(C1) + field_elements.index(int(X[0], 2))
    if tmp[0] > (len(field_elements) - 1):
        tmp[0] = tmp[0] - (len(field_elements) - 1)
    tmp[1] = field_elements.index(C2) + field_elements.index(int(X[1], 2))
    if tmp[1] > (len(field_elements) - 1):
        tmp[1] = tmp[1] - (len(field_elements) - 1)
    X_tmp.append(bin(field_elements[tmp[0]] ^ field_elements[tmp[1]]))

    print('(', bin(C1), '*', X[0], '+', bin(C2), '*', X[1], ') = ( α^' + str(field_elements.index(C1)), "* α^" + str(field_elements.index(int(X[0], 2))), '+ α^' + str(field_elements.index(C2)), '* α^' + str(field_elements.index(int(X[1], 2))), ') =')
    print('(', bin(C2), '*', X[0], '+', bin(C1), '*', X[1], ') = ( α^' + str(field_elements.index(C2)), "* α^" + str(field_elements.index(int(X[0], 2))), '+ α^' + str(field_elements.index(C1)), '* α^' + str(field_elements.index(int(X[1], 2))), ') =')
    print('\t = (α^' + str(tmp[0]), '+ α^' + str(tmp[1]), ') = (', bin(field_elements[tmp[0]]), '+',
          bin(field_elements[tmp[1]]), ') = (', X_tmp[0], ')')

    # X[1]
    tmp[0] = field_elements.index(C2) + field_elements.index(int(X[0], 2))
    if tmp[0] > (len(field_elements) - 1):
        tmp[0] = tmp[0] - (len(field_elements) - 1)
    tmp[1] = field_elements.index(C1) + field_elements.index(int(X[1], 2))
    if tmp[1] > (len(field_elements) - 1):
        tmp[1] = tmp[1] - (len(field_elements) - 1)
    X_tmp.append(bin(field_elements[tmp[0]] ^ field_elements[tmp[1]]))
    print('\t = (α^' + str(tmp[0]), '+ α^' + str(tmp[1]), ') = (', bin(field_elements[tmp[0]]), '+', bin(field_elements[tmp[1]]), ') = (', X_tmp[1], ')')
    tmp = [0, 0]
    print('')

    # X[2]
    tmp[0] = field_elements.index(C1) + field_elements.index(int(X[2], 2))
    if tmp[0] > (len(field_elements) - 1):
        tmp[0] = tmp[0] - (len(field_elements) - 1)
    tmp[1] = field_elements.index(C2) + field_elements.index(int(X[3], 2))
    if tmp[1] > (len(field_elements) - 1):
        tmp[1] = tmp[1] - (len(field_elements) - 1)
    X_tmp.append(bin(field_elements[tmp[0]] ^ field_elements[tmp[1]]))
    print('(', bin(C1), '*', X[2], '+', bin(C2), '*', X[3], ') = ( α^' + str(field_elements.index(C1)), "* α^" + str(field_elements.index(int(X[2], 2))), '+ α^' + str(field_elements.index(C2)), '* α^' + str(field_elements.index(int(X[3], 2))), ') =')
    print('(', bin(C2), '*', X[2], '+', bin(C1), '*', X[3], ') = ( α^' + str(field_elements.index(C2)), "* α^" + str(field_elements.index(int(X[2], 2))), '+ α^' + str(field_elements.index(C1)), '* α^' + str(field_elements.index(int(X[3], 2))), ') =')
    print('\t = (α^' + str(tmp[0]), '+ α^' + str(tmp[1]), ') = (', bin(field_elements[tmp[0]]), '+',
          bin(field_elements[tmp[1]]), ') = (', X_tmp[2], ')')
    tmp = [0, 0]

    # X[3]
    tmp[0] = field_elements.index(C2) + field_elements.index(int(X[2], 2))
    if tmp[0] > (len(field_elements) - 1):
        tmp[0] = tmp[0] - (len(field_elements) - 1)
    tmp[1] = field_elements.index(C1) + field_elements.index(int(X[3], 2))
    if tmp[1] > (len(field_elements) - 1):
        tmp[1] = tmp[1] - (len(field_elements) - 1)
    X_tmp.append(bin(field_elements[tmp[0]] ^ field_elements[tmp[1]]))
    print('\t = (α^' + str(tmp[0]), '+ α^' + str(tmp[1]), ') = (', bin(field_elements[tmp[0]]), '+', bin(field_elements[tmp[1]]), ') = (', X_tmp[3], ')')
    tmp = [0, 0]
    print('')
    print('X = (', X[0], X[2], ') -> (', X_tmp[0], X_tmp[2], ')')
    print('    (', X[1], X[3], ') -> (', X_tmp[1], X_tmp[3], ')')
    for i in range(len(X)):
        X[i] = X_tmp[i]
    print('')

    print('1.4) AddRoundKey\nX -> X ⨁ [W[2];W[3]]')
    print('X = (', X[0], X[2], ') ⨁ (', W2[0], W3[0], ') = (', (bin(int(X[0], 2) ^ int(W2[0], 2))), (bin(int(X[2], 2) ^ int(W3[0], 2))), ')')
    print('    (', X[1], X[3], ') ⨁ (', W2[1], W3[1], ') = (', (bin(int(X[1], 2) ^ int(W2[1], 2))), (bin(int(X[3], 2) ^ int(W3[1], 2))), ')')
    X[0] = (bin(int(X[0], 2) ^ int(W2[0], 2)))
    X[1] = (bin(int(X[1], 2) ^ int(W2[1], 2)))
    X[2] = (bin(int(X[2], 2) ^ int(W3[0], 2)))
    X[3] = (bin(int(X[3], 2) ^ int(W3[1], 2)))
    print('')

    print('2.1) SubBytes')
    print('X = ( S(', X[0], ') S(', X[2], ') ) = ( ', S_list[field_elements.index(int(X[0], 2))], S_list[field_elements.index(int(X[2], 2))], ')')
    print('    ( S(', X[1], ') S(', X[3], ') ) = ( ', S_list[field_elements.index(int(X[1], 2))], S_list[field_elements.index(int(X[3], 2))], ')')
    X[0] = S_list[field_elements.index(int(X[0], 2))]
    X[1] = S_list[field_elements.index(int(X[1], 2))]
    X[2] = S_list[field_elements.index(int(X[2], 2))]
    X[3] = S_list[field_elements.index(int(X[3], 2))]
    print('')

    print('2.2) ShiftRow')
    print('X = (', X[0], X[2], ') -> (', X[0], X[2], ')')
    print('    (', X[1], X[3], ') -> (', X[3], X[1], ')')
    X[1], X[3] = X[3], X[1]
    print('')

    print('2.3) AddRoundKey\nX -> X ⨁ [W[4];W[5]]')
    print('X = (', X[0], X[2], ') ⨁ (', W4[0], W5[0], ') = (', (bin(int(X[0], 2) ^ int(W4[0], 2))),
          (bin(int(X[2], 2) ^ int(W5[0], 2))), ')')
    print('    (', X[1], X[3], ') ⨁ (', W4[1], W5[1], ') = (', (bin(int(X[1], 2) ^ int(W4[1], 2))),
          (bin(int(X[3], 2) ^ int(W5[1], 2))), ')')
    X[0] = (bin(int(X[0], 2) ^ int(W4[0], 2)))
    X[1] = (bin(int(X[1], 2) ^ int(W4[1], 2)))
    X[2] = (bin(int(X[2], 2) ^ int(W5[0], 2)))
    X[3] = (bin(int(X[3], 2) ^ int(W5[1], 2)))
    print('')

    encrypted_text_num = []
    encrypted_text = []
    for i in range(len(X)):
        encrypted_text_num.append(int(X[i], 2))

    for i in range(len(encrypted_text_num)):
        encrypted_text.append(alphabet[encrypted_text_num[i]])

    print('Зашифрованный текст: C =', X, '=', encrypted_text_num, '=', encrypted_text)
    print('')

elif k == 2:
    print('Расшифрование')
    X.append(bin(int(P[0], 2) ^ int(W4[0], 2)))
    X.append(bin(int(P[1], 2) ^ int(W4[1], 2)))
    X.append(bin(int(P[2], 2) ^ int(W5[0], 2)))
    X.append(bin(int(P[3], 2) ^ int(W5[1], 2)))
    print('0) X = (', P[0], P[2], ') ⨁ (', W4[0], W5[0], ') = (', X[0], X[2], ')')
    print('       (', P[1], P[3], ') ⨁ (', W4[1], W5[1], ') = (', X[1], X[3], ')')
    print('')

    print('1.1) ShiftRow')
    print('X = (', X[0], X[2], ') -> (', X[0], X[2], ')')
    print('    (', X[1], X[3], ') -> (', X[3], X[1], ')')
    X[1], X[3] = X[3], X[1]
    print('')

    print('1.2) SubBytes')
    print('X = (', X[0], X[2], ') -> ( S^-1(', X[0], ') S^-1(', X[2], ') )', '= (', bin(field_elements[S_list.index(X[0])]), bin(field_elements[S_list.index(X[2])]), ')')
    print('    (', X[1], X[3], ') -> ( S^-1(', X[1], ') S^-1(', X[3], ') )', '= (', bin(field_elements[S_list.index(X[1])]), bin(field_elements[S_list.index(X[3])]), ')')
    X[0] = (bin(field_elements[S_list.index(X[0])]))
    X[1] = (bin(field_elements[S_list.index(X[1])]))
    X[2] = (bin(field_elements[S_list.index(X[2])]))
    X[3] = (bin(field_elements[S_list.index(X[3])]))
    print('')

    print('1.3) AddRoundKey\nX -> X ⨁ [W[2];W[3]]')
    print('X = (', X[0], X[2], ') ⨁ (', W2[0], W3[0], ') = (', (bin(int(X[0], 2) ^ int(W2[0], 2))),
          (bin(int(X[2], 2) ^ int(W3[0], 2))), ')')
    print('    (', X[1], X[3], ') ⨁ (', W2[1], W3[1], ') = (', (bin(int(X[1], 2) ^ int(W2[1], 2))),
          (bin(int(X[3], 2) ^ int(W3[1], 2))), ')')
    X[0] = (bin(int(X[0], 2) ^ int(W2[0], 2)))
    X[1] = (bin(int(X[1], 2) ^ int(W2[1], 2)))
    X[2] = (bin(int(X[2], 2) ^ int(W3[0], 2)))
    X[3] = (bin(int(X[3], 2) ^ int(W3[1], 2)))
    print('')

    print('1.4) MixColumn')

    print('M = (', bin(C1), bin(C2), ') = ( α^' + str(field_elements.index(C1)), 'α^' + str(field_elements.index(C2)), ')')
    print('    (', bin(C2), bin(C1), ') = ( α^' + str(field_elements.index(C2)), 'α^' + str(field_elements.index(C1)), ')')
    z = field_elements.index(C1) * 2
    if z > (len(field_elements) - 1):
        z = z - (len(field_elements) - 1)
    q = field_elements.index(C2) * 2
    if q > (len(field_elements) - 1):
        q = q - (len(field_elements) - 1)
    sss = field_elements.index(int(bin(field_elements[z] ^ field_elements[q]), 2))
    print('\u25B3 = α^' + str(z), '+ α^' + str(q), '=', bin(field_elements[z]), '+', bin(field_elements[q]), '=', bin(field_elements[z] ^ field_elements[q]), '= α^' + str(sss))
    print('')

    M_invers = []
    print('M^-1 = ( (α^' + str(field_elements.index(C1)), '/ α^' + str(sss), ') ( α^' + str(field_elements.index(C2)), '/ (α^' + str(sss), ') ) =')
    print('M^-1 = ( (α^' + str(field_elements.index(C2)), '/ α^' + str(sss), ') ( α^' + str(field_elements.index(C1)), '/ (α^' + str(sss), ') ) =')
    print('\t= ( (α^' + str(field_elements.index(C1)) + ' * α^' + str(invers_elemets.index(sss)), ') ( α^' + str(field_elements.index(C2)) + ' * α^' + str(invers_elemets.index(sss)), ') ) =')
    print('\t= ( (α^' + str(field_elements.index(C2)) + ' * α^' + str(invers_elemets.index(sss)), ') ( α^' + str(field_elements.index(C1)) + ' * α^' + str(invers_elemets.index(sss)), ') ) =' )
    tmp[0] = field_elements.index(C1) + invers_elemets.index(sss)
    if tmp[0] > (len(field_elements) - 1):
        tmp[0] = tmp[0] - (len(field_elements) - 1)
    tmp[1] = field_elements.index(C2) + invers_elemets.index(sss)
    if tmp[1] > (len(field_elements) - 1):
        tmp[1] = tmp[1] - (len(field_elements) - 1)
    print('\t= ( α^' + str(field_elements.index(C1) + invers_elemets.index(sss)), 'α^' + str(field_elements.index(C2) + invers_elemets.index(sss)), ') = ( α^' + str(int(tmp[0])), 'α^' + str(int(tmp[1])), ') =')
    print('\t= ( α^' + str(field_elements.index(C2) + invers_elemets.index(sss)), 'α^' + str(field_elements.index(C1) + invers_elemets.index(sss)), ') = ( α^'+ str(int(tmp[1])), 'α^' + str(int(tmp[0])), ') =')
    print('\t= (', bin(field_elements[int(tmp[0])]), bin(field_elements[int(tmp[1])]), ')')
    print('\t= (', bin(field_elements[int(tmp[1])]), bin(field_elements[int(tmp[0])]), ')')
    M_invers.append(bin(field_elements[int(tmp[0])]))
    M_invers.append(bin(field_elements[int(tmp[1])]))
    M_invers.append(bin(field_elements[int(tmp[1])]))
    M_invers.append(bin(field_elements[int(tmp[0])]))
    tmp = [0, 0]
    print('')
    print('(y0) = (', M_invers[0], M_invers[1], ') * (X[0])')
    print('(y1) = (', M_invers[2], M_invers[3], ') * (X[1])')
    print('')

    print('( (α^' + str(field_elements.index(int(M_invers[0], 2))) + ') (α^' + str(
        field_elements.index(int(M_invers[1], 2))) + ') ) * ( (α^' + str(field_elements.index(int(X[0], 2))) + ') ) =')
    print('( (α^' + str(field_elements.index(int(M_invers[2], 2))) + ') (α^' + str(
        field_elements.index(int(M_invers[3], 2))) + ') ) * ( (α^' + str(field_elements.index(int(X[1], 2))) + ') ) =')

    # X[0]
    tmp[0] = field_elements.index(int(M_invers[0], 2)) + field_elements.index(int(X[0], 2))
    if tmp[0] > (len(field_elements) - 1):
        tmp[0] = tmp[0] - (len(field_elements) - 1)
    tmp[1] = field_elements.index(int(M_invers[1], 2)) + field_elements.index(int(X[1], 2))
    if tmp[1] > (len(field_elements) - 1):
        tmp[1] = tmp[1] - (len(field_elements) - 1)
    X_tmp.append(bin(field_elements[tmp[0]] ^ field_elements[tmp[1]]))

    print('( α^' + str(field_elements.index(int(M_invers[0], 2))), "* α^" + str(field_elements.index(int(X[0], 2))), '+ α^' + str(field_elements.index(int(M_invers[1], 2))), '* α^' + str(field_elements.index(int(X[1], 2))), ') = (α^' + str(tmp[0]), '+ α^' + str(tmp[1]), ') = (', bin(field_elements[tmp[0]]), '+', bin(field_elements[tmp[1]]), ') = (', X_tmp[0], ')')

    # X[1]
    tmp[0] = field_elements.index(int(M_invers[1], 2)) + field_elements.index(int(X[0], 2))
    if tmp[0] > (len(field_elements) - 1):
        tmp[0] = tmp[0] - (len(field_elements) - 1)
    tmp[1] = field_elements.index(int(M_invers[0], 2)) + field_elements.index(int(X[1], 2))
    if tmp[1] > (len(field_elements) - 1):
        tmp[1] = tmp[1] - (len(field_elements) - 1)
    X_tmp.append(bin(field_elements[tmp[0]] ^ field_elements[tmp[1]]))
    print('( α^' + str(field_elements.index(int(M_invers[1], 2))), "* α^" + str(field_elements.index(int(X[0], 2))), '+ α^' + str(field_elements.index(int(M_invers[0], 2))), '* α^' + str(field_elements.index(int(X[1], 2))), ') = (α^' + str(tmp[0]), '+ α^' + str(tmp[1]), ') = (', bin(field_elements[tmp[0]]), '+', bin(field_elements[tmp[1]]), ') = (', X_tmp[1], ')')
    print('')

    print('( (α^' + str(field_elements.index(int(M_invers[0], 2))) + ') (α^' + str(
        field_elements.index(int(M_invers[1], 2))) + ') ) * ( (α^' + str(field_elements.index(int(X[2], 2))) + ') ) =')
    print('( (α^' + str(field_elements.index(int(M_invers[2], 2))) + ') (α^' + str(
        field_elements.index(int(M_invers[3], 2))) + ') ) * ( (α^' + str(field_elements.index(int(X[3], 2))) + ') ) =')

    # X[2]
    tmp[0] = field_elements.index(int(M_invers[3], 2)) + field_elements.index(int(X[2], 2))
    if tmp[0] > (len(field_elements) - 1):
        tmp[0] = tmp[0] - (len(field_elements) - 1)
    tmp[1] = field_elements.index(int(M_invers[2], 2)) + field_elements.index(int(X[3], 2))
    if tmp[1] > (len(field_elements) - 1):
        tmp[1] = tmp[1] - (len(field_elements) - 1)
    X_tmp.append(bin(field_elements[tmp[0]] ^ field_elements[tmp[1]]))
    print('( α^' + str(field_elements.index(int(M_invers[0], 2))), "* α^" + str(field_elements.index(int(X[2], 2))), '+ α^' + str(field_elements.index(int(M_invers[1], 2))), '* α^' + str(field_elements.index(int(X[3], 2))), ') = (α^' + str(tmp[0]), '+ α^' + str(tmp[1]), ') = (', bin(field_elements[tmp[0]]), '+', bin(field_elements[tmp[1]]), ') = (', X_tmp[2], ')')

    # X[3]
    tmp[0] = field_elements.index(int(M_invers[2], 2)) + field_elements.index(int(X[2], 2))
    if tmp[0] > (len(field_elements) - 1):
        tmp[0] = tmp[0] - (len(field_elements) - 1)
    tmp[1] = field_elements.index(int(M_invers[3], 2)) + field_elements.index(int(X[3], 2))
    if tmp[1] > (len(field_elements) - 1):
        tmp[1] = tmp[1] - (len(field_elements) - 1)
    X_tmp.append(bin(field_elements[tmp[0]] ^ field_elements[tmp[1]]))
    print('( α^' + str(field_elements.index(int(M_invers[1], 2))), "* α^" + str(field_elements.index(int(X[2], 2))), '+ α^' + str(field_elements.index(int(M_invers[0], 2))), '* α^' + str(field_elements.index(int(X[3], 2))), ') = (α^' + str(tmp[0]), '+ α^' + str(tmp[1]), ') = (', bin(field_elements[tmp[0]]), '+', bin(field_elements[tmp[1]]), ') = (', X_tmp[3], ')')
    print('')

    print('X = (', X[0], X[2], ') -> (', X_tmp[0], X_tmp[2], ')')
    print('    (', X[1], X[3], ') -> (', X_tmp[1], X_tmp[3], ')')
    for i in range(len(X)):
        X[i] = X_tmp[i]
    print('')

    print('2.1) ShiftRow')
    print('X = (', X[0], X[2], ') -> (', X[0], X[2], ')')
    print('    (', X[1], X[3], ') -> (', X[3], X[1], ')')
    X[1], X[3] = X[3], X[1]
    print('')

    print('2.2) SubBytes')
    print('X = (', X[0], X[2], ') -> ( S^-1(', X[0], ') S^-1(', X[2], ') )', '= (',
          bin(field_elements[S_list.index(X[0])]), bin(field_elements[S_list.index(X[2])]), ')')
    print('    (', X[1], X[3], ') -> ( S^-1(', X[1], ') S^-1(', X[3], ') )', '= (',
          bin(field_elements[S_list.index(X[1])]), bin(field_elements[S_list.index(X[3])]), ')')
    X[0] = (bin(field_elements[S_list.index(X[0])]))
    X[1] = (bin(field_elements[S_list.index(X[1])]))
    X[2] = (bin(field_elements[S_list.index(X[2])]))
    X[3] = (bin(field_elements[S_list.index(X[3])]))
    print('')

    print('2.3) AddRoundKey\nX -> X ⨁ [W[0];W[1]]')
    print('X = (', X[0], X[2], ') ⨁ (', W0[0], W1[0], ') = (', (bin(int(X[0], 2) ^ int(W0[0], 2))),
          (bin(int(X[2], 2) ^ int(W1[0], 2))), ')')
    print('    (', X[1], X[3], ') ⨁ (', W0[1], W1[1], ') = (', (bin(int(X[1], 2) ^ int(W0[1], 2))),
          (bin(int(X[3], 2) ^ int(W1[1], 2))), ')')
    X[0] = (bin(int(X[0], 2) ^ int(W0[0], 2)))
    X[1] = (bin(int(X[1], 2) ^ int(W0[1], 2)))
    X[2] = (bin(int(X[2], 2) ^ int(W1[0], 2)))
    X[3] = (bin(int(X[3], 2) ^ int(W1[1], 2)))
    print('')
    decrypted_text_num = []
    decrypted_text = []
    for i in range(len(X)):
        decrypted_text_num.append(int(X[i], 2))

    for i in range(len(decrypted_text_num)):
        decrypted_text.append(alphabet[decrypted_text_num[i]])

    print('Расшифрованный текст: C =', X, '=', decrypted_text_num, '=', decrypted_text)
