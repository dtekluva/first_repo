import math

def top_left(b, a, c):

    q = math.sqrt((b**2)-4*a*c)

    return q

def get_x1(b, q, a):
    m = ((-1 * b) + q)/(2*a)
    return m

def get_x2(b, q, a):
    m = ((-1 * b) -  q)/(2*a)
    return m

def quadratic_solve(a,b,c):
    top_left_value = top_left(b, a, c)

    x1 = get_x1(b, top_left_value, a)
    print(x1)
    x2 = get_x2(b, top_left_value, a)
    print(x2)

    print(x1, x2)
quadratic_solve(2,-5,-3)