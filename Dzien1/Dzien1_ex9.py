import pandas as pd

data=[
    {"name":"Ada","Age":34},
    {"name":"Ola","Age":45},
    {"name":"Radek","Age":37},
    {"name":"Marek","Age":53}
]

df=pd.DataFrame(data)
print(df)

writer=pd.ExcelWriter("people.xlsx",engine="xlsxwriter")
df.to_excel(writer,sheet_name="People",index=False)

writer.close()


