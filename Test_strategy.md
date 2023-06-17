# Стратегия тестирования

## Дымововое тестирование:
- [ ] 1. Проверка разблокировки кнопки "Создать" после заполнения обязательных полей.
- [ ] 2. Проверка создания БД после нажатия на кнопку "Создать"
- [ ] 3. Проверка подключения к базе данных

## Функциональное тестирование:
Позитивные тесты на ввод данных:
- [ ] 1. Проверка на ввод корректного имени базы данных. 
- [ ] 2. Проверка на выбор корректного региона размещения.
- [ ] 3. Проверка на выбор корректного размера базы данных.

Негативные тесты на ввод данных:
- [ ] 4. Проверка на ввод cуществующего имени базы данных. 
- [ ] 5. Проверка на ввод имени базы данных с использованием недопустимых символов.

Тестирование работы БД:
- [ ] 1. Проверка создания базы данных.
- [ ] 2. Проверка возможности подключения к созданной базе данных через PostgreSQL клиент.
- [ ] 3. Проверка работы запросов создания\корректировки\выборки к базе данных.
- [ ] 4. Проверка возможности изменения параметров созданной базы данных (например, увеличение размера).
- [ ] 5. Проверка удаления базы данных.

## Тестирование безопасности:
- [ ] 1. Проверка осуществления доступа к учётной записи пользователя.
- [ ] 2. Проверка осуществления доступа к БД.

## Нагрузочное тестирование:
- [ ] 1. Проверка стабильности работы облачного сервиса при разном количестве одновременных запросов на создание БД.
- [ ] 2. Проверка стабильности работы базы данных при запуске разного количества одновременных запросов на чтение/запись данных.