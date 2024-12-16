***Инструкция по сборке***
---
1. Склонировать репозиторий
```
git clone https://github.com/Yashenkov22/test_frida.git
```
2. Перейти в папку
```
cd test_frida/frida-ios-hook/
```
3. Установить виртуальное окружение
```
python3 -m venv venv
```
4. Активировать виртуальное окружение
```
source venv/bin/activate
```
или
```
source ./venv/bin/activate
```
6. Перейти в папку с зависимостями
```
cd frida-ios-hook/
```
5. Установить зависимости
```
pip install -r requirements.txt
```
6. Собрать проект
```
python3 setup.py
```

7. Запустить скрипт
```
python3 main.py
```