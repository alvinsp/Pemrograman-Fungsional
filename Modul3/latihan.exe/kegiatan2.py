def konversi_waktu(minggu):
    def konversi_hari(hari):
        def konversi_jam(jam):
            def konversi_menit(menit):
                return (minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit
            return konversi_menit
        return konversi_jam
    return konversi_hari

def is_integer(char):
    return char.isdigit()

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

data_integer = [list(filter(is_integer, item.split())) for item in data]

print()
print("[=== HASIL INTEGER ===]")
print()
# Menampilkan data masukan dan hasil konversi ke menit
for i in range(len(data)):
    print("Data inputan:", data[i])
    print("Data yang filter:", data_integer[i])
    print()

