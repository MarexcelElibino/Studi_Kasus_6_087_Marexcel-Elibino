import json
path = r"C:\Users\Acer\OneDrive\Documents\tugas\tugas\studikasus\studikasus6.json"

def baca_data():
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def simpan_data(data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


while True:
    print("\n=== SISTEM PENCATATAN NILAI MAHASISWA ===")
    print("1. Lihat semua nilai")
    print("2. Tambah nilai baru")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        data = baca_data()
        print("\n--- Daftar Nilai ---")
        for i, mhs in enumerate(data, start=1):
            print(f"{i}. {mhs['nim']} | {mhs['nama']} | {mhs['mata_kuliah']} | {mhs['nilai']}")

    elif pilihan == "2":
        data = baca_data()

        
        data_baru = {
            "nim": input("NIM: "),
            "nama": input("Nama: "),
            "mata_kuliah": input("Mata Kuliah: "),
            "nilai": int(input("Nilai: "))
        }
        data.append(data_baru)

        simpan_data(data)
        print("Data berhasil disimpan!")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
