import sympy as sp

x_s, y_s = sp.symbols("x y")

def my_func(x, y):
    return (x - 3) ** 2 + (y + 1) ** 2

expr = my_func(x_s, y_s)
df_dx = sp.diff(expr, x_s)
df_dy = sp.diff(expr, y_s)
print("∂f/∂x =", sp.expand(df_dx))
print("∂f/∂y =", sp.expand(df_dy))

grad_fn = sp.lambdify((x_s, y_s), (df_dx, df_dy))
print(grad_fn(0, 0))
print(grad_fn(0.6, -0.2))