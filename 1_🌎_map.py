import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(
    page_title='Bananas',
    page_icon='🍌',
    layout="wide",
    initial_sidebar_state="auto",
)

st.title('Экспорт бананов')
st.write('''Бананы — одна из древнейших пищевых культур, а для тропических стран — важнейшее пищевое растение и главная статья экспорта. 
         Спелые бананы широко употребляются в пищу по всему миру, их используют при приготовлении большого количества блюд''')
st.write('На карте показаны данные об объеме производства бананов с 1960г по 2021г по странам в тоннах')
st.write('''Как видно из табличных данных и на карте - с каждым годом спрос на бананы растет. 
         Одна только африка за последние 40 лет увеличила объем экспорта более чем в 7 раз. 
         Ниже, на карте, в интерактивном режиме можно посмотреть как менялся обьем производства бананов во всем мире''')


DATA = 'banana-production.csv'
DATE_COLUMN = 'Year'

def load_data():
    df = pd.read_csv(DATA, parse_dates=[DATE_COLUMN], delimiter=',')
    df[DATE_COLUMN] = df[DATE_COLUMN].dt.strftime('%Y')  # Преобразуем год к строковому формату, пробуем исправить ошибку при развертывании
    return df

df = load_data()

with open('countries.geo.json') as json_file:
    json_locations = json.load(json_file)

def draw_map_cases():
    fig = px.choropleth_mapbox(
        df,
        geojson=json_locations,
        locations='Code',
        color='Bananas',
        color_continuous_scale='brwnyl',
        mapbox_style='carto-positron',
        title='Объем производства бананов, в тоннах',
        zoom=1,
        opacity=0.5,
        animation_frame='Year'  # Добавляем параметр анимации по годам
    )
    fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    return fig

st.plotly_chart(draw_map_cases())

show_data = st.sidebar.checkbox('Показать необработанные данные объемов производства бананов')
if show_data:
    st.subheader('Необработанные данные')
    st.markdown("#### Данные об объеме производства бананов с 1960г по 2021г [здесь](https://www.kaggle.com/datasets/whenamancodes/banana-production-minion-loves-banana).")
    st.write(df)

