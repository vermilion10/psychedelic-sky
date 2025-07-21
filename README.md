# psychedelic-sky (WIP)
<b>⚠️ note ⚠️ <br>
program masih dalam tahap pengerjaan sehingga program nya sendiri tidak akan berjalan dengan layak</b>

## Deskripsi

**psychedelic-sky** adalah aplikasi desktop (GUI) berbasis python yang memungkinkan pengguna untuk menerjemahkan teks yang muncul di layar secara langsung. pengguna dapat memilih area tertentu pada layar atau menerjemahkan seluruh tampilan layar, lalu aplikasi akan mengekstrak teks dari gambar menggunakan OCR (tesseract) dan menerjemahkannya ke bahasa indonesia secara otomatis (menggunakan google translate).

## Fitur

- Pilihan untuk menerjemahkan area tertentu atau seluruh layar.
- Ekstraksi teks dari gambar/screenshot dengan OCR.
- Deteksi otomatis bahasa sumber dan terjemahan ke bahasa Indonesia.
- Tampilan hasil terjemahan langsung di aplikasi.
- Progres terjemahan dan notifikasi jika terjadi kesalahan.

## Instalasi

1. Pastikan Python dan pip sudah terinstall.
2. Clone repositori:
   ```bash
   git clone https://github.com/vermilion10/psychedelic-sky.git
   ```
3. Masuk ke direktori proyek:
   ```bash
   cd psychedelic-sky/onscreen-translator
   ```
4. Install dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```
5. Pastikan sudah menginstall aplikasi [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) dan sesuaikan path `TESSERACT_CMD_PATH` di `config.py` sesuai lokasi instalasi di komputer anda.

## Penggunaan

Jalankan aplikasi dengan perintah berikut:
```bash
py main.py
```
- Pilih mode terjemahan: area tertentu atau seluruh layar.
- Seleksi area yang ingin diterjemahkan, hasil terjemahan akan muncul di aplikasi.

