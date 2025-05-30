## Описание файлов

- `task_1.py` — скрипт на Python, которая выполняет следующие задачи:
  - читает список чисел от пользователя
  - выводит чётные числа
  - находит и выводит максимальное и минимальное число из списка
  - сортирует числа в порядке возрастания

- `task_2.py` — автоматизация с помощью Selenium:
  - открывает веб-страницу `https://example.com`
  - проверяет заголовок страницы
  - кликает по ссылке "More information..."
  - проверяет переход по URL

## Как запустить

### 1. Установить зависимости

Убедитесь, что у вас установлен Python 3.9+ или выше.

```bash
python3 --version
```

Если Python не установлен, его можно скачать с официального сайта.

Затем установите Selenium:

```bash
pip install selenium
```

### 2. Установить ChromeDriver

Selenium использует ChromeDriver для управления браузером.

#### Шаги:

1. Откройте **Google Chrome** и перейдите на сайт:[https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)
2. Найдите нужную версию и скачайте драйвер для своей ОС.
3. Распакуйте и поместите файл `chromedriver` в папку со скриптами.


### 3. Клонировать репозиторий

Откройте терминал и выполните:
```bash
git clone https://github.com/Anastasia-KKK/test-assignment.git
cd test-assignment
```

### 4. Запуск скриптов

1. Откройте папку проекта.
2. Откройте терминал в этой папке:

```bash
cd /путь/до/папки
```

3. Запустите скрипты:

Для файла `task_1.py`:
```bash
   python3 task_1.py
```

Для файла `task_2.py`:
```bash
   python3 task_2.py
```
## Используемые версии и инструменты

Для выполнения задания были использованы следующие инструменты и библиотеки:

| Инструмент      | Версия                  |
|-----------------|-------------------------|
| Python          | 3.13.2                  |
| Selenium        | 4.32.0                  |
| Google Chrome   | 136.0.7103.93 (arm64)   |
| ChromeDriver    | 114.0.5735.90           |
