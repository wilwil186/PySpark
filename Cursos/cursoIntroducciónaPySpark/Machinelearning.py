import pandas as pd

# Crear datos de ejemplo
data = {
    'InvoiceNo': ['536365', '536366', '536367', '536368', '536369'],
    'StockCode': ['85123A', '71053', '84406B', '84029G', '84048'],
    'Description': ['WHITE HANGING HEART T-LIGHT HOLDER', 'WHITE METAL LANTERN', 'CREAM CUPID HEARTS COAT HANGER', 'KNITTED UNION FLAG HOT WATER BOTTLE', 'DOORMAT WELCOME TO OUR HOME'],
    'Quantity': [6, 2, 8, 6, 4],
    'InvoiceDate': ['2010-12-01 08:26:00', '2010-12-01 08:28:00', '2010-12-01 08:34:00', '2010-12-01 13:24:00', '2010-12-01 13:25:00'],
    'UnitPrice': [2.55, 3.39, 2.75, 3.39, 7.65],
    'CustomerID': [17850, 17850, 13047, 13047, 13047],
    'Country': ['United Kingdom', 'United Kingdom', 'United Kingdom', 'United Kingdom', 'United Kingdom']
}

# Crear el dataframe
df = pd.DataFrame(data)

# Mostrar el dataframe
print(df)
