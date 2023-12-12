import pandas as pd
import re
import matplotlib.pyplot as plt
import calendar

# Зчитуємо список стоп-слів з файлу
with open('words_ua.txt', 'r', encoding='utf-8') as f:
    stop_words_list = [line.strip().lower() for line in f]

# Зчитуємо дані з CSV-файлу
df = pd.read_csv('555.csv')

# Розділяємо дату на окремі стовпці "Year" та "Month"
df['Year'] = pd.to_datetime(df['Date']).dt.year
df['Month'] = pd.to_datetime(df['Date']).dt.month

# Функція для очищення тексту
def clean_text(text):
    words = re.findall(r'\b\w+\b', text.lower(), flags=re.UNICODE)
    return [word for word in words if word not in stop_words_list]

# Групуємо дані по роках та місяцях та об'єднуємо текст новин у кожній групі
grouped_data = df.groupby(['Year', 'Month'])['Text'].apply(' '.join).reset_index()

# Проводимо аналіз для кожного періоду
for index, row in grouped_data.iterrows():
    words = clean_text(row['Text'])
    word_freq = pd.Series(words).value_counts().reset_index()
    word_freq.columns = ['Word', 'Frequency']

    # Виводимо найбільш популярні слова для кожного періоду
    print(f"Popular words in {calendar.month_name[row['Month']]} {row['Year']}:\n")
    print(word_freq.head(10))  # Приклад виведення топ-10 слів

    # Візуалізація графіків частоти слів для кожного періоду
    plt.figure(figsize=(10, 6))
    plt.bar(word_freq['Word'][:10], word_freq['Frequency'][:10])
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f"Top 10 words in {calendar.month_name[row['Month']]} {row['Year']}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
