class lorenz():
    def __init__(x0, y0z, z0, * , s=10, r=28, b=2.667):
        pass
    
    def lorenz_equation():
        x, y, z = xyz
        x_dot = s*(y - x)
        y_dot = r*x - y - x*z
        z_dot = x*y - b*z
        return np.array([x_dot, y_dot, z_dot])

    def integrate():
        pass