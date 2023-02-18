import pandas as pd
import zaman_hesaplari as zm

def nanCevir(df):
    df=pd.DataFrame(df)
    df = df.replace("nan",None)
    df = df.replace("None",None)
    df = df.replace("NaT",None)
    return df

def tb_cji3():
    tbPath = r"C:\Users\klv13\Desktop\Gider Tabloları\CJI3.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb)

    df_tb = df_tb.rename(columns={'Kayıt tarihi':"KAYIT_TARIHI", 'İş alanı':"IS_ALANI", 'Şirket kodu': "SIRKET_KODU", 'Masraf çeşidi': "MASRAF_CESIDI",
        'Değer (nesne PB)':"DEGER_TRY", 'Nesne para birimi': "NESNE_PARA_BIRIMI", 'Değer/KKPB':"DEGER_EUR", 'KK para birimi': "KK_PARA_BIRIMI",
        'Malzeme': "MALZEME", 'Toplam ol.grl.miktar': "MIKTAR", 'Kaydedilen ölçü brm.': "OLCU_BIRIMI", 'Belge türü':"BELGE_TURU",
        'Kullanıcı adı':"DUZENLEYEN", 'Ters kaydı yapıldı':"TERS_KAYDI_YAPILDI", 'Ters kayıt belgesi':"TERS_KAYIT_BELGESI",
        'Belge numarası':"BELGE_NUMARASI", 'Kayıt satırı': "KAYIT_SATIRI", 'Mali yıl':"MALI_YIL", 'Dönem':"DONEM", 'Tanım':"TANIM",
        'Karşıt kayıt hesabı':"KARSIT_KAYIT_HESABI", 'Aktivite türü':"AKTIVITE_TURU", 'Yardmc.hesap tayini_1': "SIPARIS"})


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)



    df["RAPOR_NO"] = "CJI3"
    df["GELIR_GIDER"] = "GIDER"
    df["GIDER_TURU"] = ""


    #df.to_excel( r"C:\Users\klv13\Desktop\Gider Tabloları\tb3PANDAS.xlsx")
    df=nanCevir(df)
    return df

def tb_ksb1n():
    tbPath = r"C:\Users\klv13\Desktop\Gider Tabloları\KSB1N.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb)

    df_tb = df_tb.rename(columns={'Kayıt tarihi':"KAYIT_TARIHI", 'İş alanı':"IS_ALANI", 'Şirket kodu': "SIRKET_KODU", 'Masraf çeşidi': "MASRAF_CESIDI",
        'Değer (nesne PB)':"DEGER_TRY", 'Nesne para birimi': "NESNE_PARA_BIRIMI", 'Değer/KKPB':"DEGER_EUR", 'KK para birimi': "KK_PARA_BIRIMI",
        'Malzeme': "MALZEME", 'Toplam ol.grl.miktar': "MIKTAR", 'Kaydedilen ölçü brm.': "OLCU_BIRIMI", 'Belge türü':"BELGE_TURU",
        'Kullanıcı adı':"DUZENLEYEN", 'Ters kaydı yapıldı':"TERS_KAYDI_YAPILDI", 'Ters kayıt belgesi':"TERS_KAYIT_BELGESI",
        'Belge numarası':"BELGE_NUMARASI", 'Kayıt satırı': "KAYIT_SATIRI", 'Mali yıl':"MALI_YIL", 'Dönem':"DONEM", 'Tanım':"TANIM",
        'Karşıt kayıt hesabı':"KARSIT_KAYIT_HESABI", 'Aktivite türü':"AKTIVITE_TURU", 'Yardmc.hesap tayini_1': "SIPARIS"})


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)



    df["RAPOR_NO"] = "KSB1N"
    df["GELIR_GIDER"] = "GIDER"
    df["GIDER_TURU"] = ""

    df1 = df.loc[df["AKTIVITE_TURU"].notnull()]
    
    df2 = df.loc[df['SIPARIS'].notnull() & df['SIPARIS'].str.startswith("SPR")]
    #df2['SIPARIS'] = df2['SIPARIS'].astype(str)

    result = pd.concat([df1,df2])
    result=nanCevir(result)
    return result

def tb_fagll03():
    tbPath = r"C:\Users\klv13\Desktop\Gider Tabloları\FAGLL03.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb.columns)

    df_tb = df_tb.rename(columns={'Kayıt tarihi':"KAYIT_TARIHI", 'İş alanı':"IS_ALANI", 'Şirket kodu': "SIRKET_KODU", 'Ana hesap': "MASRAF_CESIDI",
        'UP cinsinden tutar':"DEGER_TRY", 'Ulusal para birimi': "NESNE_PARA_BIRIMI", 'Şirketler topluluğu PB':"DEGER_EUR", 'CurrŞirket': "KK_PARA_BIRIMI",
        'Malzeme': "MALZEME", 'Miktar': "MIKTAR", 'Temel ölçü birimi': "OLCU_BIRIMI", 'Belge türü':"BELGE_TURU",
        'Düzenleyen':"DUZENLEYEN", 'Curr':"TERS_KAYDI_YAPILDI", 'Ters kayıt blg.no.':"TERS_KAYIT_BELGESI",
        'Belge numarası':"BELGE_NUMARASI", 'Defteri kebir kalemi': "KAYIT_SATIRI", 'Mali yıl':"MALI_YIL", 'Kayıt dönemi':"DONEM", 'Kısa metin':"TANIM",
        'Karşıt kayıt hesabı':"KARSIT_KAYIT_HESABI", 'Aktivite türü':"AKTIVITE_TURU", 'Yardmc.hesap tayini_1': "SIPARIS"})


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)


    df["SIPARIS"] = ""
    df["RAPOR_NO"] = "FAGLL03"
    df["GELIR_GIDER"] = "GIDER"
    df["GIDER_TURU"] = ""
    df= nanCevir(df)
    return df

def tb_gelir():
    tbPath = r"C:\Users\klv13\Desktop\Gider Tabloları\GELIR.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb.columns)

    df_tb = df_tb.rename(columns={'Kayıt tarihi':"KAYIT_TARIHI", 'İş alanı':"IS_ALANI", 'Şirket kodu': "SIRKET_KODU", 'Ana hesap': "MASRAF_CESIDI",
        'UP cinsinden tutar':"DEGER_TRY", 'Ulusal para birimi': "NESNE_PARA_BIRIMI", 'Şirketler topluluğu PB':"DEGER_EUR", 'CurrŞirket': "KK_PARA_BIRIMI",
        'Malzeme': "MALZEME", 'Miktar': "MIKTAR", 'Temel ölçü birimi': "OLCU_BIRIMI", 'Belge türü':"BELGE_TURU",
        'Düzenleyen':"DUZENLEYEN", 'Curr':"TERS_KAYDI_YAPILDI", 'Ters kayıt blg.no.':"TERS_KAYIT_BELGESI",
        'Belge numarası':"BELGE_NUMARASI", 'Defteri kebir kalemi': "KAYIT_SATIRI", 'Mali yıl':"MALI_YIL", 'Kayıt dönemi':"DONEM", 'Kısa metin':"TANIM",
        'Karşıt kayıt hesabı':"KARSIT_KAYIT_HESABI", 'Aktivite türü':"AKTIVITE_TURU", 'Yardmc.hesap tayini_1': "SIPARIS"})


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)

    df["DEGER_TRY"] = df["DEGER_TRY"] * -1
    df["DEGER_EUR"] = df["DEGER_EUR"] * -1
    df["SIPARIS"] = ""
    df["RAPOR_NO"] = "FAGLL03"
    df["GELIR_GIDER"] = "GELIR"
    df["GIDER_TURU"] = ""
    df=nanCevir(df)
    return df

def tb_mb52():
    tbPath = r"C:\Users\klv13\Desktop\Gider Tabloları\MB52.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb.columns)

    df_tb = df_tb.rename(columns={'Malzeme':"MALZEME", 'Üretim yeri':"IS_ALANI",  'Tahditsiz klnb.': "MIKTAR",
        'Değer thds.klnb.':"DEGER_TRY", 'Para birimi': "PARA_BIRIMI",  'Temel ölçü birimi': "OLCU_BIRIMI",})


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)

    
    df["RAPOR_NO"] = "MB52"

    df=df.astype(str)

    df=nanCevir(df)
    return df

def tb_anaHesap():
    tbPath = r"C:\Users\klv13\Desktop\Sabit Tablolar\Ana Hesap.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb.columns)

    df_tb = df_tb.rename(columns={'Hesap planı':"HESAP_PLANI", 'Ana hesap':"ANA_HESAP",  'Yaratma tarihi': "YARATMA_TARIHI",
        'Yaratan':"YARATAN", 'Hesap grubu': "HESAP_GRUBU",  'Kısa metin': "KISA_METIN", "Ana hesap uzun metni":"ANA_HESAP_UZUN_METNI","Zaman damgası":"ZAMAN_DAMGASI"})


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)

    
    df["RAPOR_NO"] = "SKA1"

    df=df.astype(str)

    df=nanCevir(df)
    return df

def tb_aktiviteTuru():
    tbPath = r"C:\Users\klv13\Desktop\Sabit Tablolar\Aktivite Türü.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb.columns)

    df_tb = df_tb.rename(columns={'Aktivite türü':"AKTIVITE_TURU", 'Tanım':"AKTIVITE_TURU_TANIMI"})


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)

    
    df["RAPOR_NO"] = "CSLA"

    df=df.astype(str)

    df=nanCevir(df)
    return df

def tb_isAlani():
    tbPath = r"C:\Users\klv13\Desktop\Sabit Tablolar\İş Alanı.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb.columns)

    df_tb = df_tb.rename(columns={'İş alanı':"IS_ALANI", 'İş alanı tanımı':"IS_ALANI_TANIMI"})


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)

    
    df["RAPOR_NO"] = "TGSBT"

    df=df.astype(str)

    df=nanCevir(df)
    return df

def tb_masrafCesidi():
    tbPath = r"C:\Users\klv13\Desktop\Sabit Tablolar\Masraf Çeşidi.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb.columns)

    df_tb = df_tb.rename(columns={'Masraf çeşidi':"MASRAF_CESIDI", 'Tanım':"MASRAF_CESIDI_TANIMI"})


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)

    
    df["RAPOR_NO"] = "CSKA"

    df=df.astype(str)

    df=nanCevir(df)
    return df

def tb_malGrubu():
    tbPath = r"C:\Users\klv13\Desktop\Sabit Tablolar\Mal Grubu.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb.columns)

    df_tb = df_tb.rename(columns={'Mal grubu':"MAL_GRUBU", 'Mal grubu tanımı':"MAL_GRUBU_TANIMI_1", 'Mal grubu tanımı 2':"MAL_GRUBU_TANIMI_2"})


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)

    
    df["RAPOR_NO"] = "T023"

    df=df.astype(str)

    df=nanCevir(df)
    return df

def tb_malzeme():
    tbPath = r"C:\Users\klv13\Desktop\Sabit Tablolar\Malzeme.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb.columns)

    df_tb = df_tb.rename(columns={'Malzeme':"MALZEME", 'Malzeme kısa metni':"MALZEME_KISA_METNI",
     'Malzeme türü':"MALZEME_TURU", "Mal grubu":"MAL_GRUBU","Temel ölçü birimi":"OLCU_BIRIMI",
     "SAS ölçü birimi":"SAS_OLCU_BIRIMI","Yaratma tarihi":"YARATMA_TARIHI","Oluşturma saati":"OLUSTURMA_SAATI",
     "Yaratıldı":"YARATAN","Son değişiklik":"SON_DEGISIKLIK","Değiştiren":"DUZENLEYEN","Tüm mlz.bakım durumu":"TUM_MLZ_BAKIM_DURUMU",
     "Bakım durumu":"BAKIM_DURUMU","ÜB dzy.silme iştr.":"DUZEY_SILME_ISARETI","Ürün":"URUN","Ürün tanıtıcısı":"URUN_TANITICISI"
    })


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)

    
    df["RAPOR_NO"] = "MARA"

    df=df.astype(str)

    df=nanCevir(df)
    return df

def tb_sirket():
    tbPath = r"C:\Users\klv13\Desktop\Sabit Tablolar\Şirket.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb.columns)

    df_tb = df_tb.rename(columns={'Şirket kodu':"SIRKET_KODU", 'Şirket adı':"SIRKET_ADI", 'Kent':"SEHIR"})


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)

    
    df["RAPOR_NO"] = "T001"

    df=df.astype(str)

    df=nanCevir(df)
    return df

def tb_ekipman():
    tbPath = r"C:\Users\klv13\Desktop\Sabit Tablolar\Ekipman.xlsx"
    df_tb = pd.read_excel(tbPath)

    #print(df_tb.columns)

    df_tb = df_tb.rename(columns={'Ekipman':"EKIPMAN", 'Aktivite türü':"AKTIVITE_TURU", 'Nesne türü':"NESNE_TURU",
    "Teknik Nesne Türü":"TEKNIK_NESNE_TURU","Teknik nesne tanımı":"TEKNIK_NESNE_TANIMI","Tip tanımı":"TIP_TANIMI",
    "Duran varlık üreticisi":"DURAN_VARLIK_URETICISI","Yapım yılı":"YAPIM_YILI","Yaratma tarihi":"YARATMA_TARIHI",
    "Yaratıldı":"YARATAN","Oturum dili":"OTURUM_DILI","Değişiklik tarihi":"DEGISIKLIK_TARIHI","Değiştiren":"DUZENLEYEN",
    "Yetki grubu":"YETKI_GRUBU", "Ekipman tipi":"EKIPMAN_TIPI","Not":"NOT","Nesne numarası":"NESNE_NUMARASI","Yetki grubu kaynağı":"YETKI_GRUBU_KAYNAGI",
    "Ekipman vr.mevcut":"EKIPMAN_VR_MEVCUT","Taşıt verileri":"TASIT_VERILERI","Kısa şekliyle zm.damgası":"KISA_SEKLIYLE_ZAMAN_DAMGASI",
    "Ruhsat Sahibi":"RUHSAT_SAHIBI","Mal Sahibi":"MAL_SAHIBI","Makine Durumu":"MAKINE_DURUMU","Ruhsat Seri No":"RUHSAT_SERI_NO",
    "Taşıt Takip Sistem Adı":"TASIT_TAKIP_SISTEMI_ADI","Taşıt Takip Cihaz IMEI No":"TASIT_TAKIP_CIHAZ_IMEI_NO",
    "Leasing Bitiş Tarihi":"LEASING_BITIS_TARIHI","Poliçe No":"POLICE_NO","Başlangıç Tarihi":"BASLANGIC_TARIHI",
    "Bitiş Tarihi":"BITIS_TARIHI","Prim Tutarı":"PRIM_TUTARI","Acenta Bilgisi":"ACENTA_BILGISI"    
    })


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)

    
    df["RAPOR_NO"] = "EQUI"

    df=df.astype(str)

    df=nanCevir(df)
    return df

def tb_ts_hakedis_toplam(df_tb):


    df_tb = df_tb.rename(columns={'Satınalma belgesi':"SATINALMA_BELGESI", 'Kalem':"KALEM", 'Kısa metin':"KISA_METIN",
     'Hakediş No':"HAKEDIS_NO",
       'Satır numarası':"SATIR_NO", 'Servis':"SERVIS", 'Kısa metin.1':"KISA_METIN_2", 'PYP öğesi':"PYP_OGESI",
        'Masraf yeri':"MASRAF_YERI",
       'Mal grubu':"MAL_GRUBU", 'Mal grubu tanımı 2':"MAL_GRUBU_TANIMI_2", 'Hakediş Tanım':"HAKEDIS_TANIM",
        'Geçerlilik bşl.':"GECERLILIK_BASLANGICI",
       'Geçerlilik sonu':"GECERLILIK_SONU", 'Üretim yeri':"URETIM_YERI", 'Satıcı':"SATICI", 'Ad 1':"AD", 'Para birimi':"PARA_BIRIMI",
       'ÖNCEKİ HAKEDİŞ İMALAT MİKTARI':"ONCEKI_HAKEDIS_IMALAT_MIKTARI", 'KÜMÜLATİF İMALAT MİKTARI':"KUMULATIF_IMALAT_MIKTARI",
       'Bu Hakediş İmalat Miktarı':"BU_HAKEDIS_IMALAT_MIKTARI", 'Sözleşme Tutarı':"SOZLESME_TUTARI", 'Önceki Hakediş Tutarı':"ONCEKI_HAKEDIS_TUTARI",
       'Bu Hakediş İmalat Tutarı':"BU_HAKEDIS_IMALAT_TUTARI", 'KÜMÜLATİF TUTAR':"KUMULATIF_TUTAR", 'KDV Tutar':"KDV_TUTAR",
       'KDV Dahil Toplam Tahakkuk Tutarı':"KDV_DAHIL_TOPLAM_TAHAKKUK_TUTARI", 'Kesinti Tutar':"KESINTI_TUTARI",
       "KDV'li Kesinti Tutar":"KDV_LI_KESINTI_TUTARI", 'Ödenecek Tutar':"ODENECEK_TUTAR", 'Temel ölçü birimi':"OLCU_BIRIMI",
       'Hakediş Oluşturan':"HAKEDIS_OLUSTURAN", 'Onay Gönderim Durumu':"ONAY_GONDERIM_DURUMU", 'Belge durumu':"BELGE_DURUMU",
       'Onay Durumu Açıklama':"ONAY_DURUMU_ACIKLAMA", 'Kur_toTry':"KUR_TO_TRY", 'Kur_toEur':"KUR_TO_EUR"    
    })


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)
    df["RAPOR_NO"] = "ZMM032H"
    
    df=df[(df["KDV_DAHIL_TOPLAM_TAHAKKUK_TUTARI"] != 0)]

    df["BEKLEME_SURESI"] = df["GECERLILIK_SONU"] - df["GECERLILIK_BASLANGICI"]
    

    df= df.drop(["ONCEKI_HAKEDIS_IMALAT_MIKTARI","KUMULATIF_IMALAT_MIKTARI","BU_HAKEDIS_IMALAT_MIKTARI","SOZLESME_TUTARI","ONCEKI_HAKEDIS_TUTARI",
    "BU_HAKEDIS_IMALAT_TUTARI","KUMULATIF_TUTAR","OLCU_BIRIMI"
    ],axis=1)

    df=df.astype(str)
    df=nanCevir(df)
    return df


def tb_ts_hakedis_detay(df_tb):


    df_tb = df_tb.rename(columns={'Satınalma belgesi':"SATINALMA_BELGESI", 'Kalem':"KALEM", 'Kısa metin':"KISA_METIN",
     'Hakediş No':"HAKEDIS_NO",
       'Satır numarası':"SATIR_NO", 'Servis':"SERVIS", 'Kısa metin.1':"KISA_METIN_2", 'PYP öğesi':"PYP_OGESI",
        'Masraf yeri':"MASRAF_YERI",
       'Mal grubu':"MAL_GRUBU", 'Mal grubu tanımı 2':"MAL_GRUBU_TANIMI_2", 'Hakediş Tanım':"HAKEDIS_TANIM",
        'Geçerlilik bşl.':"GECERLILIK_BASLANGICI",
       'Geçerlilik sonu':"GECERLILIK_SONU", 'Üretim yeri':"URETIM_YERI", 'Satıcı':"SATICI", 'Ad 1':"AD", 'Para birimi':"PARA_BIRIMI",
       'ÖNCEKİ HAKEDİŞ İMALAT MİKTARI':"ONCEKI_HAKEDIS_IMALAT_MIKTARI", 'KÜMÜLATİF İMALAT MİKTARI':"KUMULATIF_IMALAT_MIKTARI",
       'Bu Hakediş İmalat Miktarı':"BU_HAKEDIS_IMALAT_MIKTARI", 'Sözleşme Tutarı':"SOZLESME_TUTARI", 'Önceki Hakediş Tutarı':"ONCEKI_HAKEDIS_TUTARI",
       'Bu Hakediş İmalat Tutarı':"BU_HAKEDIS_IMALAT_TUTARI", 'KÜMÜLATİF TUTAR':"KUMULATIF_TUTAR", 'KDV Tutar':"KDV_TUTAR",
       'KDV Dahil Toplam Tahakkuk Tutarı':"KDV_DAHIL_TOPLAM_TAHAKKUK_TUTARI", 'Kesinti Tutar':"KESINTI_TUTARI",
       "KDV'li Kesinti Tutar":"KDV_LI_KESINTI_TUTARI", 'Ödenecek Tutar':"ODENECEK_TUTAR", 'Temel ölçü birimi':"OLCU_BIRIMI",
       'Hakediş Oluşturan':"HAKEDIS_OLUSTURAN", 'Onay Gönderim Durumu':"ONAY_GONDERIM_DURUMU", 'Belge durumu':"BELGE_DURUMU",
       'Onay Durumu Açıklama':"ONAY_DURUMU_ACIKLAMA", 'Kur_toTry':"KUR_TO_TRY", 'Kur_toEur':"KUR_TO_EUR"    
    })


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)
    df["RAPOR_NO"] = "ZMM032H"
    
    df= df.drop(["KDV_TUTAR","KDV_DAHIL_TOPLAM_TAHAKKUK_TUTARI","KESINTI_TUTARI",
    "KDV_LI_KESINTI_TUTARI","ODENECEK_TUTAR"
    ],axis=1)

    #df["BEKLEME_SURESI"] = df["Geçerlilik sonu"] - df["Geçerlilik bşl."]

    df=df.astype(str)

    df=nanCevir(df)
    return df

def tb_ts_hakedis_kesinti(df_tb):


    df_tb = df_tb.rename(columns={'Tarih':"TARIH", 'Satınalma belgesi':"SATINALMA_BELGESI", 'Hakediş No':"HAKEDIS_NO", 'Para birimi':"PARA_BIRIMI",
       'Kesinti Tutar':"KESINTI_TUTARI", "KDV'li Kesinti Tutar":"KDV_LI_KESINTI_TUTARI", 'Kesinti Tanım':"KESINTI_TANIMI", 'Açıklama':"ACIKLAMA",
       'Kur_toTry':"KUR_TO_TRY", 'Kur_toEur':"KUR_TO_EUR"  
    })


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)
    df["RAPOR_NO"] = "ZMM032K"
    
    


    #df["BEKLEME_SURESI"] = df["Geçerlilik sonu"] - df["Geçerlilik bşl."]

    df=df.astype(str)

    df=nanCevir(df)
    return df




def tb_me2n_satinalma(df_tb):


    df_tb = df_tb.rename(columns={'Silme göstergesi':"SILME_GOSTERGESI", 'Yaratıldı':"YARATILDI", 'Onay göstergesi':"ONAY_GOSTERGESI",
     'Onay durumu':"ONAY_DURUMU",
       'Onay stratejisi':"ONAY_STRATEJISI", 'Onay grubu':"ONAY_GRUBU", 'Satınalma belgesi':"SATINALMA_BELGESI", 'Tamamlanmadı':"TAMAMLANMADI",
        'Kalem':"KALEM",
       'Hesap tayini tipi':"HESAP_TAYINI_TIPI", 'SA belgesi türü':"SA_BELGESI_TURU", 'Satınalma belgesi tp':"SATINALMA_BELGESI_TP",
        'Satınalma grubu':"SATINALMA_GRUBU",
       'Belge tarihi':"BELGE_TARIHI", 'Üretim yeri':"URETIM_YERI", 'Depo yeri':"DEPO_YERI", 'Satıcı/teslimat yapan ürt.yeri':"SATICI_TESLIMAT_YAPAN_URT_YERI", 'Mal grubu':"MAL_GRUBU",
       'Malzeme':"MALZEME", 'Kısa metin':"KISA_METIN",
       'SA siparişi miktarı':"SA_SIPARISI_MIKTARI", 'SAS ölçü birimi':"SAS_OLCU_BIRIMI", 'Fiyat birimi':"FIYAT_BIRIMI",
       'SAS fiyatı ölçü brm.':"SAS_FIYATI_OLCU_BRM_", 'Net fiyat':"NET_FIYAT", 'Net SAS değeri':"NET_SAS_DEGERI",
       'Para birimi':"PARA_BIRIMI", 'Teslimatı yapılacak (miktar)':"TESLIMATI_YAPILACAK__MIKTAR_",
       "Teslimatı yapılacak (değer)":"TESLIMATI_YAPILACAK__DEGER_", 'Hesaplanacak (miktar)':"HESAPLANACAK__MIKTAR_", 'Hesaplanacak (değer)':"HESAPLANACAK__DEGER_",
       'Teslimat fazlası tol':"TESLIMAT_FAZLASI_TOL", 'Ödeme biçimi metni':"ODEME_BICIMI_METNI", 'Mal grubu tanımı':"MAL_GRUBU_TANIMI",
       'Ödeme koşulu':"ODEME_KOSULU", 'ÖdKş tanımı':"ODKS_TANIMI", 'SA bilgi kaydı':"SA_BILGI_KAYDI", "Satınalma Belgesi Başlık Metni":"SATINALMA_BELGESI_BASLIK_METNI",
        "Değişiklik tarihi" : "DEGISIKLIK_TARIHI",'Kur_toTry':"KUR_TO_TRY", 'Kur_toEur':"KUR_TO_EUR"
    })

    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)
    df["RAPOR_NO"] = "ME2N"
    


    """for index, row in df.iterrows():
        if row["SAS_FIYATI_OLCU_BRM_"] == "KG" and row["SAS_OLCU_BIRIMI"] == "TON":
            df.at[index, "SAS_OLCU_BIRIMI"] = "KG"
            df.at[index, "SA_SIPARISI_MIKTARI"] = row["SA_SIPARISI_MIKTARI"] * 1000

    for index, row in df.iterrows():
        if row["SAS_FIYATI_OLCU_BRM_"] == "TON" and row["SAS_OLCU_BIRIMI"] == "KG":
            df.at[index, "SAS_OLCU_BIRIMI"] = "TON"
            df.at[index, "SA_SIPARISI_MIKTARI"] = row["SA_SIPARISI_MIKTARI"] / 1000"""  

    mask = (df["SAS_FIYATI_OLCU_BRM_"] == "KG") & (df["SAS_OLCU_BIRIMI"] == "TON")

# SAS_OLCU_BIRIMI sütununun seçilen satırlardaki değerlerini "KG" ile değiştir
    df.loc[mask, "SAS_OLCU_BIRIMI"] = "KG"

# SA_SIPARISI_MIKTARI sütununun seçilen satırlardaki değerlerini 1000 ile çarp
    df.loc[mask, "SA_SIPARISI_MIKTARI"] *= 1000


    mask = (df["SAS_FIYATI_OLCU_BRM_"] == "TON") & (df["SAS_OLCU_BIRIMI"] == "KG")

# SAS_OLCU_BIRIMI sütununun seçilen satırlardaki değerlerini "KG" ile değiştir
    df.loc[mask, "SAS_OLCU_BIRIMI"] = "TON"

# SA_SIPARISI_MIKTARI sütununun seçilen satırlardaki değerlerini 1000 ile çarp
    df.loc[mask, "SA_SIPARISI_MIKTARI"] /= 1000

    #df["BEKLEME_SURESI"] = df["Geçerlilik sonu"] - df["Geçerlilik bşl."]
    
    df=df.astype(str)

    nanCevir(df)
    return df

def tb_zmm030_satinalma(df):


    df = df.rename(columns={'Satınalma belgesi':"SATINALMA_BELGESI", 'Yaratıldı':"YARATILDI", 'Yaratma tarihi':"YARATMA_TARIHI",
     'Onay durumu':"ONAY_DURUMU",
       'Üretim yeri':"URETIM_YERI", 'Başlık Metni':"BASLIK_METNI", 'Son İşlem Tarihi':"SON_ISLEM_TARIHI", 'Toplam Beklediği Gün':"TOPLAM_BEKLEDIGI_GUN",
        '1. Onaycı':"ONAYCI_1", "1. Onay Tarihi":"ONAY_TARIHI_1", "1. Onay Saati":"ONAY_SAATI_1",
        '2. Onaycı':"ONAYCI_2","2. Onay Tarihi":"ONAY_TARIHI_2", "2. Onay Saati":"ONAY_SAATI_2",
       '3. Onaycı':"ONAYCI_3","3. Onay Tarihi":"ONAY_TARIHI_3", "3. Onay Saati":"ONAY_SAATI_3",
        '4. Onaycı':"ONAYCI_4","4. Onay Tarihi":"ONAY_TARIHI_4", "4. Onay Saati":"ONAY_SAATI_4",
         '5. Onaycı':"ONAYCI_5","5. Onay Tarihi":"ONAY_TARIHI_5", "5. Onay Saati":"ONAY_SAATI_5",
          '6. Onaycı':"ONAYCI_6","6. Onay Tarihi":"ONAY_TARIHI_6", "6. Onay Saati":"ONAY_SAATI_6",
           '7. Onaycı':"ONAYCI_7","7. Onay Tarihi":"ONAY_TARIHI_7", "7. Onay Saati":"ONAY_SAATI_7",
       '8. Onaycı':"ONAYCI_8", "8. Onay Tarihi":"ONAY_TARIHI_8", "8. Onay Saati":"ONAY_SAATI_8"
    })

    df["TOPLAM_BEKLEDIGI_GUN"] = df["SON_ISLEM_TARIHI"] - df["YARATMA_TARIHI"]

    df=df.drop(["YARATILDI","URETIM_YERI","BASLIK_METNI"],axis=1)

    df = df.astype(str)
    df["YARATMA_TARIHI"] = pd.to_datetime(df["YARATMA_TARIHI"] + " " + "09:00:00",errors="coerce")
    df["ONAY_TARIHI_1"]= pd.to_datetime(df["ONAY_TARIHI_1"] + " " + df["ONAY_SAATI_1"],errors="coerce")
    df["ONAY_TARIHI_2"]= pd.to_datetime(df["ONAY_TARIHI_2"] + " " + df["ONAY_SAATI_2"],errors="coerce")
    df["ONAY_TARIHI_3"]= pd.to_datetime(df["ONAY_TARIHI_3"] + " " + df["ONAY_SAATI_3"],errors="coerce")
    df["ONAY_TARIHI_4"]= pd.to_datetime(df["ONAY_TARIHI_4"] + " " + df["ONAY_SAATI_4"],errors="coerce")
    df["ONAY_TARIHI_5"]= pd.to_datetime(df["ONAY_TARIHI_5"] + " " + df["ONAY_SAATI_5"],errors="coerce")
    df["ONAY_TARIHI_6"]= pd.to_datetime(df["ONAY_TARIHI_6"] + " " + df["ONAY_SAATI_6"],errors="coerce")
    df["ONAY_TARIHI_7"]= pd.to_datetime(df["ONAY_TARIHI_7"] + " " + df["ONAY_SAATI_7"],errors="coerce")
    df["ONAY_TARIHI_8"]= pd.to_datetime(df["ONAY_TARIHI_8"] + " " + df["ONAY_SAATI_8"],errors="coerce")


    # df["ONAY_SURESI_1"] = df["ONAY_TARIHI_1"] - df["YARATMA_TARIHI"]
    # df["ONAY_SURESI_2"] = df["ONAY_TARIHI_2"] - df["ONAY_TARIHI_1"]
    # df["ONAY_SURESI_3"] = df["ONAY_TARIHI_3"] - df["ONAY_TARIHI_2"]
    # df["ONAY_SURESI_4"] = df["ONAY_TARIHI_4"] - df["ONAY_TARIHI_3"]
    # df["ONAY_SURESI_5"] = df["ONAY_TARIHI_5"] - df["ONAY_TARIHI_4"]
    # df["ONAY_SURESI_6"] = df["ONAY_TARIHI_6"] - df["ONAY_TARIHI_5"]
    # df["ONAY_SURESI_7"] = df["ONAY_TARIHI_7"] - df["ONAY_TARIHI_6"]
    # df["ONAY_SURESI_8"] = df["ONAY_TARIHI_8"] - df["ONAY_TARIHI_7"]

    df["ONAY_SURESI_1"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["YARATMA_TARIHI"],row["ONAY_TARIHI_1"]),axis =1 )
    df["ONAY_SURESI_2"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_1"],row["ONAY_TARIHI_2"]),axis =1 )
    df["ONAY_SURESI_3"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_2"],row["ONAY_TARIHI_3"]),axis =1 )
    df["ONAY_SURESI_4"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_3"],row["ONAY_TARIHI_4"]),axis =1 )
    df["ONAY_SURESI_5"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_4"],row["ONAY_TARIHI_5"]),axis =1 )
    df["ONAY_SURESI_6"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_5"],row["ONAY_TARIHI_6"]),axis =1 )
    df["ONAY_SURESI_7"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_6"],row["ONAY_TARIHI_7"]),axis =1 )
    df["ONAY_SURESI_8"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_7"],row["ONAY_TARIHI_8"]),axis =1 )


    df.drop(["ONAY_SAATI_1","ONAY_SAATI_2","ONAY_SAATI_3","ONAY_SAATI_4",
    "ONAY_SAATI_5","ONAY_SAATI_6","ONAY_SAATI_7",
    "ONAY_SAATI_8",],axis=1)

    tb = TableEditor()
    df= tb.Tr2Eng(df)
 
    #df=df.astype(str)

    
    return df


def tb_zmm030_satinalma_sat(df):


    df = df.rename(columns={'Satınalma belgesi':"SATINALMA_BELGESI", 'Yaratıldı':"YARATILDI", 'Yaratma trh.':"YARATMA_TARIHI",
     'Onay durumu':"ONAY_DURUMU",
       'Üretim yeri':"URETIM_YERI", 'Başlık Metni':"BASLIK_METNI", 'Son İşlem Tarihi':"SON_ISLEM_TARIHI", 'Toplam Beklediği Gün':"TOPLAM_BEKLEDIGI_GUN",
        '1. Onaycı':"ONAYCI_1", "1. Onay Tarihi":"ONAY_TARIHI_1", "1. Onay Saati":"ONAY_SAATI_1",
        '2. Onaycı':"ONAYCI_2","2. Onay Tarihi":"ONAY_TARIHI_2", "2. Onay Saati":"ONAY_SAATI_2",
       '3. Onaycı':"ONAYCI_3","3. Onay Tarihi":"ONAY_TARIHI_3", "3. Onay Saati":"ONAY_SAATI_3",
        '4. Onaycı':"ONAYCI_4","4. Onay Tarihi":"ONAY_TARIHI_4", "4. Onay Saati":"ONAY_SAATI_4",
         '5. Onaycı':"ONAYCI_5","5. Onay Tarihi":"ONAY_TARIHI_5", "5. Onay Saati":"ONAY_SAATI_5",
          '6. Onaycı':"ONAYCI_6","6. Onay Tarihi":"ONAY_TARIHI_6", "6. Onay Saati":"ONAY_SAATI_6",
           '7. Onaycı':"ONAYCI_7","7. Onay Tarihi":"ONAY_TARIHI_7", "7. Onay Saati":"ONAY_SAATI_7",
       '8. Onaycı':"ONAYCI_8", "8. Onay Tarihi":"ONAY_TARIHI_8", "8. Onay Saati":"ONAY_SAATI_8"
    })

    df["TOPLAM_BEKLEDIGI_GUN"] = df["SON_ISLEM_TARIHI"] - df["YARATMA_TARIHI"]

    df=df.drop(["YARATILDI","URETIM_YERI","BASLIK_METNI"],axis=1)

    df = df.astype(str)
    df["YARATMA_TARIHI"] = pd.to_datetime(df["YARATMA_TARIHI"] + " " + "09:00:00",errors="coerce")
    df["ONAY_TARIHI_1"]= pd.to_datetime(df["ONAY_TARIHI_1"] + " " + df["ONAY_SAATI_1"],errors="coerce")
    df["ONAY_TARIHI_2"]= pd.to_datetime(df["ONAY_TARIHI_2"] + " " + df["ONAY_SAATI_2"],errors="coerce")
    df["ONAY_TARIHI_3"]= pd.to_datetime(df["ONAY_TARIHI_3"] + " " + df["ONAY_SAATI_3"],errors="coerce")
    df["ONAY_TARIHI_4"]= pd.to_datetime(df["ONAY_TARIHI_4"] + " " + df["ONAY_SAATI_4"],errors="coerce")
    df["ONAY_TARIHI_5"]= pd.to_datetime(df["ONAY_TARIHI_5"] + " " + df["ONAY_SAATI_5"],errors="coerce")
    df["ONAY_TARIHI_6"]= pd.to_datetime(df["ONAY_TARIHI_6"] + " " + df["ONAY_SAATI_6"],errors="coerce")
    df["ONAY_TARIHI_7"]= pd.to_datetime(df["ONAY_TARIHI_7"] + " " + df["ONAY_SAATI_7"],errors="coerce")
    df["ONAY_TARIHI_8"]= pd.to_datetime(df["ONAY_TARIHI_8"] + " " + df["ONAY_SAATI_8"],errors="coerce")


    # df["ONAY_SURESI_1"] = df["ONAY_TARIHI_1"] - df["YARATMA_TARIHI"]
    # df["ONAY_SURESI_2"] = df["ONAY_TARIHI_2"] - df["ONAY_TARIHI_1"]
    # df["ONAY_SURESI_3"] = df["ONAY_TARIHI_3"] - df["ONAY_TARIHI_2"]
    # df["ONAY_SURESI_4"] = df["ONAY_TARIHI_4"] - df["ONAY_TARIHI_3"]
    # df["ONAY_SURESI_5"] = df["ONAY_TARIHI_5"] - df["ONAY_TARIHI_4"]
    # df["ONAY_SURESI_6"] = df["ONAY_TARIHI_6"] - df["ONAY_TARIHI_5"]
    # df["ONAY_SURESI_7"] = df["ONAY_TARIHI_7"] - df["ONAY_TARIHI_6"]
    # df["ONAY_SURESI_8"] = df["ONAY_TARIHI_8"] - df["ONAY_TARIHI_7"]

    df["ONAY_SURESI_1"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["YARATMA_TARIHI"],row["ONAY_TARIHI_1"]),axis =1 )
    df["ONAY_SURESI_2"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_1"],row["ONAY_TARIHI_2"]),axis =1 )
    df["ONAY_SURESI_3"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_2"],row["ONAY_TARIHI_3"]),axis =1 )
    df["ONAY_SURESI_4"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_3"],row["ONAY_TARIHI_4"]),axis =1 )
    df["ONAY_SURESI_5"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_4"],row["ONAY_TARIHI_5"]),axis =1 )
    df["ONAY_SURESI_6"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_5"],row["ONAY_TARIHI_6"]),axis =1 )
    df["ONAY_SURESI_7"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_6"],row["ONAY_TARIHI_7"]),axis =1 )
    df["ONAY_SURESI_8"] = df.apply(lambda row: zm.zaman_farki_hesapla(row["ONAY_TARIHI_7"],row["ONAY_TARIHI_8"]),axis =1 )


    df.drop(["ONAY_SAATI_1","ONAY_SAATI_2","ONAY_SAATI_3","ONAY_SAATI_4",
    "ONAY_SAATI_5","ONAY_SAATI_6","ONAY_SAATI_7",
    "ONAY_SAATI_8",],axis=1)

    tb = TableEditor()
    df= tb.Tr2Eng(df)
 
    #df=df.astype(str)

    
    return df



def tb_stok_giris_cikis_MB51(df_tb):


    df_tb = df_tb.rename(columns={'Üretim yeri':"URETIM_YERI", 'Depo yeri':"DEPO_YERI", 'Malzeme belgesi':"MALZEME_BELGESI", 'İşlem türü':"ISLEM_TURU",
       'Hareket türleri metni':"HAREKET_TURLERI_METNI", "Giriş tarihi":"GIRIS_TARIHI", 'Giriş saati':"GIRIS_SAATI", 'Kullanıcının adı':"KULLANICININ_ADI",
       'Kayıt tarihi':"KAYIT_TARIHI", 'Belge tarihi':"BELGE_TARIHI"  , "Satınalma siparişi": "SATINALMA_SIPARISI", "Malzeme belgesi klm.":"MALZEME_BELGESI_KLM_"
       ,"Malzeme":"MALZEME", "Malzeme kısa metni": "MALZEME_KISA_METNI", "Miktar": "MIKTAR", "Temel ölçü birimi": "TEMEL_OLCU_BIRIMI", "Tutar (UPB)": "TUTAR__UPB_"
       ,"Para birimi":"PARA_BIRIMI","PYP öğesi":"PYP_OGESI", "Masraf yeri":"MASRAF_YERI","Aktivite türü":"AKTIVITE_TURU","Akt.türü kısa metni":"AKT_TURU_KISA_METNI",
       "Sipariş":"SIPARIS", "Ekipman":"EKIPMAN","Ekipman tanımı":"EKIPMAN_TANIMI","Ad 1":"AD_1","Belge başlığı metni":"BELGE_BASLIGI_METNI","İç Sipariş Tanımı":"IC_SIPARIS_TANIMI",
       "Şirket kodu":"SIRKET_KODU"
    })


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)
    df["RAPOR_NO"] = "MB51"
    


    df=df.astype(str)

    df=nanCevir(df)
    return df

#Silme göstergesi	Sabitleme göstergesi	Onay göstergesi	Satınalma talebi	Satınalma grubu	SAS tarihi	
# SAS kalemi	Satınalma siparişi	SA sprş.miktarı	Talep tarihi	Malzeme	Kısa metin	Talep miktarı	Ölçü birimi	Fatura girişi
# 	Üretim yeri	Depo yeri	SAT kalemi	Belge türü	Satınalma talebi işleme durumu	İşleme durumu	Onay tarihi	Talep eden	Yaratıldı
# 	Onay grubu	Onay stratejisi	İstenen 	İstenen satıcı adı




def tb_satinalma_talebi_ME5A(df_tb):


    df_tb = df_tb.rename(columns={'Silme göstergesi':"SILME_GOSTERGESI", 'Sabitleme göstergesi':"SABITLEME_GOSTERGESI", 'Onay göstergesi':"ONAY_GOSTERGESI",
     'Satınalma talebi':"SATINALMA_TALEBI",
       'Satınalma grubu':"SATINALMA_GRUBU", "SAS tarihi":"SAS_TARIHI", 'SAS kalemi':"SAS_KALEMI", 'Satınalma siparişi':"SATINALMA_SIPARISI",
       'SA sprş.miktarı':"SA_SPRS_MIKTARI", 'Talep tarihi':"TALEP_TARIHI"  , "Malzeme": "MALZEME", "Kısa metin":"KISA_METIN"
       ,"Talep miktarı":"TALEP_MIKTARI", "Ölçü birimi": "OLCU_BIRIMI", "Fatura girişi": "FATURA_GIRISI", "Üretim yeri": "URETIM_YERI"
       ,"Depo yeri":"DEPO_YERI","SAT kalemi":"SAT_KALEMI", "Belge türü":"BELGE_TURU","Satınalma talebi işleme durumu":"SATINALMA_TALEBI_ISLEME_DURUMU",
       "İşleme durumu":"ISLEME_DURUMU",
       "Onay tarihi":"ONAY_TARIHI","Talep eden":"TALEP_EDEN","Yaratıldı":"YARATILDI","Onay grubu":"ONAY_GRUBU",
       "Onay stratejisi":"ONAY_STRATEJISI","İstenen satıcı":"ISTENEN_SATICI","İstenen satıcı adı":"ISTENEN_SATICI_ADI"
    })


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)
    df["RAPOR_NO"] = "ME5A"
    


    df=df.astype(str)

    df=nanCevir(df)
    return df



def tb_bakim_onarim_ZPM007(df_tb):


    df_tb = df_tb.rename(columns={'Planlama üretim yeri':"PLANLAMA_URETIM_YERI", 'BO üretim yeri':"BO_URETIM_YERI", 'Ekipman':"EKIPMAN",
     'Mali yıl':"MALI_YIL",
       'Dönem':"DONEM", "Değer/KKPB":"DEGER_KKPB", 'Değer/İPB':"DEGER_IPB", 'İşlem para birimi':"ISLEM_PARA_BIRIMI",
       'Aktivite türü':"AKTIVITE_TURU", 'Sipariş':"SIPARIS"  , "Kısa metin": "KISA_METIN", "Satınalma belgesi":"SATINALMA_BELGESI"
       ,"Satıcı":"SATICI", "Ad 1": "AD_1", "Malzeme": "MALZEME", "Toplam ol.grl.miktar": "TOPLAM_OL_GRL_MIKTAR", "Kaydedilen ölçü brm.": "KAYDEDILEN_OLCU_BRM_"
       ,"Masraf çeşidi":"MASRAF_CESIDI","Belge numarası":"BELGE_NUMARASI", "Kayıt satırı":"KAYIT_SATIRI","Şirket kodu":"SIRKET_KODU",
       "İş alanı":"IS_ALANI",
       "Kayıt tarihi":"KAYIT_TARIHI"
    })


    df = df_tb
    tb = TableEditor()
    df= tb.Tr2Eng(df)
    df["RAPOR_NO"] = "ZPM007"
    


    df=df.astype(str)

    df=nanCevir(df)
    return df




class TableEditor():
    
    def Tr2Eng(self,df):
        
        string_columns = df.select_dtypes(include=["object"])

        for col in string_columns:
            #df[col] = df[col].apply(lambda x: x.lower() if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("ö", "o") if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("ü", "u") if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("ı", "i") if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("ş", "s") if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("ç", "c") if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("ğ", "g") if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("Ö", "O") if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("Ü", "U") if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("İ", "I") if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("Ş", "S") if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("Ç", "C") if isinstance(x, str) else x)
            df[col] = df[col].apply(lambda x: x.replace("Ğ", "G") if isinstance(x, str) else x)

        return df



#Hesap planı	Ana hesap	Yaratma tarihi	Yaratan	Hesap grubu	Kısa metin	Ana hesap uzun metni	Zaman damgası
