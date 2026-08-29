import csv
import pytest
from pages.login_page import LoginPage

# Fungsi pembantu untuk membaca data dari file CSV
def baca_data_csv():
    data_list=[]
    # Membaca file CSV dari folder data
    with open('data/login_data.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Lewati baris pertama (Header: username,password,status)
        for row in reader:
            data_list.append(row) # Masukkan baris data ke dalam list
    return data_list

# Fitur Data-Driven Testing dari Pytest
# Pytest akan otomatis mengulang fungsi ini sebanyak jumlah baris di CSV
@pytest.mark.parametrize("username, password, status", baca_data_csv())
def test_login_data_driven(page, username, password, status):
    print(f"menguji login dengan username: {username} | status: {status}")

    #1 panggil page objek
    login_page = LoginPage(page)

    #2 lakuka aksi
    login_page.buka_halaman()
    login_page.login(username, password)

    #3 validasi assertion berdasarkan status yang diharapkan di csv
    if status == "sukses":
        assert page.url == "https://www.saucedemo.com/inventory.html"
    elif status == "gagal_terkunci":
        pesan = login_page.ambil_pesan_error()
        assert "locked out" in pesan.lower()
    elif status == "gagal_kredensial":
        pesan = login_page.ambil_pesan_error()
        assert "do not match" in pesan.lower()
