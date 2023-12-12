from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd

driver = webdriver.Chrome()

driver.get('https://www.pravda.com.ua/archives/')
driver.maximize_window()

#Створюємо посилання для вказаної дати
format_link = lambda day, month, year: f"https://www.pravda.com.ua/archives/date_{day}{month}{year}/"

#Створюємо пустий DataFrame для зберігання даних
df = pd.DataFrame(columns=['Date', 'Text'])

#Функція для оновлення DataFrame та збереження у CSV
def update_df(text, date):
    global df
    df = pd.concat([df, pd.DataFrame({'Date': date, 'Text': [text]})], ignore_index=True)
    df.to_csv('555.csv', index=False)

#Функція для обробки сторінки новин
def process_page_news(link, date):
    try:
        #Заходимо на сторінку зі списком новин
        driver.get(link)
        #Знаходимо всі посилання на новини на даній сторінці
        articles = driver.find_elements(By.CSS_SELECTOR, 'div.article.article_list a[href]')

        #Обробляємо кожну новину
        for article in articles:
            try:
                #Отримуємо посилання на новину
                article_link = article.get_attribute('href')
                
                #Опрацювання різних типів посилань на статті
                if 'epravda.com.ua' in article_link or 'eurointegration.com.ua' in article_link or 'pravda.com.ua' in article_link:
                    driver.get(article_link)
                    main_div = driver.find_elements(By.CSS_SELECTOR, 'div.post__text p')
                    text = [p.text for p in main_div]
                    update_df(text, date)
                elif 'life.pravda.com.ua' in article_link:
                    driver.get(article_link)
                    main_div = driver.find_elements(By.CSS_SELECTOR, 'article.article p')
                    text = [p.text for p in main_div]
                    update_df(text, date)
                else:
                    pass
                driver.back()
                
                #Ігноруємо вийняття про застарілий елемент
            except StaleElementReferenceException:
                pass
        #Обробка інших винятків, якщо такі є
    except Exception as e:
        print(f"An error occurred: {e}")

#Цикли для обробки новин за роками та місяцями
for year in [2023]:
    for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]:
        process_page_news(format_link("02", month, year), f'02-{month}-{year}')

driver.quit()
