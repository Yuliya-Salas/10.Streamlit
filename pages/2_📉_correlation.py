import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image


# Настройка страницы
st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
    page_title="Качество бананов",
    page_icon="🍌",
)
# Отображение изображения
st.image("banana.png")

# Отображение заголовка и текста
st.write(
    """
    # Качество бананов
    Давайте посмотрим как вкусовые качества, размер, мягкость и время, прошедшее с момента сбора урожая, влияют друг на друга.
    На панели слева Вы можете выбрать интересующие Вас показатели и посмотреть их взаимосвязь.
    """
)


# у нас есть данные в DataFrame, назвала 'fruit_data'
fruit_data = pd.read_csv("banana_quality.csv", delimiter=",")

# Настройка боковой панели
# Создаем список доступных полей для выбора
fields = ["Weight", "Sweetness", "Softness", "HarvestTime", "Ripeness", "Acidity"]

# Выбираем первое поле для корреляции
first_field = st.sidebar.selectbox("Выберите первое поле для корреляции", fields)

# Выбираем второе поле для корреляции
second_field = st.sidebar.selectbox("Выберите второе поле для корреляции", fields)

# Вычисляем корреляцию между выбранными полями
correlation = fruit_data[first_field].corr(fruit_data[second_field])

# Создаем корреляционную диаграмму
fig, ax = plt.subplots()
plt.scatter(fruit_data[first_field], fruit_data[second_field])
plt.title(f"Корреляция между {first_field} и {second_field}")
plt.xlabel(first_field)
plt.ylabel(second_field)
plt.text(
    0.5, 0.5, f"Pearson's r = {correlation:.2f}", fontsize=14, transform=ax.transAxes
)

st.set_option(
    "deprecation.showPyplotGlobalUse", False
)  # убирает надпись PyplotGlobalUseWarning : вызываете st.pyplot() без каких-либо аргументов

# Отображаем диаграмму в Streamlit
st.pyplot()

# настраиваю чекбокс для отображения первоначальной таблицы
show_data = st.sidebar.checkbox("Показать необработанные данные(таблицу)")
if show_data == True:
    st.subheader("Необработанные данные")
    st.markdown(
        "#### Данные 'Качество бананов' можно найти [здесь](https://github.com/Yuliya-Salas/10.Streamlit/blob/main/banana_quality.csv)."
    )
    st.write(fruit_data)
