import pandas as pd

df=pd.read_excel('excel_with_multiple_sheets-1.xlsx', sheet_name=0)
df1=pd.read_excel('excel_with_multiple_sheets-1.xlsx', sheet_name="marks")
print(df)
print(df1)

# lista wszytskich zakladek
df3=pd.ExcelFile('excel_with_multiple_sheets-1.xlsx')
print(df3.sheet_names)

# odczytywanie nazwy kolumn
print(df.columns.tolist())
