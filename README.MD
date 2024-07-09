Трекер задач

Стэк: fastapi, sqlalchemy, aisqlite, uvicorn

### Локальный запуск проекта:

**_Склонировать репозиторий к себе_**
```
git@github.com:TatianaSharova/task_tracker.git
```
**_Создать и активировать виртуальное окружение:_**

Для Linux/macOS:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Для Windows:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
**_Установить зависимости из файла requirements.txt:_**
```
pip install -r requirements.txt
```
**_Запустить проект:_**
```
uvicorn main:app
```
**_Документация к проекту будет доступна по адресу:_**
http://127.0.0.1:8000/docs