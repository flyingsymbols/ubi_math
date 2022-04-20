import sympy

def main():
    # print(ubi_recurrance(10, 6))
    # print(ubi_iterate(10, 6))
    # print(ubi_iterate(60*60*24, 1))
    # print(ubi_iterate(10*60*24, 6))
    # print(ubi_iterate(60*24, 60))
    print(sum_exp(-0.1, 10, 1))
    print(sum_exp(-0.1, 10, 5))
    print(sum_exp(-0.1, 10, 25))
    print(sum_exp(-0.1, 10, 100))
    print(sum_exp(-0.1, 10, 1000))
    print(sum_exp(-0.1, 10, 10000))
    print(sum_exp(-0.1, 20, 20000))

RATE = -sympy.ln(360)/6983776800

def ubi_recurrance(n, time_step):
    print(n, time_step)
    if n == 0:
        return 0
    else:
        return (time_step + ubi_recurrance(n-1, time_step) * sympy.exp(RATE*time_step)).evalf(60)

def ubi_iterate(n, time_step):
    res = 0
    for i in range(n):
        res = (time_step + res * sympy.exp(RATE*time_step)).evalf(60)
    return res

def sum_exp(r, T, n):
    res = 0
    rate = sympy.sympify(T)/n
    for i in range(n):
        res = res + sympy.exp(i*r*rate).evalf(60)
    return res*rate

if __name__ == '__main__':
    main()
