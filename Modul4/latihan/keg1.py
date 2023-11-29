# curry function
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan
# panggil dengan hof
def panggil_hof():
    kali = perkalian(5)
    hasil = kali(6)
    print(hasil)

# manggil hof
panggil_hof()

# panggil dengan currying
print(perkalian(5)(6)) 



