import sympy as sp

x_s, y_s = sp.symbols("x y")

def f(x, y):
    return (x - 3) ** 2 + (y + 1) ** 2


def grad(x, y):
    return 2 * x - 6, 2 * y + 2


def step(lr, g, point):
    return tuple(p - lr * gi for p, gi in zip(point, g))


start = (0, 0)
new_point = step(0.1, grad(*start), start)
print(new_point, f(*new_point))


def gradient_descent(lr, steps=50, start=(0, 0)):
    point = start
    for i in range(steps):
        g = grad(*point)
        point = step(lr, g, point)
        print(f"step {i + 1:2d}: x = {point[0]:.4f}, y={point[1]:.4f}, f={f(*point):.4f}")
    return point


gradient_descent(1.1)


expr = f(x_s, y_s)
df_dx = sp.diff(expr, x_s)
df_dy = sp.diff(expr, y_s)
print("∂f/∂x =", sp.expand(df_dx))
print("∂f/∂y =", sp.expand(df_dy))

grad_fn = sp.lambdify((x_s, y_s), (df_dx, df_dy))
print(grad_fn(0, 0))
print(grad_fn(0.6, -0.2))