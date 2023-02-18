import pandas as pd
from bigqueryApplication import BigqueryApp
import TablePrepApp as tb
import time
from SapVeriCekme import SapApp
import datetime as dt
import KurCevir as kr
def nanCevir(df):
    df=pd.DataFrame(df)
    df = df.replace("nan",None)
    df = df.replace("None",None)
    df = df.replace("NaT",None)
    print(df)
    return df

def tablo_duzenle():
    df_cji3 =tb.tb_cji3()
    df_ksb1n = tb.tb_ksb1n()
    df_fagll = tb.tb_fagll03()
    df_gelir = tb.tb_gelir()
    
    df = pd.concat([df_cji3,df_ksb1n,df_fagll,df_gelir])
    df = df.astype(str)


    return df
def sabitTabloBqAktar():
    df_at =tb.tb_aktiviteTuru()

    df_ah=tb.tb_anaHesap()

    df_eq=tb.tb_ekipman()

    df_ia=tb.tb_isAlani()
    df_mg=tb.tb_malGrubu()
    df_mlz=tb.tb_malzeme()
    df_mas=tb.tb_masrafCesidi()
    df_sir=tb.tb_sirket()
    dfLog = pd.read_excel(r"C:\Users\dataset_name13\Desktop\Gider Tabloları\LOG.xlsx")
    dfLog = pd.DataFrame(dfLog)
    dfLog = dfLog.append(pd.Series(["İndirilen Tablolar Düzenlendi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)

    bq = BigqueryApp()
    bq.bq_tablo_olustur("dataset_name","Aktivite_Turu")
    dfLog = dfLog.append(pd.Series(["Aktivite Türü Tablosu Oluşturuldu",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    bq.bq_veri_gonder("dataset_name","Aktivite_Turu",df_at)
    query = """create or replace table dataset_name.Aktivite_Turu as
    select distinct * from dataset_name.Aktivite_Turu"""
    bq.bq_veri_cek(query)
    time.sleep(7)

    bq.bq_tablo_olustur("dataset_name","ANA_HESAP")
    dfLog = dfLog.append(pd.Series(["Ana Hesap Tablosu Oluşturuldu",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    bq.bq_veri_gonder("dataset_name","ANA_HESAP",df_ah)
    query = """create or replace table dataset_name.ANA_HESAP as
    select distinct * from dataset_name.ANA_HESAP"""
    bq.bq_veri_cek(query)
    time.sleep(7)

    bq.bq_tablo_olustur("dataset_name","Ekipman_Listesi")
    dfLog = dfLog.append(pd.Series(["Ekipman Tablosu Oluşturuldu",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    bq.bq_veri_gonder("dataset_name","Ekipman_Listesi",df_eq)
    query = """create or replace table dataset_name.Ekipman_Listesi as
    select distinct * from dataset_name.Ekipman_Listesi"""
    bq.bq_veri_cek(query)
    time.sleep(7)

    bq.bq_tablo_olustur("dataset_name","Is_Alani")
    dfLog = dfLog.append(pd.Series(["İş Alanı Tablosu Oluşturuldu",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    bq.bq_veri_gonder("dataset_name","Is_Alani",df_ia)
    query = """create or replace table dataset_name.Is_Alani as
    select distinct * from dataset_name.Is_Alani"""
    bq.bq_veri_cek(query)
    time.sleep(7)

    bq.bq_tablo_olustur("dataset_name","Mal_Grubu")
    dfLog = dfLog.append(pd.Series(["Mal Grubu Tablosu Oluşturuldu",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    bq.bq_veri_gonder("dataset_name","Mal_Grubu",df_mg)
    query = """create or replace table dataset_name.Mal_Grubu as
    select distinct * from dataset_name.Mal_Grubu"""
    bq.bq_veri_cek(query)
    time.sleep(7)

    bq.bq_tablo_sil("dataset_name","Malzeme_Temp")
    bq.bq_tablo_olustur("dataset_name","Malzeme_Temp")
    dfLog = dfLog.append(pd.Series(["Malzeme Tablosu Oluşturuldu",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    bq.bq_veri_gonder("dataset_name","Malzeme_Temp",df_mlz)
    querym = """CREATE OR REPLACE TABLE
    dataset_name.Malzeme AS
    SELECT
    DISTINCT k.*,
    m.MAL_GRUBU_TANIMI_1,
    m.MAL_GRUBU_TANIMI_2
    FROM
    `dataset_name.Malzeme_Temp` k
    LEFT OUTER JOIN
    `dataset_name.Mal_Grubu` m
    ON
    k.MAL_GRUBU = m.MAL_GRUBU
    """
    bq.bq_veri_cek(querym)
    time.sleep(10)

    bq.bq_tablo_olustur("dataset_name","Masraf_Cesidi")
    dfLog = dfLog.append(pd.Series(["Masraf Çeşidi Tablosu Oluşturuldu",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    bq.bq_veri_gonder("dataset_name","Masraf_Cesidi",df_mas)
    query = """create or replace table dataset_name.Masraf_Cesidi as
    select distinct * from dataset_name.Masraf_Cesidi"""
    bq.bq_veri_cek(query)
    time.sleep(7)

    bq.bq_tablo_olustur("dataset_name","Sirket_Kodu")
    dfLog = dfLog.append(pd.Series(["Şirket Kodu Tablosu Oluşturuldu",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    bq.bq_veri_gonder("dataset_name","Sirket_Kodu",df_sir)
    query = """create or replace table dataset_name.Sirket_Kodu as
    select distinct * from dataset_name.Sirket_Kodu"""
    bq.bq_veri_cek(query)
    time.sleep(7)
    query2="""create or replace table dataset_name.Malzeme as

    select mz.*,mg.MAL_GRUBU_TANIMI_1 as MAL_GRUBU_TANIMI_1 from `dataset_name.Malzeme_Temp` mz

    left outer join `dataset_name.Mal_Grubu` mg

    on mz.MAL_GRUBU = mg.MAL_GRUBU"""
    bq.bq_veri_cek(query2)
    time.sleep(7)
def tablolariBqAktar():
    dfLog = pd.read_excel(r"C:\Users\dataset_name13\Desktop\Gider Tabloları\LOG.xlsx")
    dfLog = pd.DataFrame(dfLog)
    
    tableName="GelirGiderTemp"
    datasetName = "dataset_name"
    query= """CREATE OR REPLACE TABLE
  `dataset_name.GelirGider` AS
SELECT
  DISTINCT CAST(
  IF
    (k.KAYIT_TARIHI='nan',NULL,k.KAYIT_TARIHI) AS date) AS KAYIT_TARIHI,
  CONCAT(
  IF
    (k.IS_ALANI='nan',NULL,k.IS_ALANI),"-",i.IS_ALANI_TANIMI) AS IS_ALANI,
  CONCAT(
  IF
    (k.SIRKET_KODU='nan',NULL,k.SIRKET_KODU),"-",s.SIRKET_ADI) AS SIRKET_ADI,
IF
  (k.RAPOR_NO LIKE "FAGLL%",CONCAT(
    IF
      (k.MASRAF_CESIDI='nan',NULL,k.MASRAF_CESIDI),"-",a.ANA_HESAP_UZUN_METNI),CONCAT(
    IF
      (k.MASRAF_CESIDI='nan',NULL,k.MASRAF_CESIDI),"-",mas.MASRAF_CESIDI_TANIMI)) AS MASRAF_CESIDI,
  CAST(
  IF
    (k.DEGER_TRY='nan',NULL,k.DEGER_TRY) AS float64) AS DEGER_TRY,
IF
  (k.NESNE_PARA_BIRIMI='nan',NULL,k.NESNE_PARA_BIRIMI) AS NESNE_PARA_BIRIMI,
  CAST(
  IF
    (k.DEGER_EUR='nan',NULL,k.DEGER_EUR) AS float64) AS DEGER_EUR,
IF
  (k.KK_PARA_BIRIMI='nan',NULL,k.KK_PARA_BIRIMI) AS KK_PARA_BIRIMI,
  CONCAT(
  IF
    (k.MALZEME='nan',NULL,k.MALZEME),"-",m.MALZEME_KISA_METNI) AS MALZEME,
  m.MAL_GRUBU_TANIMI_1 AS MAL_GRUBU,
  CAST(
  IF
    (k.MIKTAR='nan',NULL,k.MIKTAR) AS float64) AS MIKTAR,
IF
  (k.OLCU_BIRIMI='nan',NULL,k.OLCU_BIRIMI) AS OLCU_BIRIMI,
  CONCAT(
  IF
    (k.BELGE_TURU='nan',NULL,k.BELGE_TURU),"-",b.BELGE_TURU_TANIMI) AS BELGE_TURU,
IF
  (k.DUZENLEYEN='nan',NULL,k.DUZENLEYEN) AS DUZENLEYEN,
IF
  (k.TERS_KAYDI_YAPILDI='nan',NULL,k.TERS_KAYDI_YAPILDI) AS TERS_KAYDI_YAPILDI,
IF
  (k.TERS_KAYIT_BELGESI='nan',NULL,k.TERS_KAYIT_BELGESI) AS TERS_KAYIT_BELGESI,
IF
  (k.BELGE_NUMARASI='nan',NULL,k.BELGE_NUMARASI) AS BELGE_NUMARASI,
IF
  (k.KAYIT_SATIRI='nan',NULL,k.KAYIT_SATIRI) AS KAYIT_SATIRI,
  CAST(
  IF
    (k.MALI_YIL='nan',NULL,k.MALI_YIL) AS int64) AS MALI_YIL,
  CAST(
  IF
    (k.DONEM='nan',NULL,k.DONEM) AS int64) AS DONEM,
IF
  (k.TANIM='nan',NULL,k.TANIM) AS TANIM,
IF
  (k.KARSIT_KAYIT_HESABI='nan',NULL,k.KARSIT_KAYIT_HESABI) AS KARSIT_KAYIT_HESABI,
  CASE
    WHEN k.GELIR_GIDER = 'GIDER' AND k.IS_ALANI IN ('1001', '2001', '3001', '4001', '5001', '5101', '5201', '5301', '5401', '5501', '5601', '5701', '9010', '9011', '9020', '9030') THEN 'MERKEZ GIDERI'
    WHEN k.GELIR_GIDER = 'GELIR'
  AND k.IS_ALANI IN ('1001',
    '2001',
    '3001',
    '4001',
    '5001',
    '5101',
    '5201',
    '5301',
    '5401',
    '5501',
    '5601',
    '5701',
    '9010',
    '9011',
    '9020',
    '9030') THEN 'MERKEZ GELIRI'
    WHEN k.GELIR_GIDER = 'GELIR' AND k.IS_ALANI NOT IN ('1001', '2001', '3001', '4001', '5001', '5101', '5201', '5301', '5401', '5501', '5601', '5701', '9010', '9011', '9020', '9030') THEN 'PROJE GELIRI'
    WHEN k.GELIR_GIDER = 'GIDER'
  AND k.IS_ALANI NOT IN ('1001',
    '2001',
    '3001',
    '4001',
    '5001',
    '5101',
    '5201',
    '5301',
    '5401',
    '5501',
    '5601',
    '5701',
    '9010',
    '9011',
    '9020',
    '9030') THEN 'PROJE GIDERI'
  ELSE
  k.GIDER_TURU
END
  AS GIDER_TURU,
IF
  (k.GELIR_GIDER='nan',NULL,k.GELIR_GIDER) AS GELIR_GIDER,
IF
  (k.RAPOR_NO='nan',NULL,k.RAPOR_NO) AS RAPOR_NO,
IF
  (k.SIPARIS='nan',NULL,k.SIPARIS) AS SIPARIS,
  CONCAT(
  IF
    (k.AKTIVITE_TURU='nan',NULL,k.AKTIVITE_TURU),"-",ak.AKTIVITE_TURU_TANIMI) AS AKTIVITE_TURU
FROM
  `dataset_name.GelirGiderTemp` k
LEFT OUTER JOIN
  `dataset_name.Is_Alani` i
ON
  k.IS_ALANI = i.IS_ALANI
LEFT OUTER JOIN
  `dataset_name.Sirket_Kodu` s
ON
  k.SIRKET_KODU = s.SIRKET_KODU
LEFT OUTER JOIN
  `dataset_name.Masraf_Cesidi` mas
ON
  k.MASRAF_CESIDI = mas.MASRAF_CESIDI
LEFT OUTER JOIN
  `dataset_name.Malzeme` m
ON
  k.MALZEME = m.MALZEME
LEFT OUTER JOIN
  `dataset_name.Belge_Turu` b
ON
  k.BELGE_TURU = b.BELGE_TURU
LEFT OUTER JOIN
  `dataset_name.ANA_HESAP` a
ON
  k.MASRAF_CESIDI = a.ANA_HESAP
LEFT OUTER JOIN
  `dataset_name.Aktivite_Turu` ak
ON
  k.AKTIVITE_TURU = ak.AKTIVITE_TURU
WHERE
  k.IS_ALANI NOT IN ("2007",
    "2014",
    "2016")
UNION ALL
SELECT
  DISTINCT CAST(
  IF
    (k.KAYIT_TARIHI='nan',NULL,k.KAYIT_TARIHI) AS date) AS KAYIT_TARIHI,
  CONCAT(
  IF
    (k.IS_ALANI='nan',NULL,k.IS_ALANI),"-",i.IS_ALANI_TANIMI) AS IS_ALANI,
  CONCAT(
  IF
    (k.SIRKET_KODU='nan',NULL,k.SIRKET_KODU),"-",s.SIRKET_ADI) AS SIRKET_ADI,
IF
  (k.RAPOR_NO LIKE "FAGLL%",CONCAT(
    IF
      (k.MASRAF_CESIDI='nan',NULL,k.MASRAF_CESIDI),"-",a.ANA_HESAP_UZUN_METNI),CONCAT(
    IF
      (k.MASRAF_CESIDI='nan',NULL,k.MASRAF_CESIDI),"-",mas.MASRAF_CESIDI_TANIMI)) AS MASRAF_CESIDI,
  CAST(
  IF
    (k.DEGER_TRY='nan',NULL,k.DEGER_TRY) AS float64) AS DEGER_TRY,
IF
  (k.NESNE_PARA_BIRIMI='nan',NULL,k.NESNE_PARA_BIRIMI) AS NESNE_PARA_BIRIMI,
  CAST(
  IF
    (k.DEGER_EUR='nan',NULL,k.DEGER_EUR) AS float64) AS DEGER_EUR,
IF
  (k.KK_PARA_BIRIMI='nan',NULL,k.KK_PARA_BIRIMI) AS KK_PARA_BIRIMI,
  CONCAT(
  IF
    (k.MALZEME='nan',NULL,k.MALZEME),"-",m.MALZEME_KISA_METNI) AS MALZEME,
  m.MAL_GRUBU_TANIMI_1 AS MAL_GRUBU,
  CAST(
  IF
    (k.MIKTAR='nan',NULL,k.MIKTAR) AS float64) AS MIKTAR,
IF
  (k.OLCU_BIRIMI='nan',NULL,k.OLCU_BIRIMI) AS OLCU_BIRIMI,
  CONCAT(
  IF
    (k.BELGE_TURU='nan',NULL,k.BELGE_TURU),"-",b.BELGE_TURU_TANIMI) AS BELGE_TURU,
IF
  (k.DUZENLEYEN='nan',NULL,k.DUZENLEYEN) AS DUZENLEYEN,
IF
  (k.TERS_KAYDI_YAPILDI='nan',NULL,k.TERS_KAYDI_YAPILDI) AS TERS_KAYDI_YAPILDI,
IF
  (k.TERS_KAYIT_BELGESI='nan',NULL,k.TERS_KAYIT_BELGESI) AS TERS_KAYIT_BELGESI,
IF
  (k.BELGE_NUMARASI='nan',NULL,k.BELGE_NUMARASI) AS BELGE_NUMARASI,
IF
  (k.KAYIT_SATIRI='nan',NULL,k.KAYIT_SATIRI) AS KAYIT_SATIRI,
  CAST(
  IF
    (k.MALI_YIL='nan',NULL,k.MALI_YIL) AS int64) AS MALI_YIL,
  CAST(
  IF
    (k.DONEM='nan',NULL,k.DONEM) AS int64) AS DONEM,
IF
  (k.TANIM='nan',NULL,k.TANIM) AS TANIM,
IF
  (k.KARSIT_KAYIT_HESABI='nan',NULL,k.KARSIT_KAYIT_HESABI) AS KARSIT_KAYIT_HESABI,
  CASE
    WHEN k.GELIR_GIDER = 'GIDER' AND k.IS_ALANI IN ('1001', '2001', '3001', '4001', '5001', '5101', '5201', '5301', '5401', '5501', '5601', '5701', '9010', '9011', '9020', '9030') THEN 'MERKEZ GIDERI'
    WHEN k.GELIR_GIDER = 'GELIR'
  AND k.IS_ALANI IN ('1001',
    '2001',
    '3001',
    '4001',
    '5001',
    '5101',
    '5201',
    '5301',
    '5401',
    '5501',
    '5601',
    '5701',
    '9010',
    '9011',
    '9020',
    '9030') THEN 'MERKEZ GELIRI'
    WHEN k.GELIR_GIDER = 'GELIR' AND k.IS_ALANI NOT IN ('1001', '2001', '3001', '4001', '5001', '5101', '5201', '5301', '5401', '5501', '5601', '5701', '9010', '9011', '9020', '9030') THEN 'PROJE GELIRI'
    WHEN k.GELIR_GIDER = 'GIDER'
  AND k.IS_ALANI NOT IN ('1001',
    '2001',
    '3001',
    '4001',
    '5001',
    '5101',
    '5201',
    '5301',
    '5401',
    '5501',
    '5601',
    '5701',
    '9010',
    '9011',
    '9020',
    '9030') THEN 'PROJE GIDERI'
  ELSE
  k.GIDER_TURU
END
  AS GIDER_TURU,
IF
  (k.GELIR_GIDER='nan',NULL,k.GELIR_GIDER) AS GELIR_GIDER,
IF
  (k.RAPOR_NO='nan',NULL,k.RAPOR_NO) AS RAPOR_NO,
IF
  (k.SIPARIS='nan',NULL,k.SIPARIS) AS SIPARIS,
  CONCAT(
  IF
    (k.AKTIVITE_TURU='nan',NULL,k.AKTIVITE_TURU),"-",ak.AKTIVITE_TURU_TANIMI) AS AKTIVITE_TURU
FROM
  `dataset_name.GelirGiderTemp` k
LEFT OUTER JOIN
  `dataset_name.Is_Alani` i
ON
  k.IS_ALANI = i.IS_ALANI
LEFT OUTER JOIN
  `dataset_name.Sirket_Kodu` s
ON
  k.SIRKET_KODU = s.SIRKET_KODU
LEFT OUTER JOIN
  `dataset_name.Masraf_Cesidi` mas
ON
  k.MASRAF_CESIDI = mas.MASRAF_CESIDI
LEFT OUTER JOIN
  `dataset_name.Malzeme` m
ON
  k.MALZEME = m.MALZEME
LEFT OUTER JOIN
  `dataset_name.Belge_Turu` b
ON
  k.BELGE_TURU = b.BELGE_TURU
LEFT OUTER JOIN
  `dataset_name.ANA_HESAP` a
ON
  k.MASRAF_CESIDI = a.ANA_HESAP
  
LEFT OUTER JOIN
  `dataset_name.Aktivite_Turu` ak
ON
  k.AKTIVITE_TURU = ak.AKTIVITE_TURU
WHERE
  ((k.IS_ALANI IN ("2007",
        "2014",
        "2016" ))
    AND k.GELIR_GIDER LIKE "GELIR"
    AND k.BELGE_TURU LIKE "DR")
  OR ((k.IS_ALANI IN ("2007",
        "2014",
        "2016" ))
    AND k.GELIR_GIDER LIKE "GIDER")"""
    queryRemoweDupTemp=f"""create or replace table {datasetName}.{tableName} as
    select distinct * from {datasetName}.{tableName} """
    #queryTruncMain=f"""truncate table {datasetName}.GelirGider"""
    bq = BigqueryApp()
    bq.bq_tablo_olustur(datasetName,tableName)
    dfLog = dfLog.append(pd.Series(["BQ Tablo Oluşturuldu",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    df = tablo_duzenle()
    dfLog = dfLog.append(pd.Series(["İndirilen Tablolar Düzenlendi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    

    
    df["IS_ALANI"] = df["IS_ALANI"].apply(lambda x: x.replace(".0", "") if isinstance(x, str) else x)
    
    
    df= df.drop_duplicates()
    dfLog = dfLog.append(pd.Series([f"Yinelenen Değerler Silindi Toplam Satır Sayısı: {len(df)}",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    bq.bq_veri_gonder(datasetName,tableName,df)
    dfLog = dfLog.append(pd.Series(["Gelir Gider Tablosu Bigquerye Başarıyla Gönderildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    bq.bq_veri_cek(queryRemoweDupTemp)
    time.sleep(20)
    #bq.bq_veri_cek(queryTruncMain)
    #time.sleep(20)
    bq.bq_veri_cek(query)
    time.sleep(40)
    dfLog = dfLog.append(pd.Series(["Bigquery deki Sorgular Tamamlandı",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    
    #------MB52------


    query_mb52 = """create or replace table dataset_name.STOK_TABLOSU as

select 
cast(MIKTAR as float64) as MIKTAR,
cast(DEGER_TRY as float64) as DEGER_TRY,
concat(k.MALZEME,"-",m.MALZEME_KISA_METNI) as MALZEME,
concat(k.IS_ALANI,"-",i.IS_ALANI_TANIMI) as IS_ALANI,
m.MAL_GRUBU_TANIMI_1 as MAL_GRUBU

from `dataset_name.STOK_TABLOSU_TEMP` k

left outer join `dataset_name.Is_Alani` i
on k.IS_ALANI = i.IS_ALANI

left outer join `dataset_name.Malzeme` m
on k.MALZEME =m.MALZEME"""



    df_mb52 = tb.tb_mb52()
    
    bq.bq_tablo_olustur(datasetName,"STOK_TABLOSU_TEMP")
    dfLog = dfLog.append(pd.Series(["Bigquery de Stok Tablosu Oluşturuldu",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    bq.bq_veri_gonder(datasetName,"STOK_TABLOSU_TEMP",df_mb52,"replace")
    dfLog = dfLog.append(pd.Series(["Bigquerye Stok Verileri Gönderildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    #query_trunc=f"truncate table {datasetName}.STOK_TABLOSU"
    #bq.bq_veri_cek(query_trunc)
    #time.sleep(5)
    bq.bq_veri_cek(query_mb52)
    dfLog = dfLog.append(pd.Series(["Bigquery de Stok Sorgusu Tamamlandı",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
    time.sleep(10)
    dfLog = dfLog.append(pd.Series(["Güncelleme İşlemi Başarıyla Gerçekleşti",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)

    dfLog =pd.DataFrame(dfLog)
    dfLog.to_excel(r"C:\Users\dataset_name13\Desktop\Gider Tabloları\LOG.xlsx",index=False)
def taseronHkTablolari():
    dfHk = pd.read_excel(r"C:\Users\dataset_name13\Desktop\Taşeron Hakedişi Tabloları\Hakedis.xlsx")
    dfKs = pd.read_excel(r"C:\Users\dataset_name13\Desktop\Taşeron Hakedişi Tabloları\Kesinti.xlsx")
    dfKr = pd.read_excel(r"C:\Users\dataset_name13\Desktop\Taşeron Hakedişi Tabloları\Kur.xlsx")
    dfHk["Geçerlilik bşl."] = pd.to_datetime(dfHk["Geçerlilik bşl."],format='%Y-%m-%d',errors='coerce')
    dfKr["Geçerlilik bşl."] = pd.to_datetime(dfKr["Geçerlilik bşl."],format='%d.%m.%Y')
    dfKs["Tarih"] = pd.to_datetime(dfKs["Tarih"],format='%Y-%m-%d',errors='coerce')

    dfHk =kr.kurKolonuEkle(dfHk,dfKr,"Geçerlilik bşl.","Geçerlilik bşl.","Para birimi")
    dfKs =kr.kurKolonuEkle(dfKs,dfKr,"Tarih","Geçerlilik bşl.","Para birimi")

    dfHkTop=tb.tb_ts_hakedis_toplam(dfHk)
    dfHkDty=tb.tb_ts_hakedis_detay(dfHk)
    dfHkKs=tb.tb_ts_hakedis_kesinti(dfKs)

    bq = BigqueryApp()
    queryTsList = """CREATE OR REPLACE TABLE
    dataset_name.TS_SOZ_LISTESI AS
  SELECT
    DISTINCT SATINALMA_BELGESI,
    AD
  FROM
    `dataset_name.TS_HK_TOPLAM`"""
    bq.bq_tablo_sil("dataset_name","TS_HK_TOPLAM")
    queryHkToplam = """CREATE OR REPLACE TABLE
    dataset_name.TS_HK_TOPLAM AS
  SELECT
    k.SATINALMA_BELGESI,
    k.KALEM,
    k.KISA_METIN,
    k.HAKEDIS_NO,
    k.SATIR_NO,
    k.SERVIS,
    k.KISA_METIN_2,
    k.PYP_OGESI,
    CONCAT(k.MAL_GRUBU,"-",k.MAL_GRUBU_TANIMI_2) AS MAL_GRUBU,
    k.HAKEDIS_TANIM,
    CONCAT(k.URETIM_YERI,"-",i.IS_ALANI_TANIMI) AS IS_ALANI,
    k.SATICI,
    k.AD,
    k.PARA_BIRIMI,
  IF
    (k.MASRAF_YERI = "nan",NULL,k.MASRAF_YERI) AS MASRAF_YERI,
    CAST(
    IF
      (k.GECERLILIK_BASLANGICI="NaT",NULL,k.GECERLILIK_BASLANGICI) AS Date) AS GECERLILIK_BASLANGICI,
    CAST(
    IF
      (k.GECERLILIK_SONU="NaT",NULL,k.GECERLILIK_SONU) AS Date) AS GECERLILIK_SONU,
    CAST(k.KDV_TUTAR AS float64) AS KDV_TUTARI,
    CAST(k.KDV_DAHIL_TOPLAM_TAHAKKUK_TUTARI AS float64) AS KDV_DAHIL_TOPLAM_TAHAKKUK_TUTARI,
    CAST(k.KESINTI_TUTARI AS float64) AS KESINTI_TUTARI,
    CAST(k.KDV_LI_KESINTI_TUTARI AS float64) AS KDVLI_KESINTI_TUTARI,
    CAST(k.ODENECEK_TUTAR AS float64) AS ODENECEK_TUTAR,
  IF
    (k.HAKEDIS_OLUSTURAN = "nan",NULL,k.HAKEDIS_OLUSTURAN) AS HAKEDIS_OLUSTURAN,
    ROUND(CAST(k.KUR_TO_TRY AS float64),4) AS KUR_TO_TRY,
    ROUND(CAST(k.KUR_TO_EUR AS float64),4) AS KUR_TO_EUR,
    CAST(
    IF
      (REGEXP_REPLACE(k.BEKLEME_SURESI," days","") = "NaT",NULL,REGEXP_REPLACE(k.BEKLEME_SURESI," days","")) AS int64) AS BEKLEME_SURESI,
    k.ONAY_GONDERIM_DURUMU,
    k.ONAY_DURUMU_ACIKLAMA,
    k.RAPOR_NO,
  FROM
    `dataset_name.TS_HK_TOPLAM` k
  LEFT OUTER JOIN
    `dataset_name.Is_Alani` i
  ON
    k.URETIM_YERI = i.IS_ALANI
  """
    bq.bq_tablo_olustur("dataset_name","TS_HK_TOPLAM")
    bq.bq_veri_gonder("dataset_name","TS_HK_TOPLAM",dfHkTop)
    bq.bq_veri_cek(queryTsList)
    time.sleep(10)
    bq.bq_veri_cek(queryHkToplam)
    time.sleep(15)
    bq.bq_tablo_sil("dataset_name","TS_HK_DETAY")
    queryHkDetay= """CREATE OR REPLACE TABLE
    dataset_name.TS_HK_DETAY AS
  SELECT
    k.SATINALMA_BELGESI,
    k.KALEM,
    k.KISA_METIN,
    k.HAKEDIS_NO,
    k.SATIR_NO,
    k.SERVIS,
    k.KISA_METIN_2,
    k.PYP_OGESI,
    CONCAT(k.MAL_GRUBU,"-",k.MAL_GRUBU_TANIMI_2) AS MAL_GRUBU,
    k.HAKEDIS_TANIM,
    CONCAT(k.URETIM_YERI,"-",i.IS_ALANI_TANIMI) AS IS_ALANI,
    k.SATICI,
    k.AD,
    k.PARA_BIRIMI,
  IF
    (k.MASRAF_YERI = "nan",NULL,k.MASRAF_YERI) AS MASRAF_YERI,
    CAST(
    IF
      (k.GECERLILIK_BASLANGICI="NaT",NULL,k.GECERLILIK_BASLANGICI) AS Date) AS GECERLILIK_BASLANGICI,
    CAST(
    IF
      (k.GECERLILIK_SONU="NaT",NULL,k.GECERLILIK_SONU) AS Date) AS GECERLILIK_SONU,
    CAST(k.ONCEKI_HAKEDIS_IMALAT_MIKTARI AS float64) AS ONCEKI_HK_IMALAT_MIKTARI,
    CAST(k.KUMULATIF_IMALAT_MIKTARI AS float64) AS KUMULATIF_IMALAT_MIKTARI,
    CAST(k.BU_HAKEDIS_IMALAT_MIKTARI AS float64) AS BU_HAKEDIS_IMALAT_MIKTARI,
    CAST(k.SOZLESME_TUTARI AS float64) AS SOZLESME_TUTARI,
    CAST(k.ONCEKI_HAKEDIS_TUTARI AS float64) AS ONCEKI_HAKEDIS_TUTARI,
    CAST(k.BU_HAKEDIS_IMALAT_TUTARI AS float64) AS BU_HAKEDIS_IMALAT_TUTARI,
    CAST(k.KUMULATIF_TUTAR AS float64) AS KUMULATIF_TUTAR,
  IF
    (k.HAKEDIS_OLUSTURAN = "nan",NULL,k.HAKEDIS_OLUSTURAN) AS HAKEDIS_OLUSTURAN,
    ROUND(CAST(
      IF
        (k.KUR_TO_TRY ="nan",NULL,k.KUR_TO_TRY) AS float64),4) AS KUR_TO_TRY,
    ROUND(CAST(
      IF
        (k.KUR_TO_EUR = "nan",NULL,k.KUR_TO_EUR) AS float64),4) AS KUR_TO_EUR,
    k.ONAY_GONDERIM_DURUMU,
    k.ONAY_DURUMU_ACIKLAMA,
    k.RAPOR_NO,
  FROM
    `dataset_name.TS_HK_DETAY` k
  LEFT OUTER JOIN
    `dataset_name.Is_Alani` i
  ON
    k.URETIM_YERI = i.IS_ALANI
  """
    bq.bq_tablo_olustur("dataset_name","TS_HK_DETAY")
    bq.bq_veri_gonder("dataset_name","TS_HK_DETAY",dfHkDty)
    bq.bq_veri_cek(queryHkDetay)
    time.sleep(10) 
    bq.bq_tablo_sil("dataset_name","TS_HK_KESINTI")
    queryHkKesinti = """CREATE OR REPLACE TABLE
    dataset_name.TS_HK_KESINTI AS
  SELECT
    CAST(
    IF
      (k.TARIH = "NaT",NULL,k.TARIH) AS date) AS TARIH,
    k.SATINALMA_BELGESI,
    ts.AD,
    k.HAKEDIS_NO,
    k.PARA_BIRIMI,
    CAST(k.KESINTI_TUTARI AS float64) AS KESINTI_TUTARI,
    CAST(k.KDV_LI_KESINTI_TUTARI AS float64) AS KDVLI_KESINTI_TUTARI,
    k.KESINTI_TANIMI,
  IF
    (k.ACIKLAMA = "nan",NULL,k.ACIKLAMA) AS ACIKLAMA,
    ROUND(CAST(
      IF
        (k.KUR_TO_TRY="nan",NULL,k.KUR_TO_TRY) AS float64),4) AS KUR_TO_TRY,
    ROUND(CAST(
      IF
        (k.KUR_TO_EUR="nan",NULL,k.KUR_TO_EUR) AS float64),4) AS KUR_TO_EUR,
    k.RAPOR_NO
  FROM
    `dataset_name.TS_HK_KESINTI` k
  LEFT OUTER JOIN
    dataset_name.TS_SOZ_LISTESI ts
  ON
    k.SATINALMA_BELGESI = ts.SATINALMA_BELGESI"""
    bq.bq_tablo_olustur("dataset_name","TS_HK_KESINTI")
    bq.bq_veri_gonder("dataset_name","TS_HK_KESINTI",dfHkKs) 
    bq.bq_veri_cek(queryHkKesinti)
    time.sleep(10)

def satinalmaTablolari():
    dfSt= pd.read_excel(r"C:\Users\dataset_name13\Desktop\Satınalma Tabloları\ME2N.xlsx")
    dfKr= pd.read_excel(r"C:\Users\dataset_name13\Desktop\Taşeron Hakedişi Tabloları\Kur.xlsx")
    dfOnay = pd.read_excel(r"C:\Users\dataset_name13\Desktop\Satınalma Tabloları\ZMM030.xlsx")
    dfOnaySat = pd.read_excel(r"C:\Users\dataset_name13\Desktop\Satınalma Tabloları\Sat Onay.xlsx")

    dfSt["Belge tarihi"] = pd.to_datetime(dfSt["Belge tarihi"],format='%Y-%m-%d',errors='coerce')
    dfKr["Geçerlilik bşl."] = pd.to_datetime(dfKr["Geçerlilik bşl."],format='%d.%m.%Y')


    dfSt =kr.kurKolonuEkle(dfSt,dfKr,"Belge tarihi","Geçerlilik bşl.","Para birimi")


    dfSt=tb.tb_me2n_satinalma(dfSt)
    dfOnay = tb.tb_zmm030_satinalma(dfOnay)

    df = dfOnay
    df1= pd.merge(dfSt,dfOnay,how="left",on="SATINALMA_BELGESI")
    dfs1 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_1"],"ONAY_SURESI": df["ONAY_SURESI_1"]})
    dfs2 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_2"],"ONAY_SURESI": df["ONAY_SURESI_2"]})
    dfs3 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_3"],"ONAY_SURESI": df["ONAY_SURESI_3"]})
    dfs4 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_4"],"ONAY_SURESI": df["ONAY_SURESI_4"]})
    dfs5 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_5"],"ONAY_SURESI": df["ONAY_SURESI_5"]})
    dfs6 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_6"],"ONAY_SURESI": df["ONAY_SURESI_6"]})
    dfs7 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_7"],"ONAY_SURESI": df["ONAY_SURESI_7"]})
    dfs8 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_8"],"ONAY_SURESI": df["ONAY_SURESI_8"]})

    dfs = pd.concat([dfs1,dfs2,dfs3,dfs4,dfs5,dfs6,dfs7,dfs8])

    dfs.dropna(inplace=True)

    #dfs['ONAY_SURESI'] = dfs['ONAY_SURESI'].apply(lambda x: x / pd.Timedelta(hours=1))

    dfs = dfs[dfs["ONAY_SURESI"] < 400]


    dfOnaySat = tb.tb_zmm030_satinalma_sat(dfOnaySat)

    df = dfOnaySat
    dfs1 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_1"],"ONAY_SURESI": df["ONAY_SURESI_1"]})
    dfs2 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_2"],"ONAY_SURESI": df["ONAY_SURESI_2"]})
    dfs3 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_3"],"ONAY_SURESI": df["ONAY_SURESI_3"]})
    dfs4 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_4"],"ONAY_SURESI": df["ONAY_SURESI_4"]})
    dfs5 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_5"],"ONAY_SURESI": df["ONAY_SURESI_5"]})
    dfs6 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_6"],"ONAY_SURESI": df["ONAY_SURESI_6"]})
    dfs7 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_7"],"ONAY_SURESI": df["ONAY_SURESI_7"]})
    dfs8 = pd.DataFrame({"YARATMA_TARIHI":df["YARATMA_TARIHI"],"ONAYCI": df["ONAYCI_8"],"ONAY_SURESI": df["ONAY_SURESI_8"]})

    dfsSat = pd.concat([dfs1,dfs2,dfs3,dfs4,dfs5,dfs6,dfs7,dfs8])

    dfsSat.dropna(inplace=True)

    #dfs['ONAY_SURESI'] = dfs['ONAY_SURESI'].apply(lambda x: x / pd.Timedelta(hours=1))

    dfsSat = dfsSat[dfsSat["ONAY_SURESI"] < 400]

    dfsSat = nanCevir(dfsSat)
    
    df1=df1.astype(str)
    df1 = nanCevir(df1)

    df_kullanici = pd.read_excel(r"C:\Users\dataset_name13\Desktop\Satınalma Tabloları\kullanıcı_sicil_eşleşme.xlsx")

    bq = BigqueryApp()
    bq.bq_tablo_sil("dataset_name","KULLANICI")
    time.sleep(3)
    bq.bq_tablo_olustur("dataset_name","KULLANICI")
    bq.bq_veri_gonder("dataset_name","KULLANICI",df_kullanici)

    query="""CREATE OR REPLACE TABLE
    dataset_name.SATINALMA AS
  SELECT
    DISTINCT k.* EXCEPT(FIYAT_BIRIMI,
      BELGE_TARIHI,
      URETIM_YERI,
      MAL_GRUBU,
      MALZEME,
      SA_SIPARISI_MIKTARI,
      NET_FIYAT,
      NET_SAS_DEGERI,
      TESLIMATI_YAPILACAK__MIKTAR_,
      TESLIMATI_YAPILACAK__DEGER_,
      HESAPLANACAK__MIKTAR_,
      HESAPLANACAK__DEGER_,
      TESLIMAT_FAZLASI_TOL,
      DEGISIKLIK_TARIHI,
      KUR_TO_EUR,
      KUR_TO_TRY),
  IF
    (k.BELGE_TARIHI="NaT",NULL,CAST(k.BELGE_TARIHI AS date)) AS BELGE_TARIHI,
    CONCAT(k.URETIM_YERI,"-",i.IS_ALANI_TANIMI) AS IS_ALANI,
    ml.MAL_GRUBU_TANIMI_1 AS MAL_GRUBU,
    CONCAT(k.MALZEME,"-",m.MALZEME_KISA_METNI) AS MALZEME,
    CAST(k.SA_SIPARISI_MIKTARI AS float64) AS SA_SIPARIS_MIKTARI,
    CAST(k.NET_FIYAT AS float64)/ cast(k.FIYAT_BIRIMI as float64) AS BIRIM_FIYAT,
    CAST(k.NET_SAS_DEGERI AS float64) AS NET_SAS_DEGERI,
    CAST(k.TESLIMATI_YAPILACAK__MIKTAR_ AS float64) AS TESLIMATI_YAPILACAK_MIKTAR,
    CAST(k.TESLIMATI_YAPILACAK__DEGER_ AS float64) AS TESLIMATI_YAPILACAK_DEGER,
    CAST(k.HESAPLANACAK__MIKTAR_ AS float64) AS HESAPLANACAK_MIKTAR,
    CAST(k.HESAPLANACAK__DEGER_ AS float64) AS HESAPLANACAK_DEGER,
    CAST(k.TESLIMAT_FAZLASI_TOL AS float64) AS TESLIMAT_FAZLASI_TOL,
  IF
    (k.DEGISIKLIK_TARIHI = "NaT",NULL,CAST(k.DEGISIKLIK_TARIHI AS date)) AS DEGISIKLIK_TARIHI,
    ROUND( CAST(k.KUR_TO_TRY AS float64),4) AS KUR_TO_TRY,
    ROUND(CAST(k.KUR_TO_EUR AS float64),4) AS KUR_TO_EUR,
  FROM
    `dataset_name.SATINALMA_TEMP` k
  LEFT OUTER JOIN
    `dataset_name.Is_Alani` i
  ON
    k.URETIM_YERI = i.IS_ALANI
  LEFT OUTER JOIN
    `dataset_name.Mal_Grubu` ml
  ON
    k.MAL_GRUBU = ml.MAL_GRUBU
  LEFT OUTER JOIN
    `dataset_name.Malzeme` m
  ON
    k.MALZEME = m.MALZEME"""
    bq.bq_tablo_sil("dataset_name","SATINALMA_TEMP")
    time.sleep(2)
    bq.bq_tablo_olustur("dataset_name","SATINALMA_TEMP")
    bq.bq_veri_gonder("dataset_name","SATINALMA_TEMP",df1)
    queryDup= """CREATE OR REPLACE TABLE
    dataset_name.SATINALMA_TEMP AS
  SELECT
    DISTINCT *
  FROM
    dataset_name.SATINALMA_TEMP"""
    bq.bq_veri_cek(queryDup)
    time.sleep(10)
    bq.bq_veri_cek(query)
    time.sleep(10)

    query_sas_onay="""CREATE OR REPLACE TABLE
  `dataset_name.SATINALMA_ONAY_TEMP` AS
SELECT
  k.* EXCEPT(ONAYCI),
IF
  (u.KULLANICI IS NULL,ONAYCI,u.KULLANICI) AS ONAYCI
FROM
  `dataset_name.SATINALMA_ONAY_TEMP` k
LEFT OUTER JOIN
  `dataset_name.KULLANICI` u
ON
  k.ONAYCI = u.PERSONEL_NUMARASI
WHERE
  ONAY_SURESI >0"""
    bq.bq_tablo_sil("dataset_name","SATINALMA_ONAY_TEMP")
    time.sleep(10)
    bq.bq_tablo_olustur("dataset_name","SATINALMA_ONAY_TEMP")
    bq.bq_veri_gonder("dataset_name","SATINALMA_ONAY_TEMP",dfs)
    bq.bq_veri_cek(query_sas_onay)
    time.sleep(5)

    query_sat_onay="""CREATE OR REPLACE TABLE
  `dataset_name.SAT_ONAY_TEMP` AS
SELECT
  k.* EXCEPT(ONAYCI),
IF
  (u.KULLANICI IS NULL,ONAYCI,u.KULLANICI) AS ONAYCI
FROM
  `dataset_name.SAT_ONAY_TEMP` k
LEFT OUTER JOIN
  `dataset_name.KULLANICI` u
ON
  k.ONAYCI = u.PERSONEL_NUMARASI
WHERE
  ONAY_SURESI >0"""
    bq.bq_tablo_sil("dataset_name","SAT_ONAY_TEMP")
    time.sleep(10)
    bq.bq_tablo_olustur("dataset_name","SAT_ONAY_TEMP")
    bq.bq_veri_gonder("dataset_name","SAT_ONAY_TEMP",dfsSat)
    bq.bq_veri_cek(query_sat_onay)
    time.sleep(5)    


def malzemeTablolari():
    df_mb51= pd.read_excel(r"C:\Users\dataset_name13\Desktop\Malzeme Tabloları\MB51.xlsx")
    df_me5a= pd.read_excel(r"C:\Users\dataset_name13\Desktop\Malzeme Tabloları\ME5A.xlsx")
    df_zpm007 = pd.read_excel(r"C:\Users\dataset_name13\Desktop\EKİPMAN TABLOLARI\ZPM007.xlsx")

    df_mb51= tb.tb_stok_giris_cikis_MB51(df_mb51)
    df_me5a = tb.tb_satinalma_talebi_ME5A(df_me5a)
    df_zpm007= tb.tb_bakim_onarim_ZPM007(df_zpm007)

    bq = BigqueryApp()
    query="""CREATE OR REPLACE TABLE
  dataset_name.STOK_HAREKETLERI AS
SELECT
  DISTINCT k.* EXCEPT(URETIM_YERI,
    MALZEME,
    SIRKET_KODU,
    GIRIS_SAATI,
    GIRIS_TARIHI,
    BELGE_TARIHI,
    KAYIT_TARIHI,
    MIKTAR,
    TUTAR__UPB_),
  CONCAT(k.URETIM_YERI,"-",i.IS_ALANI_TANIMI) AS IS_ALANI,
  CONCAT(k.MALZEME,"-",m.MALZEME_KISA_METNI) AS MALZEME,
  CONCAT(k.SIRKET_KODU,"-",s.SIRKET_ADI) AS SIRKET_ADI,
  CAST(k.GIRIS_TARIHI AS date) AS GIRIS_TARIHI,
  CAST(k.GIRIS_SAATI AS time) AS GIRIS_SAATI,
  CAST(k.BELGE_TARIHI AS date) AS BELGE_TARIHI,
  CAST(k.KAYIT_TARIHI AS date) AS KAYIT_TARIHI,
  CAST(k.MIKTAR AS float64) AS MIKTAR,
  CAST(k.TUTAR__UPB_ AS float64) AS TUTAR,
FROM
  `dataset_name.STOK_GIRIS_CIKIS_TEMP` k
LEFT OUTER JOIN
  `dataset_name.Is_Alani` i
ON
  k.URETIM_YERI = i.IS_ALANI
LEFT OUTER JOIN
  `dataset_name.Malzeme` m
ON
  k.MALZEME = m.MALZEME
LEFT OUTER JOIN
  `dataset_name.Sirket_Kodu` s
ON
  k.SIRKET_KODU = s.SIRKET_KODU"""
    bq.bq_tablo_olustur("dataset_name","STOK_GIRIS_CIKIS_TEMP")
    bq.bq_veri_gonder("dataset_name","STOK_GIRIS_CIKIS_TEMP",df_mb51)
    queryDup= """CREATE OR REPLACE TABLE
    dataset_name.STOK_GIRIS_CIKIS_TEMP AS
  SELECT
    DISTINCT *
  FROM
    dataset_name.STOK_GIRIS_CIKIS_TEMP"""
    bq.bq_veri_cek(queryDup)
    time.sleep(10)
    bq.bq_veri_cek(query)
    time.sleep(10)


    query_sat = """CREATE OR REPLACE TABLE
  `dataset_name.SAT_TABLOSU` AS
SELECT
  k.* EXCEPT(URETIM_YERI,
    MALZEME,
    SAS_TARIHI,
    TALEP_TARIHI,
    ONAY_TARIHI,
    TALEP_MIKTARI,
    SA_SPRS_MIKTARI),
  CONCAT(k.URETIM_YERI,"-",i.IS_ALANI_TANIMI) AS IS_ALANI,
  CONCAT(k.MALZEME,"-",m.MALZEME_KISA_METNI) AS MALZEME,
  CAST(k.SAS_TARIHI AS datetime) AS SAS_TARIHI,
  CAST(k.TALEP_TARIHI AS datetime) AS TALEP_TARIHI,
  CAST(k.ONAY_TARIHI AS datetime) AS ONAY_TARIHI,
  CAST(k.TALEP_MIKTARI AS float64) AS TALEP_MIKTARI,
  CAST(k.SA_SPRS_MIKTARI AS float64) AS SIPARIS_MIKTARI
FROM
  `dataset_name.SAT_TABLOSU` k
LEFT OUTER JOIN
  `dataset_name.Is_Alani` i
ON
  k.URETIM_YERI = i.IS_ALANI
LEFT OUTER JOIN
  `dataset_name.Malzeme` m
ON
  k.MALZEME = m.MALZEME"""
    
    bq.bq_tablo_sil("dataset_name","SAT_TABLOSU")
    time.sleep(10)
    bq.bq_tablo_olustur("dataset_name","SAT_TABLOSU")
    bq.bq_veri_gonder("dataset_name","SAT_TABLOSU",df_me5a)
    bq.bq_veri_cek(query_sat)
    time.sleep(10)

    query_zpm="""CREATE OR REPLACE TABLE
  `dataset_name.ZPM007` AS
SELECT
  k.* EXCEPT(IS_ALANI,
    PLANLAMA_URETIM_YERI,
    SIRKET_KODU,
    MASRAF_CESIDI,
    MALZEME,
    EKIPMAN,
    TOPLAM_OL_GRL_MIKTAR,
    KAYIT_TARIHI,
    DEGER_IPB,
    DEGER_KKPB),
  CONCAT(k.PLANLAMA_URETIM_YERI,"-",i.IS_ALANI_TANIMI) AS IS_ALANI,
  CONCAT(k.SIRKET_KODU,"-",s.SIRKET_ADI) AS SIRKET_ADI,
  CONCAT(k.MASRAF_CESIDI,"-",mas.MASRAF_CESIDI_TANIMI) AS MASRAF_CESIDI,
  CONCAT(k.MALZEME,"-",m.MALZEME_KISA_METNI) AS MALZEME,
  CONCAT(k.EKIPMAN,"-",e.TEKNIK_NESNE_TANIMI) AS EKIPMAN,
  CAST(TOPLAM_OL_GRL_MIKTAR AS float64) AS MIKTAR,
  CAST(KAYIT_TARIHI AS date) AS KAYIT_TARIHI,
  CAST(DEGER_KKPB AS float64) AS DEGER_EUR,
  CAST(DEGER_IPB AS float64) AS DEGER_IPB
FROM
  `dataset_name.ZPM007` k
LEFT OUTER JOIN
  `dataset_name.Is_Alani` i
ON
  k.PLANLAMA_URETIM_YERI = i.IS_ALANI
LEFT OUTER JOIN
  `dataset_name.Sirket_Kodu` s
ON
  k.SIRKET_KODU = s.SIRKET_KODU
LEFT OUTER JOIN
  `dataset_name.Masraf_Cesidi` mas
ON
  k.MASRAF_CESIDI = mas.MASRAF_CESIDI
LEFT OUTER JOIN
  `dataset_name.Malzeme` m
ON
  k.MALZEME = m.MALZEME
LEFT OUTER JOIN
  `dataset_name.Ekipman_Listesi` e
ON
  TRIM(k.EKIPMAN) = e.EKIPMAN"""
    bq.bq_tablo_sil("dataset_name","ZPM007")
    time.sleep(10)
    bq.bq_tablo_olustur("dataset_name","ZPM007")
    bq.bq_veri_gonder("dataset_name","ZPM007",df_zpm007)
    bq.bq_veri_cek(query_zpm)
    time.sleep(10)
def main():

    sp=SapApp()

    sp.sabitTablolariIndir()
    sabitTabloBqAktar()

    sp.gelirGiderTablolariIndir()
    tablolariBqAktar()

    sp.taseronHakedisTablolariIndir()
    taseronHkTablolari()

    sp.satinalmaSiparisTablolariIndir()
    satinalmaTablolari()

    sp.malzemeTablolariIndir()
    malzemeTablolari()
  



if __name__ == "__main__":
    main()
