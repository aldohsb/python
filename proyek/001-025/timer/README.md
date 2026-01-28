# Minimalist Timer Application

Aplikasi timer minimalis untuk Windows dengan tampilan transparan, deteksi idle, statistik lengkap, dan sistem kategori.

## 🌟 Fitur

### Tampilan
- **Tampilan Minimalis**: Hanya menampilkan angka timer besar tanpa menu
- **Always on Top**: Selalu di atas window lain
- **Transparan**: Background transparan yang bisa diatur
- **Draggable**: Bisa dipindah-pindah dengan drag & drop

### Kontrol
- **System Tray**: Kontrol penuh dari system tray icon
- **Global Hotkeys**: Shortcut keyboard untuk pause/resume dan reset
- **Deteksi Idle**: Otomatis pause saat tidak ada aktivitas

### Organisasi
- **Kategori Timer**: Atur timer berdasarkan kategori (Work, Study, Exercise, dll)
- **Statistik Lengkap**: Lihat dan edit histori timer
- **Database SQLite**: Semua data tersimpan lokal

## 📋 Requirements

- Windows 7/8/10/11
- Python 3.7 atau lebih baru (untuk development)

## 🚀 Instalasi untuk Development

### 1. Install Python
Download dan install Python dari [python.org](https://www.python.org/downloads/)

### 2. Clone atau Download Project
```bash
# Extract project ke folder, misalnya C:\TimerApp
cd C:\TimerApp
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Aplikasi
```bash
python timer_app.py
```

## 🔨 Membuat Executable (.exe)

### Metode 1: Menggunakan PyInstaller (Recommended)

1. **Install PyInstaller**
```bash
pip install pyinstaller
```

2. **Build Single File Executable**
```bash
pyinstaller --onefile --windowed --name "MinimalTimer" timer_app.py
```

3. **Build dengan Icon (Opsional)**
```bash
# Jika punya icon file (.ico)
pyinstaller --onefile --windowed --icon=icon.ico --name "MinimalTimer" timer_app.py
```

4. **Executable akan ada di folder `dist/`**
```
dist/
└── MinimalTimer.exe
```

### Metode 2: Build dengan Semua Dependencies Terpisah

Jika ingin file size lebih kecil atau ada masalah dengan --onefile:

```bash
pyinstaller --windowed --name "MinimalTimer" timer_app.py
```

Ini akan membuat folder `dist/MinimalTimer/` dengan executable dan semua dependencies.

### Metode 3: Auto-py-to-exe (GUI Tool)

Untuk yang lebih suka GUI:

1. **Install auto-py-to-exe**
```bash
pip install auto-py-to-exe
```

2. **Run GUI**
```bash
auto-py-to-exe
```

3. **Konfigurasi di GUI:**
   - Script Location: `timer_app.py`
   - Onefile: One File
   - Console Window: Window Based
   - Icon: (Optional) pilih file .ico
   - Additional Files: Tambahkan semua file .py lainnya

4. **Click "Convert .py to .exe"**

## 📝 Struktur File

```
TimerApp/
├── timer_app.py          # Main application
├── database.py           # Database handler
├── settings_dialog.py    # Settings window
├── statistics_dialog.py  # Statistics window
├── category_dialog.py    # Category management
├── requirements.txt      # Python dependencies
├── README.md            # Documentation
└── timer_data.db        # SQLite database (dibuat otomatis)
```

## ⌨️ Default Keyboard Shortcuts

- **Ctrl + Alt + P**: Pause/Resume timer
- **Ctrl + Alt + R**: Reset timer

Shortcuts bisa diubah di Settings.

## 🎯 Cara Menggunakan

### Pertama Kali
1. Run aplikasi (timer_app.py atau .exe)
2. Window transparan dengan angka "00:00:00" akan muncul
3. Icon akan muncul di system tray

### Mengontrol Timer
- **Klik kanan icon di system tray** untuk menu:
  - Start/Pause: Mulai atau pause timer
  - Reset: Reset timer ke 0
  - Select Category: Pilih kategori untuk timer
  - Statistics: Lihat histori dan statistik
  - Settings: Atur preferensi
  - Show/Hide Timer: Sembunyikan/munculkan window
  - Exit: Keluar aplikasi

### Mengatur Kategori
1. Klik kanan tray icon → Select Category
2. Pilih kategori yang sudah ada atau Add New
3. Bisa edit nama dan warna kategori
4. Bisa delete kategori (session akan dipindah ke Uncategorized)

### Melihat Statistik
1. Klik kanan tray icon → Statistics
2. Tab **Sessions**: Lihat semua session, filter by category/days
3. Tab **Summary**: Lihat total waktu per kategori
4. Bisa **Edit** durasi session atau **Delete** session

### Settings yang Bisa Diatur
- **Font Size**: Ukuran angka timer (24-200pt)
- **Transparency**: Tingkat transparansi (30-100%)
- **Idle Threshold**: Waktu idle sebelum auto-pause (10-600 detik)
- **Keyboard Shortcuts**: Ubah hotkey untuk pause dan reset

## 🔧 Troubleshooting

### Aplikasi tidak muncul
- Cek system tray, mungkin window tersembunyi
- Double-click tray icon untuk show/hide

### Global hotkeys tidak bekerja
- Pastikan tidak bentrok dengan shortcut aplikasi lain
- Coba ubah shortcut di Settings
- Run as Administrator jika perlu

### Error saat build .exe
```bash
# Jika ada error module not found
pip install --upgrade pyinstaller
pip install --upgrade PyQt5 pynput

# Jika masih error, coba build tanpa --onefile
pyinstaller --windowed --name "MinimalTimer" timer_app.py
```

### Database error
- File `timer_data.db` akan dibuat otomatis di folder yang sama dengan executable
- Jika ada error, hapus file `timer_data.db` dan restart aplikasi

## 🎨 Customization

### Mengubah Warna Background Timer
Edit di `timer_app.py`, cari line:
```python
self.timer_label.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 150); ...")
```

### Menambah Default Categories
Edit di `database.py`, function `init_default_data()`:
```python
default_categories = [
    ("Your Category", "#FF6633"),
    # Tambah kategori lain...
]
```

### Mengubah Format Timer
Edit di `timer_app.py`, function `update_display()`:
```python
# Default: HH:MM:SS
time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Alternatif: MM:SS (tanpa jam)
time_str = f"{minutes:02d}:{seconds:02d}"
```

## 📦 Distribusi Aplikasi

Setelah build executable:

1. **Single File (.exe)**
   - Cukup bagikan file `MinimalTimer.exe`
   - User tinggal double-click untuk run

2. **Folder Distribution**
   - Zip folder `dist/MinimalTimer/` 
   - User extract dan run `MinimalTimer.exe`

3. **Installer (Optional)**
   - Gunakan Inno Setup atau NSIS untuk membuat installer
   - Include semua file dari folder dist

## 🐛 Known Issues

- Global hotkeys mungkin perlu administrator privileges di beberapa sistem
- Deteksi idle hanya bekerja di Windows
- Window position tidak tersimpan (reset setiap restart)

## 📄 License

Free to use and modify.

## 🤝 Contributing

Feel free to fork dan improve!

## 📧 Support

Jika ada pertanyaan atau bug, bisa create issue atau contact developer.

---

**Selamat menggunakan! 🎉**
