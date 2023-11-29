data_peserta = []

def inputData():
    print("Masukkan data peserta: ")
    peserta = {
        "id": int(input("ID: ")),
        "nama": input("Nama: "),
        "nilai": [float(x.strip()) for x in input("Nilai: ").split(",")],
    }
    data_peserta.append(peserta)

def editData(inputId):
    showNilaiAdmin(inputId)
    found = False
    for peserta in data_peserta:
        if peserta["id"] == inputId:
            new_nilai = [float(x.strip()) for x in input("Nilai yang ingin dirubah: ").split(",")]
            peserta["nilai"] = new_nilai
            found = True
            break
    if not found:
        print("ID yang Anda masukkan tidak ditemukan.")

def hitung_hasil_akhir(peserta):
    total_nilai = sum(peserta["nilai"])
    jumlah_nilai = len(peserta["nilai"])
    return (total_nilai / jumlah_nilai) 

def showNilaiAdmin(inputId):
    found = False
    for peserta in data_peserta:
        if peserta["id"] == inputId:
            print("Data Peserta:")
            print("ID:", peserta["id"])
            print("Nama:", peserta["nama"])
            print("nilai:", peserta["nilai"])
            hasil_akhir = hitung_hasil_akhir(peserta)
            print("hasil_akhir:", hasil_akhir)
            found = True
            break
    if not found:
        print("ID yang Anda masukkan tidak ditemukan.")

        
def showNilai(inputId):
    found = False
    for peserta in data_peserta:
        if peserta["id"] == inputId:
            print("Data Peserta:")
            print("ID:", peserta["id"])
            print("Nama:", peserta["nama"])
            print("nilai:", peserta["nilai"])
            hasil_akhir = hitung_hasil_akhir(peserta)
            print("hasil_akhir:", hasil_akhir)
            if hasil_akhir >= 75:
                print("Selamat, anda lulus!")
            else:
                print("Maaf, anda tidak lulus. Silakan perbaiki nilai anda.")
            found = True
            break
    if not found:
        print("ID yang Anda masukkan tidak ditemukan.")

def main():
    while True:
        print("Masukkan apakah kamu seorang admin atau peserta:")
        user = input()
        if user == "admin":
            print("1. Input Data")
            print("2. Edit Data")
            pilih = int(input("Masukkan Pilihan: "))
            if pilih == 1:
                inputData()
            elif pilih == 2:
                inputId = int(input("Masukkan ID yang ingin diedit: "))
                editData(inputId)
            else:
                print("Salah input")
        elif user == "peserta":
            inputId = int(input("Masukkan ID Anda: "))
            showNilai(inputId)
        elif user == "exit":
            break
        else:
            print("Yang Anda masukkan salah.")

if __name__ == "__main__":
    main()
