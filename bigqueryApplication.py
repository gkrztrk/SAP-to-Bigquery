
from google.api_core.exceptions import NotFound
import pandas
import pandas_gbq
from google.cloud import bigquery
from google.oauth2.service_account import Credentials
#pd.options.display.float_format = '{:,.2f} ₺'.format
import pandas 



class BigqueryApp():

    #Bigquery işlemleri yapmak için oluşturulmuştur
    credentials = Credentials.from_service_account_file(r'C:\Users\klv13\Code Projects\SAP\subtle-arcade-346306-479d467e7e29.json')
    client = bigquery.Client(credentials=credentials)

    def bq_veri_cek(self,query):

        
        self.client.query(query)
        print("sorgu tamamlandı")
        


    def bq_veri_gonder(self, database_name, table_name, data, mevcutsa = "append"):
        data = pandas.DataFrame(data)
        database = self.client.dataset(database_name)
        tablo_ref = database.table(table_name)  
        tablo_id =  f"{database.project}.{tablo_ref.dataset_id}.{tablo_ref.table_id}"
        pandas_gbq.context.credentials = self.credentials
        pandas_gbq.context.project = database.project
        print(data)
        data.to_gbq(tablo_id,database.project,credentials=self.credentials,if_exists=mevcutsa,)
        print("Veri Başarıyla Gönderildi")


    def bq_tablo_olustur(self, database_name, table_name):
        database = self.client.dataset(database_name)
        tablo_ref = database.table(table_name)       
        try:
            tablo = self.client.get_table(tablo_ref)
            print("tablo zaten var")
        except NotFound:
            tablo = bigquery.Table(tablo_ref)
            self.client.create_table(tablo)
            print("tablo oluşturuldu")


    def bq_tablo_sil(self,database_name,table_name):
        try:
            database = self.client.dataset(database_name)
            tablo_ref = database.table(table_name)  
            tablo_id =  f"{database.project}.{tablo_ref.dataset_id}.{tablo_ref.table_id}"
        
            self.client.delete_table(tablo_id)
            print("Tablo Silindi")
        except NotFound:
            print("Böyle bir tablo mevcut değil")



