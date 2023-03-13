from selenium.webdriver.common.by import By


class admail_loctore:
    Phone_contact = (
    By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]")
    Code_contact = (
    By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]")
    Submit_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]")
    Sign_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]")
    chak_page = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[1]/div[1]/span[2]")
    oder_button = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/div[2]/a[5]/span[2]")
    checkOrederPage = (By.XPATH,
                       "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]")
    empty_fild = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/div[1]")
    last_page_button = (By.XPATH,
                        "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/span[5]/i[1]")
    last_page = (
    By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]")
    export_button = (
    By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/i[1]")
    rady_order=(By.XPATH,"//span[contains(text(),'מוכנה')]")
    list_oerder=(By.XPATH,"//tbody/tr[1]/td[1]")
    list_rady=(By.XPATH,"//span[contains(text(),'במשלוח')]")
    list_disply=(By.XPATH,"//tbody/tr[1]/td[1]")
    total_result=(By.XPATH,"//span[contains(text(),'סיום')]")
    sum_list=(By.XPATH,"//tbody/tr[17]/td[1]")
    search_button=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]")