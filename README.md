# Plane tracker
## Описание:
Plane tracker - моя курсовая работа по ООП
## Установка:
1. Клонируйте репозиторий
```
git clone https://github.com/LexaNovikov/Plane-tracker.git
```

2. Установите poetry
```
pip install poetry
```
 
3. Инициализируйте poetry
```
poetry init
```

4. Установите зависимости
```
poetry install
```

## Использование:
Запустите pytest в директории tests

```
pytest ./tests
``` 

## Документация:
### В пакете ```src``` лежат модули кода:

```connect_class.py```
Содержит класс AeroplanesAPI и его методы и данные 

```plane_class.py```
Содержит класс Aeroplane и его методы и данные 

```saver_class.py``` 
Содержит класс JSONSaver и его методы и данные

В пакете ```tests``` содержатся модули и файлы для тестирования функций

```conftest.py```
Модуль, содержащий фикстуры pytest

```test_connect_class.py```
Модуль тестирования, предназначенный для тестирования функции методов класса ```connect_class.py```

```test_plane_class.py```
Модуль тестирования, предназначенный для тестирования функции методов класса ```plane_class.py```

```test_saver_class.py```
Модуль тестирования, предназначенный для тестирования функции методов класса ```saver_class.py```

