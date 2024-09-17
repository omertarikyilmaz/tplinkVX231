from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

logs = r"C:\Users\owery\OneDrive\Masaüstü\Python\tplinkVX231\logs.txt"

def write_to_file(data): 
    with open(logs, 'a', encoding='utf-8') as file:
        file.write(data)
    
def OPENINTERFACE(driver): 
    driver.get("http://192.168.1.1/") 
    time.sleep(2) 
    print("Arayuz acildi.")
    
    #----------------------------Interface Giris-----------------------------------#
def LOGINPANEL(driver):
    userName = "admin"
    userPassword = "admin123"
    userNameInput = driver.find_element(By.ID, "pc-login-user")
    userNameInput.send_keys(userName)
    userPasswordInput = driver.find_element(By.ID, "pc-login-password")
    userPasswordInput.send_keys(userPassword)
    loginButton = driver.find_element(By.ID, "pc-login-btn")
    loginButton.click()
    time.sleep(2)
    print("Giris yapildi.")

def CONFIRM_POPUP(driver): 
    try:
        confirmButton = driver.find_element(By.ID, "confirm-yes") 
        confirmButton.click() 
        print("Pop-Up atlandi.")
        time.sleep(2)
    except:
        print("Pop-Up atlanamadi.")
        pass
    #----------------------------------------------------------------------------------------#  


    #----------------------------Gelismis Sayfasi'na Giris-----------------------------------#
def ADVANCED_SECTION(driver):
    time.sleep(10)
    advanceButton = driver.find_element(By.CSS_SELECTOR, ".T_adv") 
    advanceButton.click()
    print("Gelismis sayfasina Gidildi.")
    time.sleep(10)
    #----------------------------------------------------------------------------------------#


    #--------------------------------Gelismis Sayfasi-----------------------------------------#
def UPTIME(driver):
    uptimeValue = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div[3]/div/form/div/div[1]/input")
    uptime = uptimeValue.get_attribute('value')
    print("System Uptime verisi alindi.")
    return uptime

def RAM_USAGE(driver): 
    ramUsingValue = driver.find_element(By.XPATH, "//div[@id='mem_gbar']/b")
    ramUsing = ramUsingValue.get_attribute('innerText')
    print("Ram Usage (%) degeri alindi.")
    return ramUsing    

def CPU_USAGE(driver):
    cpuUsing = driver.find_element(By.XPATH, "//div[@id='cpu_gbar']/b")
    cpuUsage = cpuUsing.get_attribute('innerText')
    print("CPU Usage (%) degeri alindi.")
    return cpuUsage
    #----------------------------------------------------------------------------------------#


    #--------------------------------SSID: 2.4 GHZ Verileri----------------------------------#
def SSID_DATA1(driver):
    ssid1 = driver.find_element(By.XPATH, "//input[@id='ssid_2g']") 
    ssid_data1 = ssid1.get_attribute('value')
    print("SSID Data (2.4 GHz) degeri alindi.")
    return ssid_data1

def CH_DATA1(driver):
    ch1 = driver.find_element(By.ID, "channel_2g")
    ch1data = ch1.get_attribute('value')
    print("Channel (2.4 GHz) degeri alindi.")
    return ch1data

def BW_DATA1(driver):
    bw1 = driver.find_element(By.ID, "channelWidth_2g")
    bw1data = bw1.get_attribute('value')
    print("Bandwidth (2.4 GHz) degeri alindi.")
    return bw1data
    #----------------------------------------------------------------------------------------#


    #--------------------------------5G Veri Kismina Gecis-----------------------------------#
def SW5GHZ(driver):
    switchTo5GButton = driver.find_element(By.ID, "showWireless_5g")
    switchTo5GButton.click()
    time.sleep(2)
    #----------------------------------------------------------------------------------------#


    #-----------------------------------SSID: 5 GHZ Verileri---------------------------------#
def SSID_DATA2(driver):
    ssid2 = driver.find_element(By.ID, "ssid_5g") 
    ssid_data2 = ssid2.get_attribute('value')
    print("SSID Data (5 GHz) degeri alindi.")
    return ssid_data2

def CH_DATA2(driver):
    ch2 = driver.find_element(By.ID, "channel_5g")
    ch2data = ch2.get_attribute('value')
    print("Channel (5 GHz) degeri alindi.")
    return ch2data

def BW_DATA2(driver):
    bw2 = driver.find_element(By.ID, "channelWidth_5g")
    bw2data = bw2.get_attribute('value')
    print("Bandwidth (2.4 GHz) degeri alindi.")
    return bw2data
    #----------------------------------------------------------------------------------------#


    #-----------------------------------DL/UL Sayfasina Gidis---------------------------------#
def dl_ul_datapage(driver):
    systemToolsButton = driver.find_element(By.CSS_SELECTOR, ".ml1:nth-child(10) > .click > .text")
    systemToolsButton.click()
    time.sleep(3)
    systemTrafficButton = driver.find_element(By.CSS_SELECTOR, ".ml2:nth-child(9) .text") 
    systemTrafficButton.click()
    time.sleep(10)
    #------------------------------------------------------------------------------------------#


    #-------------------------------------DL ve UL Verileri------------------------------------#
def DOWNLOAD_DATA(driver):
    downloadspeed = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > .table-content:nth-child(13)")
    download_data = downloadspeed.text
    return download_data

def UPLOAD_DATA(driver):
    uploadspeed = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > .table-content:nth-child(12)")
    upload_data = uploadspeed.text
    return upload_data

def WAN_IP(driver):
    wip = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .table-content:nth-child(4)")
    wipdata = wip.text
    print("WAN IP degeri alindi.")
    return wipdata
    #-------------------------------------------------------------------------------------------#

def CLOSEWEB(driver):
    driver.quit

    #---------------------------------------MAIN FONKSIYONU---------------------------------------#
def main():
    driver = webdriver.Chrome(service=Service("C:/Program Files (x86)/chromedriver.exe"))
    OPENINTERFACE(driver)
    LOGINPANEL(driver)
    CONFIRM_POPUP(driver)
    ADVANCED_SECTION(driver)
    
    uptime = UPTIME(driver)
    ram_usage = RAM_USAGE(driver)
    cpu_usage = CPU_USAGE(driver)
    
    ssid_data2g = SSID_DATA1(driver)
    channel_data2g = CH_DATA1(driver)
    bandwidth_data2g = BW_DATA1(driver)

    SW5GHZ(driver)

    ssid_data5g = SSID_DATA2(driver)
    channel_data5g = CH_DATA2(driver)
    bandwidth_data5g = BW_DATA2(driver)

    dl_ul_datapage(driver)

    download_data = DOWNLOAD_DATA(driver)
    upload_data = UPLOAD_DATA(driver)
    wip_data = WAN_IP(driver)

    time_data = datetime.now()
    write_to_file(f"{time_data}|{uptime}|{ram_usage}       |{cpu_usage}       |{wip_data}|{ssid_data2g}|{channel_data2g}          |{bandwidth_data2g}                |{ssid_data5g}|{channel_data5g}       |{bandwidth_data5g}              |{download_data}|{upload_data}|\n")
    CLOSEWEB(driver)

if __name__ == "__main__":
    for _ in range(50):
     main()
     time.sleep(10)