# **Check Version Digispot**

Этот скрипт предназначен для проверки версий исполняемых файлов Digispot в указанных путях из CSV-файла.    
Он особенно полезен для поиска файлов версии 2.x, даже если они имеют такое же имя, как и другие версии.

## __Функциональность__
Чтение списка путей из CSV-файла.   
Проверка версий указанных исполняемых файлов: "djin.exe mag2.exe mediaplanner.exe track2.exe ddb.exe".    
Автоматический поиск версии 2.x файла в той же директории, если текущая версия не 2.x.    
Запись результатов в текстовый файл.    

## __Требования__
Python 3.x    
Модуль pywin32 (для работы с версиями Windows-файлов)

## __Установите необходимые зависимости:__
```bash
pip install pywin32
```

## __Использование__
Подготовьте CSV-файл (Digispot-BackupDJin.csv) с путями к проверяемым файлам/папкам

## __Запустите скрипт:__
```
python check_versions.py
```
Результаты будут сохранены в файл output.txt в формате:
[полный путь к файлу] [версия]

## __Особенности__
Скрипт проверяет как конкретные файлы, так и все целевые исполняемые файлы в указанных директориях
Поддерживается поиск файлов версии 2.x с тем же именем в той же папке (регистронезависимый поиск)
Обрабатываются ошибки доступа к файлам и чтения их версий.    
##__Выходные данные__    
Для каждого найденного файла выводится:    
Полный путь к файлу    
Версия файла (в формате X.X.X.X)    
Если версия не 2.x, но в той же папке найден файл с версией 2.x - будет использована версия 2.x    
Для файлов, которые не удалось проверить, версия указывается как "N/A".    
