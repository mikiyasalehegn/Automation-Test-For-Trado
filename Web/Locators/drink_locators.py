from selenium.webdriver.common.by import By


class Drink_Locators:
    option1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]')
    option2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    save = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    drink_page = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/a[3]/div/img")
    drink_text = (
        By.XPATH, '//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[3]/div[1]/div[1]')
    drink_english_text = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/a[3]/div/div')
    drink = (
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[4]")

    milk = (By.XPATH,
            "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[2]/div[1]/div[2]/div[2]/div[1]")
    currency = (By.XPATH, "//div[contains(text(),'goats milk')]")
    addcart = (By.XPATH,
               "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[2]/div[1]/div[2]")
    add_list_disply = (By.XPATH,
                       "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]")

    deleted_button = (By.XPATH,
                      "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/div[1]/div[3]/div[2]/img[1]")
    empty_list = (By.XPATH, "//h5[contains(text(),'העגלה שלך ריקה')]")
    pyment = (By.XPATH, "//button[contains(text(),'תשלום')]")
    pyment_page = (By.XPATH, "//h2[contains(text(),'ברוכים השבים! מתרגשים לראות אתכם כאן')]")
    mianes_button = (By.XPATH,
                     "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[3]/div[1]/div[1]/span[2]/i[1]")
    add_button = (By.XPATH,
                  "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]")
    display_list = (By.XPATH,
                    "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[3]")
    x_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/span[1]/i[1]")
    signin = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
    google_button = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/img[1]")
    ok_button = (By.XPATH,
                 "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]/span[1]/span[1]/i[1]")
    signin_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]")
    signup_registor_button = (By.XPATH, "//span[contains(text(),'הרשם')]")
    facebook_button = (
        By.XPATH,
        "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/button[1]/img[1]")
    tweeter_button = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/img[1]")
    phone_filed = (
        By.XPATH,
        "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]/input[1]")