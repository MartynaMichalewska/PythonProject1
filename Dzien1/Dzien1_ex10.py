import pandas as pd

age_data=[
    {"name":"Ada","Age":34},
    {"name":"Ola","Age":45},
    {"name":"Radek","Age":37},
    {"name":"Marek","Age":53}
]

hight_data=[
    {"name":"Ada","Hight":34},
    {"name":"Ola","Hight":45},
    {"name":"Radek","Hight":37},
    {"name":"Marek","Hight":53}
]
# rzucamy do tabelki
hight_data_df=pd.DataFrame(hight_data)
age_data_df=pd.DataFrame(age_data)

# kazda tabelke do innego taba
writer=pd.ExcelWriter("people.xlsx",engine="xlsxwriter")
hight_data_df.to_excel(writer,sheet_name="hight",index=False)
age_data_df.to_excel(writer,sheet_name="age",index=False)

writer.close()