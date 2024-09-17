from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

output_file = r"C:\Users\owery\OneDrive\Masaüstü\Python\tplinkVx231\logs.txt" # Loglar yolu belirlenmis olan yere yazilir.

def write_to_file(data): # Yolu belirlenmis olan yere ekleme yaparak yazar.
    with open(output_file, 'a', encoding='utf-8') as file: # output_file olarak tanimlanmis olan txt dosyasani file olarak acip ustune ekleyerek yazar.
        file.write(data)
    

def OPENINTERFACE(driver): # Modemin arayuzunu acar.
    
    driver.get("http://192.168.1.1/") # Modemin arayuz linkini tarayicida acar.
    time.sleep(2) # Diger isleme gecmeden once ekranin yuklenmesini bekler
    print("Arayuz acildi.")
    
def LOGINPANEL(driver): # Modemin arayuzune giris yapmak icin gerekli verilerle giris yapar.
    userName = "admin"
    userPassword = "admin123"
    userNameInput = driver.find_element(By.ID, "pc-login-user")
    userNameInput.send_keys(userName) # Gerekli username'i girer.
    userPasswordInput = driver.find_element(By.ID, "pc-login-password")
    userPasswordInput.send_keys(userPassword) # Gerekli sifreyi girer.
    loginButton = driver.find_element(By.ID, "pc-login-btn")
    loginButton.click()
    time.sleep(2)
    print("Giris yapildi.")

def CONFIRM_POPUP(driver): # Modemin arayuzune giris yapilirken baska cihazda oturum aciksa sabit cihazi bu cihaz yapar.
    try:
        confirmButton = driver.find_element(By.ID, "confirm-yes") # Cikan pop-up ekranina onay verir adresi "confirmButton" olarak tanimlar.
        confirmButton.click() # Tanimlanmis olan "confirmButton" tusuna tiklar.
        time.sleep(2)
    except:
        pass

def ADVANCED_SECTION(driver): # Modemin arayuzunun menusunde yer alan 'Advcanced' kismina tiklar ve sayfanin yuklenmesini bekler.
    time.sleep(10)
    advanceButton = driver.find_element(By.CSS_SELECTOR, ".T_adv") # Advanced menusunun adresini "advanceButton" olarak tanimlar.
    advanceButton.click() # Tanimlanmis olan "advanceButton" tusuna tiklar.
    time.sleep(15)
    

def UPTIME(driver): # 'Advanced' kisminda yer alan "Up Time" verisini ceker ve dosyaya yazdirir.
    uptimeValue = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div[3]/div/form/div/div[1]/input") # "Up Time" verisinin yolu.
    uptime = uptimeValue.get_attribute('value') # "Up Time" verisini cekip "uptime" degiskeni olarak atar.

    return uptime

def RAM_USAGE(driver): # Toplam RAM'in ne kadararinin kullanilmadigi verisini ceker ve dosyaya yazdirir.
    ramNotUsingValue = driver.find_element(By.XPATH, "//input[@id='tMemFree']") # Kullanilmayan RAM degerinin adresini belirler.
    ramNotUsing = ramNotUsingValue.get_attribute('value') # Belirlenen adresi "ramNotUsing" degiskeni olarak atar.
   
    return ramNotUsing

def CPU_USAGE(driver): # CPU'nun ne kadarinin calistiginin verisini ceker ve dosyaya yazdirir.
    
    cpuUsing = driver.find_element(By.XPATH, "//b[@id='cpu_gitem']") # CPU degerinin adresini belirler.
    time.sleep(2)
    cpuUsage = cpuUsing.text # Belirlenen adresi "cpuUsage" olarak atar.
    print(cpuUsage)
    return cpuUsage

def SSID_DATA(driver): # SSID verisini ceker ve dosyaya yazdirir.
    ssid = driver.find_element(By.XPATH, "//input[@id='ssid_2g']") # SSID degerinin adresini belirler.
    ssid_data = ssid.get_attribute('value') # Belirlenen adresi "ssid_data" olarak atar.
    
    return ssid_data

def CHANNEL_DATA(driver): # Channel Data verisini ceker ve dosyaya yazdirir.
    channel = driver.find_element(By.XPATH, "//input[@id='channel_2g']") # Channel Data degerinin adresini belirler.
    channel_data = channel.get_attribute('value') # Belirlenen adresi "channel_data" olarak atar.
   
    return channel_data

def BANDWIDTH_DATA(driver): # Band Width verisini ceker ve dosyaya yazdirir.
    bandwidth = driver.find_element(By.XPATH, "//input[@id='channelWidth_2g']") # Band Width degerinin adresini belirler.
    bandwidth_data = bandwidth.get_attribute('value') # Belirlenen adresi "bandwidth_data" olarak atar.
    
    return bandwidth_data

def dl_ul_datapage(driver):# DL ve UL verilerine ulasmak icin gereken sayfaya erisim saglar.
    systemToolsButton = driver.find_element(By.CSS_SELECTOR, ".ml1:nth-child(10) > .click > .text") # System Tools menusunun adresini belirler.
    systemToolsButton.click() # System Tools menusune tiklar.
    time.sleep(3)
    systemTrafficButton = driver.find_element(By.CSS_SELECTOR, ".ml2:nth-child(9) .text") # System Tools menusunde yer alan Trafik butonunun adresini belirler.
    systemTrafficButton.click() # Trafik butonuna tiklar.
    time.sleep(3)
    

def DOWNLOAD_DATA(driver):
    downloadspeed = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .table-content:nth-child(12)") 
    download_data = downloadspeed.text 
    return download_data

def UPLOAD_DATA(driver):
    uploadspeed = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .table-content:nth-child(13)") 
    upload_data = uploadspeed.text 
    return upload_data

def refresh_page(driver): # Sayfayi yeniler.
    time.sleep(3) # Verilerin islenmesini bekler.
    driver.refresh()
    

def EXIT(driver): # Arayuzden cikis yapilmasini saglar.
    exit1Button = driver.find_element(By.CSS_SELECTOR, "#localLogin > .icon") # Admin Logosunun adresini belirler.
    exit1Button.click() # Bu adrese tiklar.
    
    time.sleep(3)

    exit2Button = driver.find_element(By.CSS_SELECTOR, "#top-control-localaccount-logout") # Acilan menude cikis yap butonunun adresi belirlenir.
    exit2Button.click() # Bu butona tiklanir.

    time.sleep(3)

    exit3Button = driver.find_element(By.CSS_SELECTOR, ".btn-msg-ok > span") # Cikis yapmak istediginizden emin misiniz sorusunun evet seceneginin adresi belirlenir.   
    exit3Button.click() # Butona tiklanir ve cikis yapilir.

    time.sleep(3)

def CLOSEWEB(driver):
    driver.quit

# Fonksiyonlarin cagrilip uygulanmasi:
def main():
    driver = webdriver.Chrome(service=Service("C:/Program Files (x86)/chromedriver.exe"))
    
    OPENINTERFACE(driver)
    LOGINPANEL(driver)
    
    CONFIRM_POPUP(driver)
    
    ADVANCED_SECTION(driver)
    
    uptime = UPTIME(driver)
    ram_usage = RAM_USAGE(driver)
    cpu_usage = CPU_USAGE(driver)
    ssid_data = SSID_DATA(driver)
    channel_data = CHANNEL_DATA(driver)
    bandwidth_data = BANDWIDTH_DATA(driver)
    
    dl_ul_datapage(driver)
    download_data = DOWNLOAD_DATA(driver)
    upload_data = UPLOAD_DATA(driver)
    
    time_data = datetime.now()
    write_to_file(f"\n{time_data} | {uptime} | {ram_usage} |  {cpu_usage}     |  {ssid_data} |  {channel_data}      |  {bandwidth_data}           |  {download_data}    |  {upload_data}")
    
    EXIT(driver)
    CLOSEWEB(driver)

if __name__ == "__main__":
    for _ in range(10):
     main()
     time.sleep(180)