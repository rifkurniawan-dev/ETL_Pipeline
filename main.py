import pandas as pd
from utilitas.ekstrak import scrape_fashion
from utilitas.transform import clean_and_transform
from utilitas.load import DataSaver

def main():
    BASE_URL = 'https://fashion-studio.dicoding.dev/'

    print("Mengeksrak data dari website")
    raw_data = scrape_fashion(BASE_URL)
    if not raw_data:
        print("Tidak ada data yang berhasil diambil.")
        return

    df_raw = pd.DataFrame(raw_data)
    print(f"{len(df_raw)} baris data berhasil diambil.")

    print("Membersihkan dan mentransformasi data")
    df_clean = clean_and_transform(df_raw)
    print(f"{len(df_clean)} baris data setelah dibersihkan.")

    
    print("Menyimpan data ke dalam csv")
    saver = DataSaver(df_clean)
    saver.save_all()

    print("Proses ETL Pipeline selesai!")

if __name__ == '__main__':
    main()