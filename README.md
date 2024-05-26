# Установка
Клонировать репозиторий:  
```bash
git clone https://github.com/MixidFinder/selenium_language_testing.git
```

Создать `.venv` и активировать его:  
```bash
python -m venv .venv
.venv\Scripts\activate
```

Установить зависимости:  
```bash
pip install -r requirements.txt
```

# Использование
Запуск по умолчанию с `ru` языком:  
```bash
pytest
```

Параметризированный запуск:  
```bash
pytest --language=es
```
