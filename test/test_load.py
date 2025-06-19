import sys
import os
import unittest
import pandas as pd
from unittest.mock import patch, MagicMock

# Menambahkan path untuk mengimpor modul dari folder utilitas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utilitas.load import DataSaver

class TestDataSaver(unittest.TestCase):

    @patch('utilitas.load.pd.DataFrame.to_csv')
    def test_save_to_csv(self, mock_to_csv):
        # Arrange
        df = pd.DataFrame({
            'title': ['Kaos Polos', 'Jaket Hoodie'],
            'price': [15000, 35000],
            'rating': [4.0, 4.8]
        })
        saver = DataSaver(df)

        # Act
        saver.save_to_csv('dummy_output.csv')

        # Assert
        mock_to_csv.assert_called_once_with('dummy_output.csv', index=False)

if __name__ == '__main__':
    unittest.main()
