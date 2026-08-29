# 🚀 Web UI Automation Framework (POM & Data-Driven Testing)

Proyek ini adalah *framework* pengujian otomatisasi *Web UI* tingkat lanjut yang dirancang menggunakan standar industri (Clean Code). Proyek ini memvalidasi fungsionalitas aplikasi *e-commerce* ([Saucedemo](https://www.saucedemo.com/)) dengan menerapkan arsitektur **Page Object Model (POM)** dan teknik **Data-Driven Testing (DDT)**.

## 🌟 Fitur Utama (Key Features)
1.  **Page Object Model (POM):** Pemisahan yang tegas antara elemen UI/Halaman dengan skrip pengujian (Test Logic), membuat kode sangat mudah dirawat (*maintainable*) dan skalabel.
2.  **Data-Driven Testing (DDT):** Menggunakan file CSV eksternal (`data/login_data.csv`) untuk menjalankan satu skenario pengujian berulang kali dengan berbagai kombinasi data tes (Positif & Negatif) secara otomatis.
3.  **Visual Reporting (Allure):** Terintegrasi penuh dengan **Allure Report** untuk menghasilkan dasbor laporan pengujian visual yang interaktif, menampilkan metrik kelulusan, waktu eksekusi, dan riwayat kegagalan.

## 🛠️ Teknologi yang Digunakan (Tech Stack)
*   **Bahasa Pemrograman:** Python
*   **Automation Tool:** Playwright
*   **Test Runner:** Pytest
*   **Reporting:** Allure Report
*   **Data Source:** CSV (Built-in Python `csv` module)

  <img width="1352" height="665" alt="allure" src="https://github.com/user-attachments/assets/c28ccddd-5d69-43b0-a6aa-30ae4d1e3dae" />

## 📁 Struktur Arsitektur Proyek
```text
qa-framework-pom/
├── data/
│   └── login_data.csv        # Sumber data tes (Username, Password, Expected Status)
├── pages/
│   ├── __init__.py
│   └── login_page.py         # Locator & Action methods khusus halaman Login
├── tests/
│   ├── __init__.py
│   └── test_login_pom.py     # Skrip eksekusi tes utama (Menggunakan @pytest.mark.parametrize)
├── allure-results/           # Direktori output data mentah Allure (Digenerate otomatis)
├── conftest.py               # Konfigurasi global Pytest & Playwright
└── README.md
