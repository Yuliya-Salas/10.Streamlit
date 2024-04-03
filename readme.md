# Streamlit демо

Этот проект демонстрирует данные в виде веб-приложени] с использованием платформы [Streamlit](https://www.streamlit.io/). Данные, используемые в этом репозитории, представляют собой набор даных ["Качество бананов"](https://www.kaggle.com/datasets/l3llff/banana) и ["Производство бананов в мире"](https://www.kaggle.com/datasets/whenamancodes/banana-production-minion-loves-banana) c Kaggle.

Попробуйте приложение [здесь](https://first-project-salasvallejos.streamlit.app/)!

## Файлы

- `1_🌎_map.py` и `2_📉_correlation.py`: файлы приложения с потоковой подсветкой
- `banana_quality.csv` и `banana-production.csv`: файлы данных
- `requirements.txt`: файлы требований к пакету
- `countries.geo.json`: содержит географические данные о странах в формате JSON
- `Dockerfile` для развертывания докера

## Запустить демонстрацию локально

### Оболочка

Для прямого запуска streamlit локально в корневой папке репо следующим образом::

```shell
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run 1_🌎_map.py
```
Откройте http://localhost:8501 чтобы просмотреть приложение.

### Docker

For build and run the docker image named `st-demo`:

```
$ docker build -t st-demo .
$ docker run -it --rm -p '8501:8501' st-demo
```

`-it` keeps the terminal interactive

`--rm` removes the image once the command is stopped (e.g. using control + c)

Open http://localhost:8501/ to view the app.

## Streamlit Cloud Deployment
 
1. Put your app on GitHub (like this repo)
Make sure it's in a public folder and that you have a `requirements.txt` file.
 
2. Sign into Streamlit Cloud
Sign into share.streamlit.io with your GitHub email address, you need to have access to Streamlit Cloud service.
 
3. Deploy and share!  
Click "New app", then fill in your repo, branch, and file path, choose a Python version (3.9 for this demo) and click "Deploy", then you should be able to see your app.
