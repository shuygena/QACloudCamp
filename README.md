# QACloudCamp
Тестовое задание для поступления в QACloudCamp

## :clipboard: Содержание

1. Процесс тестирования нового функционала  
[Стратегия тестирования](https://github.com/shuygena/QACloudCamp/blob/main/Test_strategy.md)
2. Автоматизация тестирования API. Часть 1  
[Тесты](https://github.com/shuygena/QACloudCamp/blob/main/tests/test_api.py)
3. Автоматизация тестирования API. Часть 2  
[Dockerfile](https://github.com/shuygena/QACloudCamp/blob/main/Dockerfile)

## :link: Загрузка и запуск проекта
Склонируйте репозиторий:
```
git clone https://github.com/shuygena/QACloudCamp QACloudCamp
```
Перейдите в директорию:
```
cd QACloudCamp
```
Создайте виртуальное окружение:
```
python3 -m venv venv
```
Активируйте виртуальное окружение:
```
source venv/bin/activate
```
Установите требуемые пакеты:  
```
python3 -m pip install -r requirements.txt
```
Запустите:   
```
python3 -m pytest -v
``` 

## :whale: Загрузка и запуск проекта с Docker
Склонируйте репозиторий:
```
git clone https://github.com/shuygena/QACloudCamp QACloudCamp
```
Перейдите в директорию:
```
cd QACloudCamp
```
Создайте образ:
```
docker build -t myapp 
```
Запустите:
```
docker run myapp 
```
 

