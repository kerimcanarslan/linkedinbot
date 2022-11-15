#############
# LIBRARIES
#############

# FURKAN AKDAĞ
# KERİMCAN ARSLAN
# MİUUl & VBO


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# PATH OLARAK DRIVER KENDİ BİLGİSAYARINDA HANGİ PATHSE ONU VERMELİSİN!!!

driver_path = "/Users/kerimcanarslan/anaconda3/bin/chromedriver"
driver = webdriver.Chrome(driver_path)

#####################
# LINKED'INE BAĞLAN
#####################
driver.get("https://www.linkedin.com/")

#######################
# LINKEDIN'E GİRİŞ YAP
#######################
driver.find_element(by=By.XPATH, value="/html/body/nav/div/a[2]").click()  # Oturum Aç
mail = driver.find_element(by=By.NAME, value="session_key").send_keys("MAİL ADRESİNİZ")  # Maili gir
pw = driver.find_element(by=By.NAME, value="session_password").send_keys("ŞİFRENİZ")  # Şifreyi gir
driver.find_element(by=By.XPATH,
                    value="/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()  # Onaylama butonuna bas


for i in range(1, 100):
    driver.get(f'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22102105699%22%5D&keywords=data&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page={i}&sid=kcZ')  # Gitmek istediğimiz sayfa
    sleep(1)  # Sayfanın yüklenmesi için 1 saniye bekle

    ##################################################
    # TAKİP ET VE BAĞLANTI KUR "BUTONLARINI" YAKALAMA
    ##################################################
    submit_button = driver.find_elements(by=By.CSS_SELECTOR, value='button')  # CSS_SELECTOR ile yakalama
    # submit_button = driver.find_elements(by=By.XPATH, value='//span[@class="artdeco-button__text"]')  # XPATH ile yakalama

    """
    Yukarıdaki işlem sayfadaki tüm butonları getirecektir(arama butonu, üstteki iş ilanları, ağım vs. butonları). 
    Bize sadece bunların içerisinde "Bağlantı kur" ve "Takip Et" yazan butonlar gerekli. 
    Bulunan butonlar içerisindeki text'lere bakıp filtreleme yaparız. 
    """
    for i in submit_button:
        if i.text == "Bağlantı kur":
            i.click()  # bunlardan biriyse tıkla

            # Arada karşımıza çıkan "Davetiyeye not ekleyerek kişiselleştirebilirsiniz" penceresindeki "Gönder" butonuna tıklamak için
            try:
                gonder = driver.find_elements(by=By.CSS_SELECTOR, value='button')
                for g in gonder:
                   if g.text == "Gönder":
                       g.click()
            except:  # Eğer pencere açılmazsa koda devam et
                 continue