import streamlit as st
import sqlite3
import pandas as pd

# Inisialisasi database SQLite
conn = sqlite3.connect('sales.db')
c = conn.cursor()

# Membuat tabel jika belum ada
c.execute('''CREATE TABLE IF NOT EXISTS Sales
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             tanggal DATE,
             pelanggan TEXT,
             jumlah REAL,
             total REAL)''')

c.execute('''CREATE TABLE IF NOT EXISTS Products
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nama TEXT,
             harga REAL)''')

# Fungsi untuk menambahkan data penjualan ke database
def add_sales(tanggal, pelanggan, jumlah, total):
    c.execute("INSERT INTO Sales (tanggal, pelanggan, jumlah, total) VALUES (?, ?, ?, ?)",
              (tanggal, pelanggan, jumlah, total))
    conn.commit()

# Fungsi untuk mendapatkan semua data penjualan
def get_all_sales():
    c.execute("SELECT * FROM Sales")
    rows = c.fetchall()
    return rows

# Fungsi untuk menampilkan aplikasi web
def main():
    st.title('Aplikasi Akuntansi Penjualan')

    menu = ['Tambah Penjualan', 'Lihat Penjualan', 'Analisis']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Tambah Penjualan':
        st.subheader('Input Penjualan Baru')
        tanggal = st.date_input('Tanggal')
        pelanggan = st.text_input('Nama Pelanggan')
        jumlah = st.number_input('Jumlah', min_value=1)
        total = st.number_input('Total', min_value=0.0)
        if st.button('Tambah'):
            add_sales(tanggal, pelanggan, jumlah, total)
            st.success('Penjualan berhasil ditambahkan!')

    elif choice == 'Lihat Penjualan':
        st.subheader('Data Penjualan')
        rows = get_all_sales()
        df = pd.DataFrame(rows, columns=['ID', 'Tanggal', 'Pelanggan', 'Jumlah', 'Total'])
        st.dataframe(df)

    elif choice == 'Analisis':
        st.subheader('Analisis Penjualan')
        # Di sini bisa ditambahkan grafik atau statistik sesuai kebutuhan

if __name__ == '__main__':
    main()
