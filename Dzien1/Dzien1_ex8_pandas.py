import pandas as pd

writer=pd.ExcelWriter('empty_file.xlsx', engine='xlsxwriter')
empty_dataframe=pd.DataFrame()

empty_dataframe.to_excel(writer, sheet_name='empty')


data=[['John', 25], ['Jane', 30, ], ['Darwin', 45], ['Joel', 39]]

column_names=["Name","Age"]

df=pd.DataFrame(data, columns=column_names)
writer=pd.ExcelWriter('excel_with_list.xlsx', engine='xlsxwriter')

# polecenie to_excel to jakby zapisanie pliku excel
df.to_excel(writer, sheet_name='first_sheet', index=False, freeze_panes=(4,0), startrow=3, startcol=2) # naglowek w 4 wierszu, frezee pance w 5

writer.close()



