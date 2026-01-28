# Panduan Lengkap Penggunaan Minimalist Timer

## 📖 Daftar Isi
1. [Instalasi](#instalasi)
2. [Penggunaan Dasar](#penggunaan-dasar)
3. [Fitur-Fitur](#fitur-fitur)
4. [Tips & Trik](#tips--trik)
5. [FAQ](#faq)

---

## Instalasi

### Untuk Pengguna (Sudah Ada .exe)

1. **Download file `MinimalTimer.exe`**
2. **Double-click untuk menjalankan**
3. **Selesai!** Tidak perlu instalasi khusus

### Untuk Developer (Dari Source Code)

1. **Install Python 3.7+**
   - Download dari [python.org](https://www.python.org)
   - Pastikan centang "Add Python to PATH" saat install

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Aplikasi**
   ```bash
   python timer_app.py
   ```

4. **Build Executable (Optional)**
   ```bash
   # Cara Mudah: Double-click build.bat
   
   # Atau manual:
   pip install pyinstaller
   pyinstaller --onefile --windowed --name "MinimalTimer" timer_app.py
   ```

---

## Penggunaan Dasar

### Pertama Kali Membuka

1. **Jalankan aplikasi**
   - Double-click `MinimalTimer.exe` atau
   - Run `python timer_app.py`

2. **Window Timer Muncul**
   - Tampilan transparan dengan angka besar "00:00:00"
   - Bisa di-drag ke posisi yang kamu mau
   - Always on top (selalu di atas window lain)

3. **System Tray Icon**
   - Icon timer muncul di system tray (dekat jam)
   - Icon ini untuk mengakses semua fitur

### Mulai Timer

**Cara 1: System Tray**
- Klik kanan icon di system tray
- Pilih "Start"

**Cara 2: Keyboard Shortcut**
- Tekan `Ctrl + Alt + P` (default)

Timer akan mulai berjalan!

### Pause Timer

**Cara 1: System Tray**
- Klik kanan icon di system tray
- Pilih "Pause"

**Cara 2: Keyboard Shortcut**
- Tekan `Ctrl + Alt + P` lagi

**Cara 3: Auto-Pause**
- Timer akan otomatis pause jika kamu tidak menyentuh keyboard/mouse selama 60 detik (bisa diatur)

### Reset Timer

**Cara 1: System Tray**
- Klik kanan icon di system tray
- Pilih "Reset"

**Cara 2: Keyboard Shortcut**
- Tekan `Ctrl + Alt + R` (default)

Timer akan kembali ke 00:00:00

### Menyembunyikan/Menampilkan Window

**Cara 1: System Tray Menu**
- Klik kanan icon → "Show/Hide Timer"

**Cara 2: Double-Click Icon**
- Double-click icon di system tray

Window akan disembunyikan tapi timer tetap jalan!

---

## Fitur-Fitur

### 1. Kategori Timer

#### Mengapa Pakai Kategori?
- Atur waktu berdasarkan aktivitas (Work, Study, Exercise, dll)
- Lihat statistik per kategori
- Tracking lebih terorganisir

#### Cara Memilih Kategori

1. **Klik kanan tray icon → "Select Category"**

2. **Dialog kategori akan muncul dengan kategori default:**
   - Uncategorized (abu-abu)
   - Work (biru)
   - Study (orange)
   - Exercise (hijau)
   - Reading (ungu)
   - Project (merah)

3. **Pilih kategori dan klik "Select"**

4. **Timer sekarang menggunakan kategori yang dipilih**

#### Menambah Kategori Baru

1. **Di dialog kategori, klik "Add New"**
2. **Masukkan nama kategori**
3. **Pilih warna untuk kategori**
4. **Klik OK**

Contoh kategori yang bisa dibuat:
- Coding
- Meeting
- Gaming
- Cooking
- Meditation
- Social Media
- dll

#### Mengedit Kategori

1. **Pilih kategori yang mau diedit**
2. **Klik "Edit"**
3. **Ubah nama atau warna**
4. **Klik OK**

**Catatan:** Kategori "Uncategorized" tidak bisa diedit

#### Menghapus Kategori

1. **Pilih kategori yang mau dihapus**
2. **Klik "Delete"**
3. **Konfirmasi penghapusan**

**Penting:** 
- Semua session dengan kategori yang dihapus akan dipindah ke "Uncategorized"
- Kategori "Uncategorized" tidak bisa dihapus

### 2. Statistics (Statistik)

#### Membuka Statistik

**Klik kanan tray icon → "Statistics"**

#### Tab Sessions

**Apa yang bisa dilakukan:**
- Lihat semua session timer yang pernah kamu jalankan
- Filter berdasarkan kategori
- Filter berdasarkan jumlah hari (default: 30 hari terakhir)
- Edit durasi session
- Delete session

**Kolom yang ditampilkan:**
- ID: Nomor unik session
- Category: Kategori timer
- Duration: Lama waktu (HH:MM:SS)
- Start Time: Kapan mulai
- End Time: Kapan selesai
- Actions: Tombol Edit dan Delete

#### Edit Session

1. **Klik tombol "Edit" di session yang mau diubah**
2. **Masukkan durasi baru format HH:MM:SS**
   - Contoh: `02:30:45` untuk 2 jam 30 menit 45 detik
3. **Klik OK**

**Kapan perlu edit?**
- Salah catat waktu
- Timer lupa di-pause
- Ingin koreksi data manual

#### Delete Session

1. **Klik tombol "Delete"**
2. **Konfirmasi penghapusan**

**Hati-hati:** Data yang dihapus tidak bisa dikembalikan!

#### Tab Summary

**Menampilkan ringkasan total:**
- Jumlah session per kategori
- Total waktu per kategori
- Rata-rata waktu per session

**Contoh tampilan:**
```
Category    | Sessions | Total Time  | Average Time
Work        | 45       | 67:30:15    | 01:30:00
Study       | 30       | 45:15:30    | 01:30:31
Exercise    | 20       | 15:45:00    | 00:47:15
```

### 3. Settings (Pengaturan)

#### Membuka Settings

**Klik kanan tray icon → "Settings"**

#### Appearance (Tampilan)

**Font Size (Ukuran Angka)**
- Range: 24pt - 200pt
- Default: 72pt
- Semakin besar = angka semakin besar
- Cocok untuk berbagai ukuran monitor

**Transparency (Transparansi)**
- Range: 30% - 100%
- Default: 80%
- 30% = sangat transparan (nyaris tidak terlihat)
- 100% = solid (tidak transparan)
- Slider untuk adjust sesuai selera

#### Behavior (Perilaku)

**Idle Threshold (Batas Waktu Idle)**
- Range: 10 - 600 detik
- Default: 60 detik
- Timer akan auto-pause jika tidak ada aktivitas keyboard/mouse selama waktu ini
- Berguna agar timer tidak jalan saat kamu pergi

**Contoh:**
- Set 30 detik: Auto-pause cepat (untuk pekerjaan yang sering interupsi)
- Set 300 detik: Auto-pause lama (untuk pekerjaan fokus panjang)

#### Keyboard Shortcuts

**Pause/Resume Shortcut**
- Default: `<ctrl>+<alt>+p`
- Format: `<ctrl>+<alt>+<key>` atau `<ctrl>+<shift>+<key>`
- Contoh custom: `<ctrl>+<alt>+s`, `<ctrl>+<shift>+t`

**Reset Shortcut**
- Default: `<ctrl>+<alt>+r`
- Format sama seperti di atas

**Tips:**
- Pilih shortcut yang tidak bentrok dengan aplikasi lain
- Gunakan kombinasi yang mudah dijangkau
- Test shortcut setelah save

---

## Tips & Trik

### 1. Posisi Window Optimal

**Strategi Penempatan:**
- **Top Center**: Selalu terlihat tapi tidak mengganggu
- **Top Right Corner**: Di dekat jam system
- **Bottom Right**: Dekat taskbar
- **Second Monitor**: Jika punya dual monitor

**Cara Pindah:**
- Klik dan drag window ke posisi yang kamu mau
- Position tidak tersimpan, jadi akan reset setiap restart

### 2. Workflow dengan Kategori

**Metode Pomodoro:**
```
1. Pilih kategori "Work"
2. Set timer 25 menit (pause di 00:25:00)
3. Reset dan pilih "Break"
4. Set timer 5 menit
5. Ulangi
```

**Daily Tracking:**
```
Pagi:
- Kategori "Email" → 30 menit
- Kategori "Meeting" → 1 jam
- Kategori "Coding" → 3 jam

Sore:
- Kategori "Learning" → 2 jam
- Kategori "Exercise" → 1 jam
```

**Project-Based:**
```
- Project A: Buat kategori "Project A"
- Project B: Buat kategori "Project B"
- Analisis: Lihat total waktu per project di Statistics
```

### 3. Keyboard Shortcuts Efektif

**Recommended Shortcuts:**
- Pause: `<ctrl>+<alt>+p` (mudah dijangkau)
- Reset: `<ctrl>+<alt>+r` (dekat dengan P)

**Alternatif untuk Gaming:**
- Pause: `<ctrl>+<shift>+t` (tidak bentrok dengan game)
- Reset: `<ctrl>+<shift>+y`

### 4. Statistik Best Practices

**Weekly Review:**
1. Buka Statistics setiap akhir minggu
2. Set filter "7 days"
3. Analisis waktu per kategori
4. Identifikasi kategori yang kurang/over

**Data Cleanup:**
- Edit session yang tidak akurat
- Delete session yang salah
- Kategorisasi ulang jika perlu

**Goal Setting:**
```
Contoh Goals Mingguan:
- Work: min 40 jam
- Study: min 10 jam
- Exercise: min 5 jam
- Reading: min 3 jam
```

### 5. Multi-Task Workflow

**Quick Switch:**
```
1. Lagi kerja kategori "Coding"
2. Tiba-tiba meeting → Pause timer
3. Switch kategori ke "Meeting" → Start
4. Meeting selesai → Pause
5. Switch kembali ke "Coding" → Resume
```

**Task Batching:**
```
Morning:
- Semua email → Kategori "Email"
- Semua meeting → Kategori "Meeting"

Afternoon:
- Deep work → Kategori "Focus Work"
```

### 6. Transparansi Optimal

**Untuk Presentasi/Recording:**
- Set transparency 50-70%
- Timer terlihat tapi tidak terlalu mengganggu

**Untuk Fokus Pribadi:**
- Set transparency 80-90%
- Timer subtle di background

**Untuk Monitoring Ketat:**
- Set transparency 100%
- Timer jelas dan tegas

---

## FAQ

### Q: Aplikasi tidak muncul setelah di-run?

**A:** Cek system tray. Window mungkin tersembunyi.
- Double-click icon di tray untuk show/hide
- Atau klik kanan → "Show/Hide Timer"

### Q: Shortcut keyboard tidak bekerja?

**A:** Beberapa kemungkinan:
1. Shortcut bentrok dengan aplikasi lain
2. Perlu run as Administrator
3. Coba ubah shortcut di Settings
4. Restart aplikasi setelah ubah settings

### Q: Timer tidak auto-pause saat idle?

**A:** Pastikan:
1. Idle threshold sudah diset di Settings
2. Benar-benar tidak ada aktivitas keyboard/mouse
3. Coba turunkan idle threshold untuk testing

### Q: Bagaimana cara backup data?

**A:** Data tersimpan di file `timer_data.db`
1. Locate file di folder yang sama dengan .exe
2. Copy file `timer_data.db` ke tempat aman
3. Untuk restore: Replace file `timer_data.db` dengan backup

### Q: Bisa install di Mac/Linux?

**A:** Saat ini hanya Windows karena deteksi idle pakai Windows API.
- Untuk Mac/Linux perlu modifikasi kode
- Bisa run dari source dengan beberapa adjustment

### Q: Timer loss precision?

**A:** Timer update setiap detik, jadi presisi hingga detik.
- Jika perlu presisi milidetik, perlu modifikasi kode
- Untuk daily tracking, presisi detik sudah cukup

### Q: Bagaimana cara uninstall?

**A:**
1. Close aplikasi dari tray icon → Exit
2. Delete file `MinimalTimer.exe`
3. Delete file `timer_data.db` jika tidak perlu data
4. Selesai! Tidak ada registry atau file system lain

### Q: File .exe dideteksi sebagai virus?

**A:** False positive dari antivirus.
- PyInstaller executable sering di-flag
- Aplikasi 100% aman (cek source code)
- Add to exception di antivirus jika perlu

### Q: Bisa customize tampilan lebih lanjut?

**A:** Ya! Edit source code:
- Warna background: `timer_app.py` line ~120
- Format waktu: `timer_app.py` function `update_display()`
- Default categories: `database.py` function `init_default_data()`

### Q: Timer terus jalan setelah close window?

**A:** Itu fitur! Window close = hide, bukan exit.
- Timer tetap jalan di background
- Lihat di tray icon
- Untuk benar-benar exit: Klik kanan tray → Exit

### Q: Data statistik berapa lama disimpan?

**A:** Semua data disimpan permanent di database.
- Tidak ada auto-delete
- Bisa manual delete via Statistics dialog
- Database tidak punya size limit (sampai harddisk penuh)

### Q: Bisa sync data antar device?

**A:** Tidak ada fitur sync built-in.
- Manual: Copy file `timer_data.db` antar device
- Future feature: Bisa add cloud sync (Google Drive, Dropbox, etc)

---

## 🎓 Advanced Usage

### Custom Categories untuk Freelancer

```
Kategori per Client:
- Client A
- Client B
- Client C

Kategori per Task Type:
- Design
- Development
- Meeting
- Email

→ Combine untuk tracking detail
```

### Time Blocking Method

```
1. Buat kategori "Deep Work"
2. Set 4-hour timer
3. No distraction, pure focus
4. Lihat statistics → improve consistency
```

### Productivity Analysis

```
Weekly Report:
1. Export data (manual dari Statistics)
2. Analisis:
   - Total productive hours
   - Distribution per category
   - Peak productive times
3. Adjust schedule based on data
```

---

## 🔄 Update & Support

### Cek Update
- Tidak ada auto-update
- Cek GitHub/source untuk versi baru
- Download dan replace .exe

### Report Bug
- Screenshot error message
- Describe steps to reproduce
- Kirim via GitHub issues atau email

### Request Feature
- Jelaskan use case
- Kenapa feature itu penting
- Submit via GitHub atau email

---

**Selamat Produktif! 🚀**

*Timer ini dibuat untuk membantu kamu track waktu dengan mudah dan efisien. Semoga bermanfaat!*
