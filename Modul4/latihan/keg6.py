def point(x, y):
    return x, y

def line_equation_of(p1, M):
    x1, y1 = p1
    
    # TODO 1: Hitung nilai intercept (C)
    C = y1 - M * x1
    
    return f"y = {M:.2f}x + {C:.2f}"

# Contoh: Persamaan garis yang melalui titik (2, 2) dengan gradien 3
titik_1 = point(2, 2)
gradien = 3

hasil_persamaan = line_equation_of(titik_1, gradien)

# Tampilkan hasil
print("Persamaan garis yang melalui titik (2, 2) dengan gradien 3:")
print(hasil_persamaan)
