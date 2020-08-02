def multiplyString(num1,num2):
    res = 0
    carry1 = 1
    for n1 in num1[::-1]:
        carry2 = 1
        for n2 in num2[::-1]:
            res += int(n1) * int(n2) * carry1 * carry2
            carry2 *= 10
        carry1 *= 10
    return str(res)
multiplyString('123','456')