# Universal Runner Script (run.sh)

## Описание

`run.sh` - это универсальный скрипт для автоматической настройки окружения и запуска Goznak PPTX Generator. Скрипт полностью автоматизирует процесс установки, обновления и проверки всех компонентов системы.

## 🚀 Быстрый запуск

```bash
cd /Users/NVE/Documents/my_program/goznak_adhoc_script
./run.sh
```

**Всё.** Скрипт сделает всё остальное автоматически.

## ✨ Возможности

### 🔧 Автоматическая настройка окружения
- **Проверка Python** - автоматическая проверка наличия Python 3.7+
- **Создание/обновление venv** - умное управление виртуальным окружением
- **Сравнение версий Python** - пересоздание venv при несовместимости
- **Обновление pip** - автоматическое обновление до последней версии

### 📚 Управление зависимостями
- **Базовые библиотеки**: python-pptx, requests, tqdm
- **OpenAI библиотека**: автоматическая установка для GPT-Image-1
- **Проверка версий** - обновление только при необходимости
- **Восстановление при сбоях** - автоматическое переустановка поврежденных пакетов

### 🔍 Комплексная диагностика
- **Проверка импортов** - тестирование всех критических модулей
- **Проверка файлов проекта** - валидация структуры директорий
- **Функциональное тестирование** - проверка работоспособности OpenAI API
- **Создание отчетов** - генерация environment_info.txt

### 🎨 Интерфейс
- **Цветной вывод** - информативные сообщения с цветовым кодированием
- **Детальные этапы** - пошаговое отображение прогресса
- **Информативные ошибки** - точная диагностика проблем

## 📋 Этапы выполнения

### Этап 1: Проверка Python
```bash
[INFO] Python найден: Python 3.13.1
```

### Этап 2: Настройка виртуального окружения
```bash
[INFO] Виртуальное окружение существует, проверяем актуальность...
[INFO] Python в venv: Python 3.13.1
[SUCCESS] Виртуальное окружение актуально
[SUCCESS] Виртуальное окружение активировано
```

### Этап 3: Обновление менеджера пакетов
```bash
[INFO] Обновление pip до последней версии...
[SUCCESS] pip обновлен: pip 25.1.1
```

### Этап 4: Установка и обновление зависимостей
```bash
[INFO] Установка базовых зависимостей...
[SUCCESS] Базовые зависимости установлены
[INFO] Проверка OpenAI библиотеки...
[SUCCESS] OpenAI уже установлена: 1.82.1
[SUCCESS] Версия OpenAI соответствует требованиям (>= 1.0.0)
```

### Этап 5: Проверка целостности зависимостей
```bash
[SUCCESS] ✓ python-pptx - OK
[SUCCESS] ✓ requests - OK
[SUCCESS] ✓ tqdm - OK
[SUCCESS] ✓ openai - OK
```

### Этап 6: Проверка файлов проекта
```bash
[SUCCESS] ✓ Основной скрипт: goznak_pptx_generator.py
[SUCCESS] ✓ Контент слайдов: pptx_content/slide_content.txt
[SUCCESS] ✓ Шаблон презентации: pptx_template/Шаблон презентации 16х9.pptx
```

### Этап 7: Тестирование функциональности
```bash
[INFO] Тестирование импортов Python...
✓ Все критические модули импортированы успешно
✓ OpenAI клиент функционален
✓ Все тесты пройдены успешно
[SUCCESS] Функциональное тестирование завершено успешно
```

### Этап 8: Обновление информационных файлов
```bash
[SUCCESS] Информация об окружении сохранена: environment_info.txt
```

### Этап 9: Финальная проверка и запуск
```bash
[SUCCESS] Все системы готовы к запуску!
🚀 ЗАПУСК GOZNAK PPTX GENERATOR
```

## 🛠️ Решение проблем

### Автоматическое восстановление
Скрипт включает механизмы автоматического восстановления:

1. **Поврежденное виртуальное окружение** - пересоздание
2. **Устаревшие версии Python** - обновление venv
3. **Отсутствующие зависимости** - автоматическая установка
4. **Поврежденные пакеты** - переустановка с --force-reinstall

### Обработка ошибок
```bash
[ERROR] Python3 не найден! Установите Python 3.7+ и повторите попытку.
[WARNING] Версии Python не совпадают (система: 3.13, venv: 3.12)
[INFO] Пересоздаем виртуальное окружение...
```

### Диагностика проблем
Если возникают проблемы, проверьте:

1. **environment_info.txt** - детальная информация об окружении
2. **Цветные сообщения** - красный = ошибка, желтый = предупреждение
3. **Коды выхода** - `echo $?` для определения типа ошибки

## 🎯 Преимущества

### Для пользователя
- **Одна команда** - `./run.sh` запускает всё
- **Нет ручной настройки** - полная автоматизация
- **Актуальные зависимости** - всегда последние совместимые версии
- **Надежность** - автоматическое восстановление при сбоях

### Для системы
- **Изолированная среда** - использование виртуального окружения
- **Проверка совместимости** - валидация версий Python и библиотек
- **Детальная диагностика** - полное тестирование перед запуском
- **Информативность** - подробные логи и отчеты

## 📁 Создаваемые файлы

### environment_info.txt
Содержит полную информацию об окружении:
```
Goznak PPTX Generator - Environment Information
===============================================
Дата создания: Mon Jun  2 05:30:00 PDT 2025
Рабочая директория: /Users/NVE/Documents/my_program/goznak_adhoc_script
Python версия: Python 3.13.1
Virtual Environment: /path/to/venv

Установленные пакеты:
openai==1.82.1
python-pptx==0.6.23
requests==2.32.3
tqdm==4.67.1

Статус: ГОТОВ К РАБОТЕ ✓
```

## 🔄 Совместимость

### Операционные системы
- ✅ **macOS** - полная поддержка
- ✅ **Linux** - полная поддержка  
- ⚠️ **Windows** - требует WSL или Git Bash

### Версии Python
- ✅ **Python 3.7+** - минимальная версия
- ✅ **Python 3.8-3.11** - тестированные версии
- ✅ **Python 3.12+** - последние версии

## 🚨 Требования системы

### Минимальные требования
- **Bash shell** - для выполнения скрипта
- **Python 3.7+** - основная среда выполнения
- **Internet connection** - для загрузки пакетов
- **~100MB свободного места** - для виртуального окружения

### Рекомендуемые требования
- **Python 3.10+** - оптимальная производительность
- **1GB RAM** - комфортная работа
- **Стабильное соединение** - быстрая установка пакетов

## 🎉 Результат

После успешного выполнения `./run.sh`:

1. ✅ **Виртуальное окружение** настроено и активировано
2. ✅ **Все зависимости** установлены и проверены
3. ✅ **OpenAI библиотека** готова для GPT-Image-1
4. ✅ **Файлы проекта** проверены и валидны
5. ✅ **Goznak PPTX Generator** автоматически запущен

**Один скрипт - полная настройка - немедленный запуск!**

---

*Universal Runner обеспечивает надежный, автоматизированный и user-friendly способ запуска Goznak PPTX Generator с минимальными усилиями пользователя.*