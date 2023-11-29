# Kegiatan 1

# Fungsi untuk penjumlahan
def plus(a, b):
    return a + b

# Fungsi untuk pengurangan


def minus(a, b):
    return a - b

# Fungsi untuk perkalian


def mult(a, b):
    return a * b

# Fungsi untuk pembagian


def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa melakukan pembagian oleh 0"


def tree(expression_tree):
    if isinstance(expression_tree, tuple):
        left, operation, right = expression_tree
        if operation == '+':
            return plus(tree(left), tree(right))
        elif operation == '-':
            return minus(tree(left), tree(right))
        elif operation == '*':
            return mult(tree(left), tree(right))
        elif operation == '/':
            return div(tree(left), tree(right))
    else:
        return expression_tree


# Contoh pohon ekspresi: ((2, '+', 3), '*', (5, '-', 1))
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi:", result, "\n")

# =======================================================================

# Kegiatan 2
random_list = [105, 3.1, "hello", 737, "python",
               2.7, "world", 412, 5.5, "AI", 50, 80, 20]

# Inisialisasi variabel untuk menyimpan nilai int, float, dan string
int_values = {}
float_values = ()
string_values = []

# Iterasi melalui random_list untuk memisahkan nilai
for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = (item // 100) % 10

        # Menyimpan dalam dictionary
        int_values[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float):
        # Menambahkan float ke dalam tuple
        float_values += (item,)
    elif isinstance(item, str):
        # Menambahkan string ke dalam list
        string_values.append(item)

# Menampilkan hasil pemisahan
print("Nilai Integer (dalam bentuk dictionary):")
print(int_values)
print("\nNilai Float (dalam bentuk tuple):")
print(float_values)
print("\nNilai String (dalam bentuk list):")
print(string_values, '\n')


# =======================================================================

# Kegiatan 3

# Fungsi untuk menghitung nilai akhir mahasiswa
def hitung_nilai_akhir(nilai_uts, nilai_uas):
    return (nilai_uts + nilai_uas) / 2

# Fungsi untuk menampilkan nilai akhir mahasiswa


def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print(f"Nama: {nama}\tNilai Akhir: {nilai_akhir:.2f}")


def main():
    data_mahasiswa = {
        "dafa": (85, 90),
        "pepeh": (78, 88),
        "noval": (92, 85),
    }

    # Menghitung nilai akhir semua mahasiswa
    data_nilai_akhir = {}
    for nama, (uts, uas) in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(uts, uas)
        data_nilai_akhir[nama] = nilai_akhir

    # Menampilkan nilai akhir mahasiswa
    tampilkan_nilai_akhir(data_nilai_akhir)


if __name__ == "__main__":
    main()
