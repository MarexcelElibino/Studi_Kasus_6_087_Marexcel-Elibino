**NAMA: MAREXCEL ELIBINO**

**NIM: 2609116087**

**KELAS: C**

**TUGAS: GANJIL**


---

<img width="1463" height="992" alt="Screenshot 2026-10-06 202504" src="https://github.com/user-attachments/assets/dbcfa157-706d-40cd-913c-8972ecc81fa8" />
Ini isi file `studikasus6.json` sebelum ada data baru. Di dalamnya sudah ada dua data mahasiswa, yaitu Ucup (Matematika Diskrit, nilai 85) dan Rahullll (Dasar Pemrograman, nilai 78). Datanya berbentuk list yang diawali tanda `[` dan diakhiri `]`, dan tiap mahasiswa ditulis dalam kurung `{ }`.

---


<img width="928" height="102" alt="Screenshot 2026-10-06 202623" src="https://github.com/user-attachments/assets/8855a189-16dc-481c-af75-47e2d45e3e48" />
Baris 1 `import json` dipakai supaya Python bisa membaca dan menulis file JSON. Baris 2 berisi variabel `path`, yaitu lokasi file `studikasus6.json` di komputer saya.

---

<img width="1459" height="257" alt="Screenshot 2026-10-06 202722" src="https://github.com/user-attachments/assets/5fbb085c-901b-4b6a-b36a-975e8a1a9d5a" />
Ada dua fungsi di sini. `baca_data()` membuka file dengan mode `"r"`, lalu isinya diambil pakai `json.load()` dan dikembalikan sebagai list. `simpan_data()` membuka file dengan mode `"w"`, lalu list ditulis ke file pakai `json.dump()` dengan `indent=4` supaya rapi. Fungsi kedua inilah yang membuat data tersimpan permanen.


---
<img width="1920" height="1080" alt="Screenshot 2026-10-06 202819" src="https://github.com/user-attachments/assets/e892c207-084c-4d24-ba41-246a258ca2ab" />
Menunya ada di dalam `while True` jadi muncul terus sampai kita pilih menu 3. Kalau memilih 1, program memanggil `baca_data()` lalu menampilkan data satu per satu pakai `for`. Kalau memilih 2, program membaca data lama, meminta input NIM, nama, mata kuliah, dan nilai, memasukkannya ke list dengan `append()`, lalu menyimpannya lewat `simpan_data()`. Kalau memilih 3, program berhenti pakai `break`. Input selain 1, 2, dan 3 akan menampilkan "Pilihan tidak valid!".

---

<img width="1920" height="1080" alt="Screenshot 2026-10-06 203344" src="https://github.com/user-attachments/assets/9278156a-6417-4d77-9388-6509a9d85d4c" />
Setelah menambah data lewat menu 2, file `studikasus6.json` bertambah satu data, yaitu Excell (Bahasa Inggris, nilai 99). Jadi sekarang ada tiga data. Ini membuktikan data baru benar-benar tertulis ke dalam file.

---

<img width="1920" height="1080" alt="Screenshot 2026-10-06 203422" src="https://github.com/user-attachments/assets/621999c1-1e24-42d8-aad0-b8d531df1fa4" />
Saya menjalankan program dengan urutan berikut. Pertama, memilih menu 1 dan muncul dua data lama. Kedua, memilih menu 2 dan mengisi NIM 44444444, nama Excell, mata kuliah Bahasa Inggris, dan nilai 99, lalu muncul tulisan "Data berhasil disimpan!". Terakhir, memilih menu 3 dan program selesai.

---
<img width="1449" height="561" alt="Screenshot 2026-10-06 210010" src="https://github.com/user-attachments/assets/c136e62a-eefb-4c1c-9ccd-a5b980d9f0b8" />
Setelah program ditutup lalu dijalankan lagi, saya memilih menu 1 dan data Excell masih muncul. Artinya data tidak hilang karena sudah tersimpan di file JSON.








