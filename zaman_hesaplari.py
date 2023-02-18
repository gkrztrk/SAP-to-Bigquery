import pandas as pd

def zaman_farki_hesapla(baslangic_tarihi,bitis_tarihi):

    # mesai saatlerini ve haftasonlarını dikkate alarak zaman farkı hesaplama..

    bitis_tarihi =pd.to_datetime(bitis_tarihi)
    baslangic_tarihi = pd.to_datetime(baslangic_tarihi)

    sayac=0
    bekleme_suresi =0
    hafta_ici= ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    tarih = baslangic_tarihi 

    while baslangic_tarihi.date() + pd.Timedelta(days=sayac) < bitis_tarihi.date() :
        
        
        if tarih.day_name() in hafta_ici:
            bekleme_suresi = bekleme_suresi + 10
            sayac=sayac + 1
            tarih = tarih + pd.Timedelta(days=1)
        elif tarih.day_name() == "Saturday":
            bekleme_suresi = bekleme_suresi + 5
            sayac = sayac + 1
            tarih = tarih + pd.Timedelta(days=1)
        else:
            sayac = sayac + 1
            tarih = tarih + pd.Timedelta(days=1)

    bekleme_suresi = pd.Timedelta(hours=bekleme_suresi)
    
    bekleme_suresi = bekleme_suresi + (bitis_tarihi - tarih )
    if baslangic_tarihi.date() == bitis_tarihi.date():
        if  bekleme_suresi > pd.Timedelta(hours=10):
            bekleme_suresi = pd.Timedelta(hours=10)

    bekleme_suresi=bekleme_suresi.total_seconds()/3600

    print(bekleme_suresi)
    return bekleme_suresi

