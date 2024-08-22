
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys

bilgisayarlar = []

def main(ortalama_fiyat):  # Add ortalama_fiyat as a parameter
    
    class bilgisayar():
        def __init__(self, islemci, islemci_model, SSD, Ekran_Kartı, VRAM, RAM, Hz, puan, pc_fiyat ,URL):
            self.islemci = islemci
            self.islemci_model = islemci_model
            self.SSD = SSD
            self.Ekran_Kartı = Ekran_Kartı
            self.VRAM = VRAM
            self.RAM = RAM
            self.Hz = Hz
            self.puan = 0
            self.URL = URL
            self.pc_fiyat = pc_fiyat

        def puan_arttir(self,sayi):
            self.puan += sayi
        def puanyazdir(self):
            return self.puan

    options = Options()
    options.add_argument("--no-sandbox")
    

    #options.add_argument("--blink-settings=imagesEnabled=false")
    browser = webdriver.Edge(options=options)

    browser.minimize_window()
    browser.set_window_position(-10000, 0)
    browser.get("https://www.trendyol.com")
    time.sleep(0.4)
    arama_yeri = browser.find_element(By.XPATH, "//*[@id='sfx-discovery-search-suggestions']/div/div[1]/input")
    arama_yeri.send_keys("Oyuncu Dizüstü Bilgisayar")

    arama_tusu = browser.find_element(By.XPATH, "//*[@id='sfx-discovery-search-suggestions']/div/div/i")
    browser.execute_script("arguments[0].click();", arama_tusu)

    fiyat = WebDriverWait(browser, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='sticky-aggregations']/div/div[8]/div[1]/div[2]/i"))
            )
    browser.execute_script("arguments[0].click();", fiyat)

    time.sleep(0.5)

    min_fiyat = WebDriverWait(browser, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='sticky-aggregations']/div/div[8]/div[2]/div/input[1]"))
            )
    max_fiyat = WebDriverWait(browser, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='sticky-aggregations']/div/div[8]/div[2]/div/input[2]"))
            )
    
    #min_fiyat.clear()
    #max_fiyat.clear()
    
    min_fiyat.send_keys(str(ortalama_fiyat * 0.09))
    max_fiyat.send_keys(str(ortalama_fiyat * 0.11))

    time.sleep(2)

    fiyat_arama = browser.find_element(By.XPATH, "//*[@id='sticky-aggregations']/div/div[8]/div[2]/div/button")
    #browser.execute_script("arguments[0].click();", fiyat_arama)
    fiyat_arama.click()
    time.sleep(0.5)

    def scroll_page_incrementally():
        scroll_pause_time = 1
        last_height = browser.execute_script("return document.body.scrollHeight")
        
        while True:
            browser.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(scroll_pause_time)
            new_height = browser.execute_script("return document.body.scrollHeight")
            
            if new_height == last_height:
                break
            last_height = new_height

    scroll_page_incrementally()

    
    for i in range(2, 38):
        try:  # Sayfayı kaydırma işleminden sonra daha fazla bilgisayar taranabilir.
            if i == 18:
                scroll_page_incrementally()
                continue
            pc = browser.find_element(By.XPATH, "//*[@id='search-app']/div/div/div/div[2]/div[4]/div[1]/div/div[{}]/div[1]/a".format(i))
            browser.execute_script("arguments[0].click();", pc)
            
            browser.switch_to.window(browser.window_handles[1])
            
            islemci_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[1]/span[2]/b/div"))
            )
            islemci_str = islemci_element.text
            

            islemci_model_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[14]/span[2]/b/div"))
            )
            islemci_model_str = islemci_model_element.text
            

            if islemci_model_str == "8" or islemci_model_str == "6" or islemci_model_str == "10" or islemci_model_str == "12+" or islemci_model_str == "24" or islemci_model_str == "16" or islemci_model_str == "4":
                islemci_model_element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[13]/span[2]/b/div"))
            )
                
            islemci_model_str = islemci_model_element.text
                
            SSD_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[3]/span[2]/b/div"))
            )
            SSD_str = SSD_element.text
            

            Ekran_Kartı_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[7]/span[2]/b/div"))
            )
            Ekran_Kartı_str = Ekran_Kartı_element.text
            if Ekran_Kartı_str == "Resmi Distribütör Garantili":
                Ekran_Kartı_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[8]/span[2]/b/div"))
            )
            elif Ekran_Kartı_str == "15,6 inç":
                Ekran_Kartı_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[6]/span[2]/b/div"))
            )
            Ekran_Kartı_str = Ekran_Kartı_element.text
            

            VRAM_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[13]/span[2]/b/div"))
            )
            VRAM_str = VRAM_element.text
            

            if VRAM_str != "6 GB" and VRAM_str != "8 GB" and VRAM_str != "4 GB" and VRAM_str != "4 GB ve altı":
                VRAM_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[12]/span[2]/b/div"))
            )
                
            VRAM_str = VRAM_element.text

            RAM_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[2]/span[2]/b/div"))
            )
            RAM_str = RAM_element.text
        
            Hz_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[6]/span[2]/b/div"))
            )
            Hz_str = Hz_element.text
            if Hz_str == Ekran_Kartı_str:
                Hz_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/section/div/ul/li[10]/span[2]/b/div"))
            )
            Hz_str = Hz_element.text
            try:
                pc_fiyat = WebDriverWait(browser, 0.5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[4]/div/div/span"))
                )
            except:
                try:
                    pc_fiyat = WebDriverWait(browser, 0.4).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[4]/div/div/div/div[2]/span"))
                )
                except:
                    try:
                        pc_fiyat = WebDriverWait(browser, 0.1).until(
                            EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[4]/div/div/span"))
                    )
                    except:
                        try:
                            pc_fiyat = WebDriverWait(browser, 0.1).until(
                                EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[3]/div/div/span"))
                        )
                        except:
                            try:   
                                pc_fiyat = WebDriverWait(browser, 0.1).until(
                                    EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/span[2]"))
                            )
                            except:
                                try:
                                    pc_fiyat = WebDriverWait(browser, 0.1).until(
                                        EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/span"))
                                )
                                except:
                                    pc_fiyat = WebDriverWait(browser, 0.1).until(
                                        EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[2]/span"))
                                )
                                
            pc_fiyat_str = pc_fiyat.text

            pc_url = browser.current_url

            browser.close()  
            browser.switch_to.window(browser.window_handles[0])  
            
            pc = bilgisayar(islemci_str, islemci_model_str, SSD_str, Ekran_Kartı_str, VRAM_str, RAM_str, Hz_str, any,pc_fiyat_str, pc_url)
            bilgisayarlar.append(pc)

            time.sleep(0.1)
            print("Bilgisayarlar Taranıyor ({}/38)".format(i-1))
            taranıyor = "Bilgisayarlar Taranıyor ({}/38)".format(i-1)
        except Exception as e:
            browser.close()  
            browser.switch_to.window(browser.window_handles[0])
            print(f"Bir hata oluştu: {str(e)}")

    for i in bilgisayarlar:
        print(i.islemci + " / " + i.islemci_model + " / " + i.SSD + " / " + i.Ekran_Kartı + " / " + i.VRAM + " / " + i.RAM + " / " + i.pc_fiyat)

    time.sleep(2)

    amd_islemciler = ["AMD Ryzen 5","AMD Ryzen 7"]
    intel_islemciler = ["Intel Core i5","Intel Core i7"]
    amd_islemcinesilleri = ["5. Nesil","6. Nesil","7. Nesil",]
    intel_islemcimodelleri = ["10. Nesil","11. Nesil","12. Nesil","13. Nesil","14. Nesil",]
    ekrankarları = ["AMD Radeon Graphics","Dahili Ekran Kartı","Nvidia GeForce MX550","Nvidia GeForce RTX 2050 Laptop","Nvidia GeForce RTX 3050","AMD Radeon RX6500M","Nvidia GeForce RTX 3050 Ti","Nvidia GeForce RTX3060","Nvidia GeForce RTX 3070","Nvidia GeForce RTX 4050","Nvidia GeForce RTX 4060","Nvidia GeForce RTX 3070Ti","Nvidia GeForce RTX 4070","Nvidia GeForce RTX 4080","Nvidia GeForce RTX 4090"]
    ramler = ["8 GB","12 GB","16 GB","20 GB","24 GB","32 GB","36 GB","40 GB"]
    vramler = ["Paylaşımlı","4 GB ve altı","6 GB","8 GB","12 GB","16 GB"]
    ssd = ["256 GB","500 GB","512 GB","1 TB","2 TB"]

    

    for pc in bilgisayarlar:
        for i in range(0,len(amd_islemciler)):
            if pc.islemci == amd_islemciler[i]:
                pc.puan_arttir(i+1)
        for i in range(0,len(intel_islemciler)):
            if pc.islemci == intel_islemciler[i]:
                pc.puan_arttir(i+1)
        for i in range(0,len(ekrankarları)):
            if pc.Ekran_Kartı == ekrankarları[i]:
                pc.puan_arttir(i+1)
        for i in range(0,len(ramler)):
            if pc.RAM == ramler[i]:
                pc.puan_arttir(i+1)
        for i in range(0,len(vramler)):
            if pc.VRAM == vramler[i]:
                pc.puan_arttir(i+1)
        for i in range(0,len(ssd)):
            if pc.SSD == ssd[i]:
                pc.puan_arttir(i+1)
        print(pc.puan)
    # Diğer işlem kodları...
    max_object = max(bilgisayarlar, key=lambda obj: obj.puan)

    with open('data.txt', 'w') as file:
        file.write(str(max_object.URL))

    print(max_object.URL)

