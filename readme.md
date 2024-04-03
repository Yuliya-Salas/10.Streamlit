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

## Облачное развертывание Streamlit
 
1. Разместите свое приложение на GitHub (например, в этом репозитории). Убедитесь, что оно находится в общедоступной папке и что у вас есть файл requirements.txt.
   
2. Войдите в Streamlit Cloud. Войдите в Share.streamlit.io, указав свой адрес электронной почты GitHub. Вам потребуется доступ к сервису Streamlit Cloud.

3. Разверните и поделитесь!
Нажмите «Новое приложение», затем укажите репозиторий, ветку и путь к файлу, выберите версию Python (3.9 для этой демонстрации) и нажмите «Развернуть», после чего вы сможете увидеть свое приложение.
