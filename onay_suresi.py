import pandas as pd


dfOnay = pd.read_excel(r"C:\Users\klv13\Desktop\Taşeron Hakedişi Tabloları\HakedisOnay.xlsx")

dfOnay.sort_values(["Satınalma belgesi","Hakediş No", "Onay Sırası"],ascending=True, inplace=True)

dfOnay["Onaycı"] = dfOnay["Adı"] + " " + dfOnay["Soyadı"]

dfOnay = dfOnay.astype(str)

dfOnay["Yaratma tarihi"] = pd.to_datetime(dfOnay["Yaratma tarihi"] + " " + dfOnay["Yaratma saati"],errors="coerce")
dfOnay["Onay Tarihi"] = pd.to_datetime(dfOnay["Onay Tarihi"] + " " + dfOnay["Onay Saati"] ,errors="coerce")

df = dfOnay.drop(['Yaratma saati', 'Onay Saati'], axis=1)

gruplu = df.groupby(["Satınalma belgesi","Hakediş No"])

gruplu.apply() 


