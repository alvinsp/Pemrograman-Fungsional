def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    # Inner function untuk menghitung gradien (m)
    def calculate_slope():
        return (y2 - y1) / (x2 - x1)
    
    # Closure untuk mendapatkan nilai M
    M = calculate_slope()
    
    # Rumus untuk mendapatkan nilai C
    def calculate_intercept():
        return y1 - M * x1
    
    # Mendapatkan nilai C melalui closure
    C = calculate_intercept()
    
    return f"y = {M:.2f}x + {C:.2f}"

# Points A and B
A = point(1, 2)
B = point(2, 3)

equation_AB = line_equation_of(A, B)

# Display the result
print("Persamaan garis yang melalui A and B:")
print(equation_AB)
