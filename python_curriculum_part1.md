# Kurikulum Python: Data Analytics & Automation
## Part 1: Foundation & Basic Python (Hari 1-60)

### MINGGU 1-2: Pengenalan & Setup (Hari 1-14)

**Hari 1: Pengenalan Programming & Python**
* Apa itu programming dan mengapa Python?
* Kegunaan Python dalam data analytics dan automation
* Instalasi Python, VS Code, dan Jupyter Notebook
* Menjalankan program Python pertama

Project: Hello World & Kalkulator Sederhana
- Buat program yang mencetak "Hello, World!"
- Buat kalkulator sederhana yang bisa menjumlahkan 2 angka
- Input dari user menggunakan input()
- Output menggunakan print()

**Hari 2: Variables & Data Types**
* Konsep variabel dan penamaan variabel
* Tipe data dasar: string, integer, float, boolean
* Type conversion dan type checking
* Operasi dasar pada setiap tipe data

Project: Konverter Suhu
- Program untuk mengkonversi Celsius ke Fahrenheit dan Kelvin
- Input suhu dari user
- Tampilkan hasil konversi dalam format yang rapi
- Gunakan variabel dengan nama yang descriptive

**Hari 3: String Manipulation Dasar**
* String indexing dan slicing
* String methods: upper(), lower(), strip(), replace()
* String concatenation dan f-strings
* Multi-line strings

Project: Text Formatter
- Program yang menerima nama lengkap user
- Format output: uppercase, lowercase, title case
- Hitung jumlah karakter dan kata
- Extract nama depan dan belakang

**Hari 4: Numbers & Basic Math**
* Operasi aritmatika (+, -, *, /, //, %, **)
* Import module math
* Pembulatan angka (round, ceil, floor)
* Random numbers

Project: Kalkulator BMI
- Input tinggi (cm) dan berat badan (kg)
- Hitung BMI dengan formula
- Kategorikan hasil (underweight, normal, overweight, obese)
- Format output dengan 2 desimal

**Hari 5: Boolean & Comparison Operators**
* Boolean values (True/False)
* Comparison operators (==, !=, >, <, >=, <=)
* Logical operators (and, or, not)
* Truth tables

Project: Password Validator Sederhana
- Cek panjang password minimal 8 karakter
- Cek apakah mengandung angka
- Cek apakah mengandung huruf besar
- Beri feedback valid/tidak valid

**Hari 6-7: Review & Mini Challenge**
* Review semua konsep minggu pertama
* Debugging dasar dan error handling sederhana
* Best practices dalam menulis kode

Project: Aplikasi Biodata Mahasiswa
- Input: nama, NIM, umur, IPK
- Validasi: NIM harus angka, IPK 0-4
- Format output yang rapi dengan f-strings
- Tampilkan kategori prestasi berdasarkan IPK

**Hari 8: Conditional Statements - If/Else**
* Struktur if, elif, else
* Nested conditionals
* Kondisi dengan multiple conditions
* Ternary operators

Project: Sistem Grading Nilai
- Input nilai 0-100
- Konversi ke grade (A, B, C, D, E)
- Tampilkan status kelulusan
- Beri rekomendasi berdasarkan nilai

**Hari 9: Conditional Statements Lanjutan**
* Match-case statements (Python 3.10+)
* Guard conditions
* Best practices dalam conditional logic

Project: Kalkulator Diskon Belanja
- Input total belanja
- Hitung diskon berdasarkan tier (>500rb: 20%, >200rb: 10%, dll)
- Tampilkan total sebelum diskon, diskon, dan total bayar
- Cek apakah dapat free ongkir

**Hari 10: Lists - Part 1**
* Membuat dan mengakses list
* List indexing dan slicing
* List methods: append(), insert(), remove(), pop()
* List length dengan len()

Project: To-Do List Sederhana
- Buat list untuk menyimpan tasks
- Tambah task baru
- Hapus task yang sudah selesai
- Tampilkan semua tasks dengan numbering

**Hari 11: Lists - Part 2**
* List sorting dan reversing
* List copying
* List comprehension dasar
* Nested lists

Project: Pencatat Nilai Siswa
- Simpan nilai beberapa mata pelajaran dalam list
- Hitung rata-rata nilai
- Temukan nilai tertinggi dan terendah
- Urutkan nilai dari tertinggi ke terendah

**Hari 12: Loops - While Loop**
* Struktur while loop
* Loop counter
* Break dan continue
* Infinite loops dan cara menghindarinya

Project: Number Guessing Game
- Program tebak angka 1-100
- User punya maksimal 7 kesempatan
- Beri hint "terlalu tinggi" atau "terlalu rendah"
- Tampilkan jumlah percobaan saat berhasil

**Hari 13: Loops - For Loop**
* Struktur for loop
* Range function
* Iterasi melalui lists dan strings
* Enumerate dan zip

Project: Pattern Generator
- Buat pola bintang segitiga
- Buat pola piramida
- Buat pola angka
- User bisa input tinggi pola

**Hari 14: Review Week 2 & Integration**
* Review lists dan loops
* Combining conditionals dengan loops
* Nested loops

Project: Sistem Kasir Mini Market
- List produk dengan harga
- User bisa tambah produk ke keranjang (loop)
- Hitung total belanja
- Tampilkan struk pembelian
- Hitung kembalian

### MINGGU 3-4: Data Structures & Functions (Hari 15-28)

**Hari 15: Tuples & Sets**
* Perbedaan tuple, list, dan set
* Tuple packing dan unpacking
* Set operations (union, intersection, difference)
* Immutability concept

Project: Sistem Koordinat
- Input beberapa titik koordinat (x, y) sebagai tuple
- Simpan dalam list
- Hitung jarak antar titik
- Cari titik terjauh dari origin (0, 0)

**Hari 16: Dictionaries - Part 1**
* Membuat dan mengakses dictionary
* Adding dan modifying items
* Dictionary methods: keys(), values(), items()
* Checking key existence

Project: Kontak Book
- Dictionary untuk menyimpan nama dan nomor telepon
- Tambah kontak baru
- Cari kontak berdasarkan nama
- Update nomor telepon
- Hapus kontak

**Hari 17: Dictionaries - Part 2**
* Nested dictionaries
* Dictionary comprehension
* Merging dictionaries
* Default values dengan get()

Project: Database Mahasiswa Sederhana
- Dictionary nested untuk menyimpan data mahasiswa
- Setiap mahasiswa punya: nama, NIM, nilai per mata kuliah
- Hitung IPK per mahasiswa
- Cari mahasiswa dengan IPK tertinggi

**Hari 18: Functions - Part 1**
* Definisi dan pemanggilan function
* Parameters dan arguments
* Return values
* Scope variables (local vs global)

Project: Kalkulator Fungsi Matematika
- Function untuk operasi matematika (tambah, kurang, kali, bagi)
- Function untuk menghitung luas dan keliling (persegi, lingkaran, segitiga)
- Function untuk konversi satuan
- Menu untuk memilih fungsi

**Hari 19: Functions - Part 2**
* Default parameters
* Keyword arguments
* *args dan **kwargs
* Lambda functions

Project: Text Analyzer
- Function untuk hitung jumlah kata
- Function untuk hitung frekuensi huruf
- Function untuk cek palindrome
- Function untuk reverse text
- Main function yang memanggil semua analyzer

**Hari 20: Functions - Part 3**
* Recursive functions
* Function documentation (docstrings)
* Type hints dasar
* Best practices dalam function design

Project: Kalkulator Faktorial & Fibonacci
- Function rekursif untuk faktorial
- Function rekursif untuk fibonacci
- Function iteratif sebagai pembanding
- Tampilkan perbandingan waktu eksekusi

**Hari 21: Review & Mini Project**
* Review data structures dan functions
* Combining concepts
* Code organization

Project: Sistem Inventori Toko
- Dictionary untuk produk (nama, harga, stok)
- Function untuk tambah produk
- Function untuk update stok
- Function untuk cari produk
- Function untuk laporan nilai inventori
- Menu interaktif dengan loop

**Hari 22: File Handling - Reading**
* Opening dan closing files
* Reading methods: read(), readline(), readlines()
* Context manager (with statement)
* File paths (absolute vs relative)

Project: Log File Reader
- Buat sample log file
- Baca dan tampilkan isi file
- Hitung jumlah baris
- Cari kata tertentu dalam file
- Tampilkan baris yang mengandung keyword

**Hari 23: File Handling - Writing**
* Writing modes (w, a, r+)
* Write dan writelines
* Creating new files
* File encoding

Project: Notes Application
- Menu: tambah note, lihat semua notes, cari note
- Simpan notes ke file text
- Setiap note punya timestamp
- Load notes saat program start
- Save notes saat program exit

**Hari 24: Working with CSV**
* CSV format introduction
* Reading CSV dengan csv module
* Writing to CSV
* CSV with headers

Project: Student Grade Manager (CSV)
- Baca data nilai siswa dari CSV
- Tambah siswa baru
- Update nilai siswa
- Hitung rata-rata kelas
- Export laporan ke CSV baru

**Hari 25: Exception Handling - Part 1**
* Try-except blocks
* Multiple except clauses
* Catching specific exceptions
* Exception hierarchy

Project: Safe Calculator
- Kalkulator dengan error handling
- Handle division by zero
- Handle invalid input (non-numeric)
- Handle empty input
- Beri pesan error yang user-friendly

**Hari 26: Exception Handling - Part 2**
* Else dan finally clauses
* Raising exceptions
* Custom exceptions
* Best practices

Project: File Processor dengan Error Handling
- Baca file dengan error handling (file not found)
- Parse data dengan error handling (format error)
- Write output dengan error handling (permission error)
- Log semua errors ke file terpisah

**Hari 27: Modules & Imports**
* Import statement
* From import
* Import dengan alias
* Creating custom modules

Project: Math Utilities Module
- Buat module sendiri dengan fungsi matematika
- Module untuk statistik dasar (mean, median, mode)
- Module untuk geometry calculations
- Main program yang import dan gunakan modules

**Hari 28: Review Week 3-4**
* Comprehensive review
* Best practices consolidation
* Debugging techniques

Project: Mini CLI Application - Expense Tracker
- Track income dan expenses
- Simpan data ke CSV
- Functions untuk: add transaction, view all, monthly summary
- Exception handling untuk invalid input
- Report generation (total income, expenses, balance)
- Data persistence (save/load dari file)

### MINGGU 5-6: String Processing & Data Manipulation (Hari 29-42)

**Hari 29: Advanced String Methods**
* String searching: find(), index(), count()
* String validation: isdigit(), isalpha(), isalnum()
* String formatting: format(), f-strings advanced
* String splitting dan joining

Project: Email Validator & Formatter
- Validasi format email
- Extract username dan domain
- Normalize email (lowercase, strip spaces)
- Cek domain yang valid
- Batch process multiple emails

**Hari 30: Regular Expressions - Part 1**
* Introduction to regex
* Basic patterns dan metacharacters
* re.search(), re.match(), re.findall()
* Character classes

Project: Phone Number Extractor
- Extract nomor telepon dari text
- Support multiple format (08xx, +62, (021))
- Validasi format nomor Indonesia
- Normalize ke format standard
- Save ke CSV

**Hari 31: Regular Expressions - Part 2**
* Groups dan capturing
* Lookahead dan lookbehind
* Substitution dengan re.sub()
* Regex flags

Project: Data Scrubber
- Clean text data dari file
- Remove special characters
- Extract specific patterns (email, URL, dates)
- Standardize format
- Generate clean output file

**Hari 32: Working with Dates & Times**
* datetime module
* Creating dan formatting dates
* Timedelta operations
* Timezone handling

Project: Event Countdown & Age Calculator
- Hitung umur detail (tahun, bulan, hari)
- Countdown ke event tertentu
- Hitung hari kerja antara 2 tanggal
- Generate calendar untuk bulan tertentu
- Log event dengan timestamp

**Hari 33: JSON Handling**
* JSON format introduction
* json.dumps() dan json.loads()
* Reading dan writing JSON files
* Pretty printing JSON

Project: Configuration Manager
- Baca settings dari JSON file
- Update settings
- Validate settings structure
- Save configuration
- Default configuration handling

**Hari 34: Working with Multiple Files**
* Directory operations dengan os
* Listing files dalam folder
* File operations: rename, move, delete
* Path manipulation dengan pathlib

Project: File Organizer
- Scan folder untuk files
- Organize files by extension (images, docs, videos)
- Rename files based on pattern
- Generate report of file types
- Create backup structure

**Hari 35: Data Cleaning Basics**
* Handling missing data
* Data type conversion
* String cleaning techniques
* Data validation

Project: CSV Data Cleaner
- Load messy CSV data
- Handle missing values
- Clean string data (strip, normalize)
- Validate data types
- Export cleaned data
- Generate data quality report

**Hari 36: List & Dict Comprehensions Advanced**
* Nested comprehensions
* Conditional comprehensions
* Dict comprehension dengan filtering
* Performance considerations

Project: Data Transformer
- Transform list of dicts ke different structure
- Filter data based on multiple conditions
- Aggregate data by category
- Pivot data structure
- Performance comparison dengan traditional loops

**Hari 37: Sorting & Filtering Data**
* sorted() dengan custom key
* Sorting complex structures
* Filter() function
* Multiple level sorting

Project: Product Ranking System
- List of products dengan attributes (price, rating, sales)
- Sort by different criteria
- Filter by price range dan rating
- Combine filters
- Generate top 10 report

**Hari 38: Data Aggregation Basics**
* Grouping data
* Calculating aggregates (sum, avg, count)
* Using Counter from collections
* Basic pivot operations

Project: Sales Report Generator
- Load sales data (product, quantity, price, date)
- Aggregate by product
- Aggregate by date/month
- Calculate totals dan averages
- Generate summary report
- Export to JSON dan CSV

**Hari 39: Working with APIs - Part 1**
* HTTP requests concept
* requests library introduction
* GET requests
* Handling responses

Project: Weather Data Fetcher
- Get weather data dari public API
- Parse JSON response
- Display formatted weather info
- Handle API errors
- Save data to file untuk offline use

**Hari 40: Working with APIs - Part 2**
* POST requests
* API authentication basics
* Rate limiting
* Error handling untuk API calls

Project: Currency Converter
- Fetch real-time exchange rates dari API
- Convert between currencies
- Cache rates to reduce API calls
- Handle API failures gracefully
- Log all conversions

**Hari 41: Project Integration Day**
* Combining all concepts learned
* Project planning
* Code organization best practices

Project: Personal Finance Dashboard (2 hari)
Hari 41-42 (Project besar):
- Track multiple accounts (CSV storage)
- Add transactions dengan kategori
- Monthly reports dan statistics
- Budget tracking
- Data visualization dengan ASCII charts
- Export reports to JSON/CSV
- Configuration via JSON
- Full error handling
- CLI menu system

**Hari 42: Personal Finance Dashboard - Completion**
* Testing semua features
* Documentation
* Code refinement

(Lanjutan project hari 41)
- Add recurring transactions feature
- Income vs expense analysis
- Category-wise breakdown
- Year-over-year comparison
- README documentation

### MINGGU 7-8: Introduction to Data Analytics (Hari 43-56)

**Hari 43: Statistics Fundamentals**
* Mean, median, mode calculation manual
* Standard deviation dan variance
* Percentiles dan quartiles
* Understanding distributions

Project: Grade Statistics Calculator
- Calculate statistics untuk dataset nilai
- Identify outliers
- Quartile analysis
- Generate text-based histogram
- Statistical summary report

**Hari 44: Introduction to NumPy - Part 1**
* NumPy installation
* Arrays vs Lists
* Creating arrays berbagai cara
* Array indexing dan slicing

Project: Array Calculator
- Create arrays dari user input
- Basic array operations
- Array statistics
- Array reshaping
- Compare performance vs lists

**Hari 45: NumPy - Part 2**
* Array operations dan broadcasting
* Universal functions
* Array manipulation
* Boolean indexing

Project: Sales Data Analyzer (NumPy)
- Load sales data ke NumPy array
- Calculate statistics by region
- Filter data using boolean indexing
- Compute trends
- Export results

**Hari 46: NumPy - Part 3**
* Mathematical operations
* Linear algebra basics
* Random number generation
* Saving dan loading arrays

Project: Random Data Generator & Analyzer
- Generate synthetic dataset
- Statistical analysis
- Correlation calculation
- Save dataset untuk future use
- Data quality metrics

**Hari 47: Introduction to Pandas - Part 1**
* Pandas installation
* Series dan DataFrame
* Reading CSV dengan pandas
* Basic DataFrame operations

Project: CSV Explorer
- Load CSV file to DataFrame
- Display basic info (shape, columns, dtypes)
- Show first/last rows
- Basic statistics
- Export subsets

**Hari 48: Pandas - Part 2**
* Selecting data: loc, iloc
* Filtering data
* Sorting data
* Adding dan removing columns

Project: Student Performance Analyzer
- Load student data
- Filter by performance criteria
- Add calculated columns (grades, pass/fail)
- Sort by multiple criteria
- Generate filtered reports

**Hari 49: Pandas - Part 3**
* Handling missing data
* Data type conversion
* String operations dalam pandas
* Apply functions

Project: Data Cleaning Pipeline
- Load messy dataset
- Identify missing values
- Fill or drop missing data
- Convert data types
- Clean string columns
- Validate cleaned data
- Export clean dataset

**Hari 50: Pandas - GroupBy & Aggregation**
* GroupBy operations
* Aggregate functions
* Multiple aggregations
* Pivot tables basics

Project: E-commerce Sales Analysis
- Load transaction data
- Group by product category
- Calculate total sales per category
- Monthly sales aggregation
- Customer purchase patterns
- Top products report

**Hari 51: Pandas - Merging & Joining**
* Concatenating DataFrames
* Merge operations
* Join types (inner, outer, left, right)
* Handling duplicates

Project: Customer Order Merger
- Multiple CSV files (customers, orders, products)
- Merge all data sources
- Create complete transaction view
- Calculate customer lifetime value
- Generate comprehensive report

**Hari 52: Data Visualization Basics - Matplotlib Part 1**
* Matplotlib installation
* Basic plotting
* Line plots
* Customizing plots (labels, title, colors)

Project: Temperature Trend Plotter
- Load temperature data
- Create line plot untuk trends
- Multiple lines untuk comparison
- Add labels dan legends
- Save plots to file

**Hari 53: Matplotlib - Part 2**
* Bar charts dan histograms
* Scatter plots
* Subplots
* Styling plots

Project: Sales Visualization Dashboard
- Bar chart untuk sales by category
- Histogram untuk price distribution
- Scatter plot untuk price vs quantity
- Multiple subplots dalam satu figure
- Export visualizations

**Hari 54: Matplotlib - Part 3**
* Pie charts
* Box plots
* Customization advanced
* Figure dan axes object

Project: Survey Result Analyzer
- Pie chart untuk categorical data
- Box plot untuk response distributions
- Customized styling
- Multi-page report dengan plots
- Professional formatting

**Hari 55: Introduction to Seaborn**
* Seaborn installation
* Seaborn vs Matplotlib
* Statistical plots
* Styling dengan seaborn

Project: Dataset Explorer dengan Seaborn
- Load dataset
- Create distribution plots
- Correlation heatmap
- Pairplot untuk relationships
- Styled statistical visualizations

**Hari 56: Review & Integration Week 7-8**
* Review NumPy dan Pandas
* Visualization best practices
* End-to-end analysis workflow

Project: Complete Data Analysis Project
- Load real-world dataset (e.g., COVID, sales, weather)
- Data cleaning dengan Pandas
- Statistical analysis dengan NumPy
- Grouping dan aggregation
- Multiple visualizations
- Comprehensive report
- Insights dan conclusions

### MINGGU 9: Consolidation & Practice (Hari 57-60)

**Hari 57: Best Practices & Code Quality**
* PEP 8 style guide
* Code documentation
* Naming conventions
* Code organization

Project: Code Refactoring Exercise
- Take previous projects
- Apply PEP 8 standards
- Add comprehensive docstrings
- Improve variable names
- Reorganize code structure

**Hari 58: Debugging & Testing Basics**
* Debugging techniques
* Using print statements effectively
* Understanding error messages
* Basic unit testing concept

Project: Bug Hunting Challenge
- Debug intentionally broken code
- Write test cases
- Fix issues systematically
- Document fixes

**Hari 59: Version Control Introduction**
* Git basics
* GitHub introduction
* Committing changes
* Repository management

Project: Portfolio Setup
- Create GitHub account
- Upload previous projects
- Write README files
- Organize repository structure

**Hari 60: Month 2 Review & Assessment**
* Comprehensive review of all topics
* Self-assessment
* Identifying knowledge gaps

Project: Personal Data Analysis
- Choose personal interest dataset
- Complete analysis pipeline
- From data loading to visualization
- Document process
- Present findings
- GitHub repository upload

---

## Progress Check - Hari 60
Setelah 60 hari, Anda seharusnya sudah:
✓ Memahami fundamental Python programming
✓ Comfortable dengan data structures (lists, dicts, sets, tuples)
✓ Bisa menulis functions dan handle errors
✓ Familiar dengan file operations
✓ Mengerti basics NumPy dan Pandas
✓ Bisa membuat visualizations sederhana
✓ Punya portfolio projects di GitHub

**Next Phase Preview**: Hari 61-120 akan fokus pada advanced Pandas, data cleaning workflows, statistical analysis, dan introduction to automation basics.
