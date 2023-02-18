import time
import subprocess
import win32com.client as win32
import os
import pandas as pd
import datetime as dt



class SapApp():

    def connectSap(self):
        self.SapGuiAuto= win32.GetObject("SAPGUI")
        application = self.SapGuiAuto.GetScriptingEngine
        self.connection= application.Children(0)
        self.session = self.connection.Children(0)

    def openSap(self):
        path = r"C:\Program Files (x86)\SAP\FrontEnd\SapGui\saplogon.exe"
        subprocess.Popen(path)

    def sapLogin(self):
        self.openSap()
        time.sleep(3)

        self.SapGuiAuto= win32.GetObject("SAPGUI")
        application = self.SapGuiAuto.GetScriptingEngine
        self.connection= application.OpenConnection("KLV CANLI", True)
        time.sleep(3)

        self.session = self.connection.Children(0)

        try:
            #client
            self.session.findById("wnd[0]/usr/txtRSYST-MANDT").text = '100'
            #User
            self.session.findById("wnd[0]/usr/txtRSYST-BNAME").text = 'UserName'
            #Password
            self.session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = 'Password'
            #Language
            self.session.findById("wnd[0]/usr/txtRSYST-LANGU").text = 'TR'
            #Enter
            self.session.findById("wnd[0]").sendVKey(0)

        except Exception as e:
            print(e)

    def closeSap(self):
        self.connectSap()
        self.connection.CloseSession("ses[0]")
        time.sleep(3)
      
    def elementListesiBulma(self):
        try:
            windows = self.session.Windows()
            for w in windows:
                print("Window Title:", w.Text)
                for c in w.Children():
                    print("\tControl Type:", c.Type, "\tControl ID:", c.Id)
        except Exception as e:
            print(e)




#---------------GELIR GIDER STOK TABLOLARI------------------

    def cji3(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "cji3"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/ctxtSVALD-VALUE[0,21]").text = "1000"
            self.session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/ctxtSVALD-VALUE[0,21]").caretPosition = 4
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtTCNT-PROF_DB").text = "000000000001"
            self.session.findById("wnd[1]/usr/ctxtTCNT-PROF_DB").caretPosition = 12
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtCN_PROJN-LOW").text = "*"
            self.session.findById("wnd[0]/usr/ctxtR_BUDAT-LOW").text = "01092022"
            self.session.findById("wnd[0]/usr/ctxtR_BUDAT-HIGH").text = "03032023"
            self.session.findById("wnd[0]/usr/ctxtR_BUDAT-HIGH").caretPosition = 8
            self.session.findById("wnd[0]/usr/btnBUT1").press()
            self.session.findById("wnd[1]/usr/txtKAEP_SETT-MAXSEL").text = "999999999"
            self.session.findById("wnd[1]/usr/txtKAEP_SETT-MAXSEL").caretPosition = 9
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]").sendVKey (43)
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Gider Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "CJI3.xlsx"
            self.session.findById("wnd[1]").sendVKey (11)
            
            time.sleep(3)
            print("CJI3 tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
            
        except Exception as e:
            print(e)

    def ksb1n(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "ksb1n"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/ctxtSVALD-VALUE[0,21]").text = "1000"
            self.session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/ctxtSVALD-VALUE[0,21]").caretPosition = 4
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[0]").sendVKey (17)
            self.session.findById("wnd[1]/usr/txtENAME-LOW").text = ""
            self.session.findById("wnd[1]/usr/txtENAME-LOW").setFocus()
            self.session.findById("wnd[1]/usr/txtENAME-LOW").caretPosition = 0
            self.session.findById("wnd[1]/tbar[0]/btn[8]").press()
            self.session.findById("wnd[1]/usr/cntlALV_CONTAINER_1/shellcont/shell").currentCellRow = 5
            self.session.findById("wnd[1]/usr/cntlALV_CONTAINER_1/shellcont/shell").selectedRows = "5"
            self.session.findById("wnd[1]/usr/cntlALV_CONTAINER_1/shellcont/shell").doubleClickCurrentCell()
            self.session.findById("wnd[0]/usr/chkP_HANA").selected = "false"
            self.session.findById("wnd[0]/usr/ctxtR_BUDAT-LOW").text = "01092022"
            self.session.findById("wnd[0]/usr/ctxtR_BUDAT-HIGH").text = "01032023"
            self.session.findById("wnd[0]/usr/ctxtR_BUDAT-HIGH").setFocus()
            self.session.findById("wnd[0]/usr/ctxtR_BUDAT-HIGH").caretPosition = 8
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]").sendVKey (43)
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Gider Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "KSB1N.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 10
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("KSB1N tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)       

    def fagll03Gider(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "fagll03"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]").sendVKey (17)
            self.session.findById("wnd[1]/usr/txtENAME-LOW").text = ""
            self.session.findById("wnd[1]/usr/txtENAME-LOW").setFocus()
            self.session.findById("wnd[1]/usr/txtENAME-LOW").caretPosition = 0
            self.session.findById("wnd[1]").sendVKey (8)
            self.session.findById("wnd[1]/usr/cntlALV_CONTAINER_1/shellcont/shell").currentCellRow = 4
            self.session.findById("wnd[1]/usr/cntlALV_CONTAINER_1/shellcont/shell").selectedRows = "4"
            self.session.findById("wnd[1]/usr/cntlALV_CONTAINER_1/shellcont/shell").doubleClickCurrentCell()
            self.session.findById("wnd[0]/usr/ctxtSO_BUDAT-LOW").text = "01092022"
            self.session.findById("wnd[0]/usr/ctxtSO_BUDAT-HIGH").text = "01032023"
            self.session.findById("wnd[0]/usr/ctxtSO_BUDAT-HIGH").setFocus()
            self.session.findById("wnd[0]/usr/ctxtSO_BUDAT-HIGH").caretPosition = 8
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]").sendVKey (43)
            self.session.findById("wnd[0]/tbar[0]/btn[3]").press()
            self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").setCurrentCell(7,"HKONT")
            self.session.findById("wnd[0]").sendVKey (16)
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Gider Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "FAGLL03.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 12
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("FAGLL03 tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)            

    def fagll03Gelir(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "fagll03"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]").sendVKey (17)
            self.session.findById("wnd[1]/usr/txtENAME-LOW").text = ""
            self.session.findById("wnd[1]/usr/txtENAME-LOW").setFocus()
            self.session.findById("wnd[1]/usr/txtENAME-LOW").caretPosition = 0
            self.session.findById("wnd[1]").sendVKey (8)
            self.session.findById("wnd[1]/usr/cntlALV_CONTAINER_1/shellcont/shell").currentCellRow = 3
            self.session.findById("wnd[1]/usr/cntlALV_CONTAINER_1/shellcont/shell").selectedRows = "3"
            self.session.findById("wnd[1]/usr/cntlALV_CONTAINER_1/shellcont/shell").doubleClickCurrentCell()
            self.session.findById("wnd[0]/usr/ctxtSO_BUDAT-LOW").text = "01092022"
            self.session.findById("wnd[0]/usr/ctxtSO_BUDAT-HIGH").text = "01032023"
            self.session.findById("wnd[0]/usr/ctxtPA_VARI").text = "GKR3"
            self.session.findById("wnd[0]/usr/ctxtSO_BUDAT-HIGH").setFocus()
            self.session.findById("wnd[0]/usr/ctxtSO_BUDAT-HIGH").caretPosition = 8
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]").sendVKey (43)
            self.session.findById("wnd[0]/tbar[0]/btn[3]").press()
            self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").setCurrentCell (2,"HKONT")
            self.session.findById("wnd[0]").sendVKey (16)
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Gider Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "GELIR.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = (10)
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("GELIR tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)          

    def mb52(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "mb52"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtMATNR-LOW").text = "*"
            self.session.findById("wnd[0]/usr/ctxtMATNR-LOW").caretPosition = 1
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/mbar/menu[0]/menu[3]/menu[1]").select()
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Gider Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "MB52.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("MB52 tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)           



#---------------SATINALMA SİPARİŞ TABLOLARI------------------



    def me2n(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "me2n"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtEN_EBELN-LOW").text = "*"
            self.session.findById("wnd[0]/usr/ctxtEN_EBELN-LOW").caretPosition = 1
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]").sendVKey (33)
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cmbG51_SCREEN-USPEC_LBOX").key = "X"
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cntlD500_CONTAINER/shellcont/shell").clickCurrentCell()
            self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").firstVisibleRow = 1
            self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").firstVisibleRow = 0
            self.session.findById("wnd[0]").sendVKey (43)
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Satınalma Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "ME2N.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
            self.session.findById("wnd[1]").sendVKey (11)
            
            time.sleep(3)
            print("ME2N tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
            
        except Exception as e:
            print(e)


    def zmm030Sas(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "zmm030"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/radR1").setFocus()
            self.session.findById("wnd[0]/usr/radR1").select()
            self.session.findById("wnd[0]/usr/cmbP_ONAY").setFocus()
            self.session.findById("wnd[0]/usr/cmbP_ONAY").key = ""
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/tbar[1]/btn[33]").press()
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cmbG51_SCREEN-USPEC_LBOX").key = "X"
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cntlD500_CONTAINER/shellcont/shell").currentCellColumn = "TEXT"
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cntlD500_CONTAINER/shellcont/shell").clickCurrentCell()
            self.session.findById("wnd[0]").sendVKey (43)
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Satınalma Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "ZMM030.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = (11)
            self.session.findById("wnd[1]").sendVKey (11)
            
            time.sleep(3)
            print("ZMM030 tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
            
        except Exception as e:
            print(e)



    def zmm030Sat(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "zmm030"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/cmbP_ONAY").key = ""
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/tbar[1]/btn[33]").press()
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cmbG51_SCREEN-USPEC_LBOX").key = "X"
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cntlD500_CONTAINER/shellcont/shell").setCurrentCell (0,"TEXT")
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cntlD500_CONTAINER/shellcont/shell").selectedRows = "0"
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cntlD500_CONTAINER/shellcont/shell").clickCurrentCell()
            self.session.findById("wnd[0]").sendVKey (43)
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Satınalma Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Sat Onay.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 13
            self.session.findById("wnd[1]").sendVKey (11)
            
            time.sleep(3)
            print("ZMM030 Sat tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
            
        except Exception as e:
            print(e)


#--------------------SABİT TABLOLAR-------------------------

    def aktiviteTuru(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "se16n"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").text = "csla"
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").setFocus()
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").caretPosition = 0
            self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&XXL")
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Sabit Tablolar"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Aktivite Türü.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 20
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("Aktivite Türü tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)

    def anaHesap(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "se16n"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").text = "ska1"
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
            self.session.findById("wnd[0]/usr/txtGD-VARIANTTEXT").setFocus()
            self.session.findById("wnd[0]/usr/txtGD-VARIANTTEXT").caretPosition = 0
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&XXL")
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Sabit Tablolar"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Ana Hesap.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 14
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("Ana Hesap tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)

    def ekipman(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "se16n"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").text = "equi"
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").setFocus()
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").caretPosition = 0
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&XXL")
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Sabit Tablolar"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Ekipman.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 12
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("Ekipman tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)

    def isAlani(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "se16n"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").text = "tgsbt"
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").caretPosition = 5
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&XXL")
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Sabit Tablolar"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "İş Alanı.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 16
            self.session.findById("wnd[1]").sendVKey (11)           
            print("İş Alanı tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)

    def malzeme(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "se16n"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").text = "mara"
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").caretPosition = 4
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&XXL")
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Sabit Tablolar"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Malzeme.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 12
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("Malzeme tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)

    def masrafCesidi(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "se16n"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").text = "cska"
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").caretPosition = 4
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&XXL")
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Sabit Tablolar"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Masraf Çeşidi.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 20
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("Masraf Çeşidi tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)

    def sirket(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "se16n"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").text = "t001"
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").caretPosition = 4
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&XXL")
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Sabit Tablolar"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Şirket.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 12
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("Şirket tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)

    def malGrubu(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "se16n"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").text = "t023"
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").caretPosition = 4
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&XXL")
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Sabit Tablolar"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Mal Grubu.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 14
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("Mal Grubu tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)



    def kur(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "se16n"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").text = "TCURR"
            self.session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
            self.session.findById("wnd[0]/usr/ctxtGD-TAB").caretPosition = 5
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
            self.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem ("&XXL")
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Taşeron Hakedişi Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Kur.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 8
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("Kur tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)

    def stok_giris_cikis_MB51(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "mb51"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtMATNR-LOW").text = "*"
            self.session.findById("wnd[0]/usr/ctxtBUDAT-LOW").text = "01102022"
            self.session.findById("wnd[0]/usr/ctxtBUDAT-HIGH").text = "22032023"
            self.session.findById("wnd[0]/usr/ctxtALV_DEF").text = "GKR"
            self.session.findById("wnd[0]/usr/ctxtBUDAT-HIGH").setFocus()
            self.session.findById("wnd[0]/usr/ctxtBUDAT-HIGH").caretPosition = 8
            self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
            self.session.findById("wnd[0]/tbar[1]/btn[32]").press()
            self.session.findById("wnd[1]/tbar[0]/btn[36]").press()
            self.session.findById("wnd[1]/usr/tabsG_TS_ALV/tabpALV_M_R9/ssubSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cmbG51_SCREEN-USPEC_LBOX").key = "X"
            self.session.findById("wnd[1]/usr/tabsG_TS_ALV/tabpALV_M_R9/ssubSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cntlD500_CONTAINER/shellcont/shell").clickCurrentCell()
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
            self.session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[1]").select()
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Malzeme Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "MB51.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("Stok-Giriş-Çıkış tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)


    def satinalma_talebi_ME5A(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "me5a"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/chkP_MEMORY").selected = True
            self.session.findById("wnd[0]/usr/chkP_ERLBA").selected = True
            self.session.findById("wnd[0]/usr/ctxtBA_BANFN-LOW").text = "*"
            self.session.findById("wnd[0]/usr/chkP_ERLBA").setFocus()
            self.session.findById("wnd[0]/tbar[1]/btn[8]").press()
            self.session.findById("wnd[0]/tbar[1]/btn[33]").press()
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cmbG51_SCREEN-USPEC_LBOX").key = "X"
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cntlD500_CONTAINER/shellcont/shell").clickCurrentCell
            self.session.findById("wnd[0]").sendVKey (43)
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Malzeme Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "ME5A.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("Satınalma Talebi tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)

    def bakim_onarim_ZPM007(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "zpm007"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/ctxtSO_EQUNR-LOW").text = "*"
            self.session.findById("wnd[0]/usr/ctxtSO_EQUNR-LOW").caretPosition = 1
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/usr/cntlCONTAINER/shellcont/shell").pressToolbarContextButton ("&MB_VARIANT")
            self.session.findById("wnd[0]/usr/cntlCONTAINER/shellcont/shell").selectContextMenuItem ("&LOAD")
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cmbG51_SCREEN-USPEC_LBOX").key = "X"
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press
            self.session.findById("wnd[0]/usr/cntlCONTAINER/shellcont/shell").pressToolbarContextButton ("&MB_EXPORT")
            self.session.findById("wnd[0]/usr/cntlCONTAINER/shellcont/shell").selectContextMenuItem ("&XXL")
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\EKİPMAN TABLOLARI"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "ZPM007.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 11
            self.session.findById("wnd[1]").sendVKey (11)
            
            print("Satınalma Talebi tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)



#--------------------TASERON HAKEDİŞLERİ-------------------------


    def zmm032Hk(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "zmm032"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]/mbar/menu[0]/menu[3]/menu[1]").select()
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Taşeron Hakedişi Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Hakedis.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 12
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/tbar[0]/btn[11]").press()
            
            print("Hakediş tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)           

    def zmm032Ks(self):
        try:
            self.session.findById("wnd[0]").maximize
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "zmm032"
            self.session.findById("wnd[0]").sendVKey (0)
            self.session.findById("wnd[0]/usr/radR2").setFocus()
            self.session.findById("wnd[0]/usr/radR2").select()
            self.session.findById("wnd[0]").sendVKey (8)
            self.session.findById("wnd[0]").sendVKey (33)
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cntlD500_CONTAINER/shellcont/shell").currentCellRow = 2
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cntlD500_CONTAINER/shellcont/shell").selectedRows = "2"
            self.session.findById("wnd[1]/usr/subSUB_CONFIGURATION:SAPLSALV_CUL_LAYOUT_CHOOSE:0500/cntlD500_CONTAINER/shellcont/shell").clickCurrentCell()
            self.session.findById("wnd[0]/mbar/menu[0]/menu[3]/menu[1]").select()
            self.session.findById("wnd[1]").sendVKey (0)
            self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = r"C:\Users\klv13\Desktop\Taşeron Hakedişi Tabloları"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Kesinti.xlsx"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 12
            self.session.findById("wnd[1]/tbar[0]/btn[11]").press()

            
            print("Hakediş tablosu indirildi")
            os.system("taskkill /f /im excel.exe")
        except Exception as e:
            print(e)           



            



#------------Tabloları İndir-------------------

    def gelirGiderTablolariIndir(self):

        dfLog = pd.DataFrame()
        dfLog= pd.read_excel(r"C:\Users\klv13\Desktop\Gider Tabloları\LOG.xlsx")
        sp = SapApp()

        sp.sapLogin()
        sp.cji3()
        dfLog = dfLog.append(pd.Series(["CJI3 Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.ksb1n()
        dfLog = dfLog.append(pd.Series(["KSB1N Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.fagll03Gider()
        dfLog = dfLog.append(pd.Series(["FAGLL03 Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.fagll03Gelir()
        dfLog = dfLog.append(pd.Series(["GELIR Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.mb52()
        dfLog = dfLog.append(pd.Series(["MB52 Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()

        dfLog =pd.DataFrame(dfLog)
        dfLog.to_excel(r"C:\Users\klv13\Desktop\Gider Tabloları\LOG.xlsx",index=False)

    def sabitTablolariIndir(self):

        dfLog = pd.DataFrame()
        dfLog= pd.read_excel(r"C:\Users\klv13\Desktop\Gider Tabloları\LOG.xlsx")
        sp = SapApp()

        sp.sapLogin()
        sp.aktiviteTuru()
        dfLog = dfLog.append(pd.Series(["Aktivite Türü Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.anaHesap()
        dfLog = dfLog.append(pd.Series(["Ana Hesap Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.ekipman()
        dfLog = dfLog.append(pd.Series(["Ekipman Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.isAlani()
        dfLog = dfLog.append(pd.Series(["İş Alanı Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.malzeme()
        dfLog = dfLog.append(pd.Series(["Malzeme Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.masrafCesidi
        dfLog = dfLog.append(pd.Series(["Masraf Çeşidi Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.sirket()
        dfLog = dfLog.append(pd.Series(["Şirket Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.malGrubu()
        dfLog = dfLog.append(pd.Series(["Mal Grubu Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.kur()
        dfLog = dfLog.append(pd.Series(["Kur Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()

        dfLog =pd.DataFrame(dfLog)
        dfLog.to_excel(r"C:\Users\klv13\Desktop\Gider Tabloları\LOG.xlsx",index=False)

    def taseronHakedisTablolariIndir(self):

        dfLog = pd.DataFrame()
        dfLog= pd.read_excel(r"C:\Users\klv13\Desktop\Gider Tabloları\LOG.xlsx")
        sp = SapApp()

        sp.sapLogin()
        sp.zmm032Hk()
        dfLog = dfLog.append(pd.Series(["Hakedis Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.zmm032Ks()
        dfLog = dfLog.append(pd.Series(["Kesinti Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        
        dfLog =pd.DataFrame(dfLog)
        dfLog.to_excel(r"C:\Users\klv13\Desktop\Gider Tabloları\LOG.xlsx",index=False)


    def satinalmaSiparisTablolariIndir(self):

        dfLog = pd.DataFrame()
        dfLog= pd.read_excel(r"C:\Users\klv13\Desktop\Gider Tabloları\LOG.xlsx")
        sp = SapApp()

        sp.sapLogin()
        sp.me2n()
        dfLog = dfLog.append(pd.Series(["Me2n Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.zmm030Sas()
        dfLog = dfLog.append(pd.Series(["ZMM030Sas Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()

        sp.sapLogin()
        sp.zmm030Sat()
        dfLog = dfLog.append(pd.Series(["ZMM030Sat Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()        
        
        dfLog =pd.DataFrame(dfLog)
        dfLog.to_excel(r"C:\Users\klv13\Desktop\Gider Tabloları\LOG.xlsx",index=False)


    def malzemeTablolariIndir(self):

        dfLog = pd.DataFrame()
        dfLog= pd.read_excel(r"C:\Users\klv13\Desktop\Gider Tabloları\LOG.xlsx")
        sp = SapApp()

        sp.sapLogin()
        sp.stok_giris_cikis_MB51()
        dfLog = dfLog.append(pd.Series(["Me2n Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        sp.sapLogin()
        sp.satinalma_talebi_ME5A()
        dfLog = dfLog.append(pd.Series(["ZMM030Sas Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()

        sp.sapLogin()
        sp.bakim_onarim_ZPM007()
        dfLog = dfLog.append(pd.Series(["ZMM030Sas Tablosu İndirildi",dt.datetime.now()],index=["Log","Time"]),ignore_index=True)
        sp.closeSap()
        
        dfLog =pd.DataFrame(dfLog)
        dfLog.to_excel(r"C:\Users\klv13\Desktop\Gider Tabloları\LOG.xlsx",index=False)

   
