
import pandas as pd

class DataSaver:
    """Kelas untuk menyimpan data ke file CSV."""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def save_to_csv(self, filename: str = 'products.csv'):
        """Simpan data ke file CSV."""
        if self.df.empty:
            print("Dataframe kosong, tidak ada data yang disimpan.")
            return

        try:
            self.df.to_csv(filename, index=False)
            print(f"Data berhasil disimpan ke {filename}.")
        except Exception as e:
            print(f"Gagal menyimpan ke CSV: {e}")

    def save_all(self):
        """Panggil semua metode penyimpanan."""
        self.save_to_csv()
