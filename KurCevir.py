import pandas as pd



def kurKolonuEkle(dfLeft,dfRight,columnLeft,columnRight,leftGroupColumn):
    dfHk = dfLeft
    dfKr = dfRight

    groupped= dfHk.groupby(leftGroupColumn)
    kurGroupped = dfKr.groupby(["Kur tipi",'Kaynak para birimi','Hedef para birimi'])
    dfKr["Kur"] = dfKr["Kur"].replace(",",".",regex=True)
    if "TRY" in dfHk[leftGroupColumn].unique():
        tl = groupped.get_group("TRY")
        tl["Kur"] = 1
        
    if "EUR" in dfHk[leftGroupColumn].unique():
        eur = groupped.get_group("EUR")
        eurToTry= kurGroupped.get_group(("M","EUR","TRY"))
        eurToTry["Kur"] = eurToTry["Kur"].astype(float)
        dfEur= pd.merge(eur,eurToTry,left_on=columnLeft,right_on=columnRight,how="left")
        dfEur["Kur"] = dfEur["Kur"].fillna(method="ffill").fillna(method="bfill")
        df = pd.concat([tl,dfEur])
    if "USD" in dfHk[leftGroupColumn].unique():
        usd = groupped.get_group("USD")
        usdToTry = kurGroupped.get_group(("M","USD","TRY"))
        usdToTry["Kur"] = usdToTry["Kur"].astype(float)
        dfUsd= pd.merge(usd,usdToTry,left_on=columnLeft,right_on=columnRight,how="left")
        dfUsd["Kur"] = dfUsd["Kur"].fillna(method="ffill").fillna(method="bfill")
        df = pd.concat([df,dfUsd])
    if "KZT" in dfHk[leftGroupColumn].unique():
        kzt = groupped.get_group("KZT")
        kztToTry = kurGroupped.get_group(("K","TRY","KZT"))
        kztToTry["Kur"] = kztToTry["Kur"].astype(float)
        kztToTry["Kur"]=1/kztToTry["Kur"]
        dfKzt= pd.merge(kzt,kztToTry,left_on=columnLeft,right_on=columnRight,how="left")
        dfKzt["Kur"] = dfKzt["Kur"].fillna(method="ffill").fillna(method="bfill")
        df = pd.concat([df,dfKzt])
    if "GBP" in dfHk[leftGroupColumn].unique():
        gbp = groupped.get_group("GBP")
        gbpToTry = kurGroupped.get_group(("M","GBP","TRY"))
        dfGbp= pd.merge(gbp,gbpToTry,left_on=columnLeft,right_on=columnRight,how="left")
        dfGbp["Kur"] = dfGbp["Kur"].fillna(method="ffill").fillna(method="bfill")
        df = pd.concat([df,dfGbp])
    

 
    

    df=df.drop(['Kur tipi', 'Kaynak para birimi', 'Hedef para birimi',
            'Faktör (kyn)', 'Faktör(hedef)'],axis=1)

    

    if columnLeft != columnRight:
        df=df.drop([columnRight],axis=1)

    dfTry = pd.merge(df,eurToTry,left_on=columnLeft,right_on=columnRight,suffixes=("_toTry","_toEur"),how="left")

    if columnLeft != columnRight:
        dfTry=dfTry.drop([columnRight],axis=1)

    dfTry["Kur_toEur"] = dfTry["Kur_toEur"].astype(float)
    dfTry["Kur_toTry"] = dfTry["Kur_toTry"].astype(float)

    dfTry["Kur_toEur"] = 1/dfTry["Kur_toEur"]

    dfTry=dfTry.drop(['Kur tipi', 'Kaynak para birimi', 'Hedef para birimi',
            'Faktör (kyn)', 'Faktör(hedef)'],axis=1)
    return dfTry
