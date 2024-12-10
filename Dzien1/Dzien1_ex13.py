import pandas as pd

# liczy suma dla danej kolumny

df=pd.read_excel('excel_without_index-1.xlsx')
suma=df['Height'].sum(skipna=False)
print(suma)

