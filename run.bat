@echo off
REM Скрипт быстрого запуска Goznak PPTX Generator для Windows
chcp 65001 >nul

echo 🚀 Запуск Goznak PPTX Generator...

REM Проверка нахождения в правильной директории
if not exist "start.py" (
    echo ❌ Ошибка: файл start.py не найден
    echo Убедитесь, что вы находитесь в директории проекта goznak_adhoc_script
    pause
    exit /b 1
)

REM Проверка наличия виртуального окружения
if not exist "venv" (
    echo ❌ Ошибка: виртуальное окружение не найдено
    echo Создайте виртуальное окружение командой: python -m venv venv
    pause
    exit /b 1
)

REM Активация виртуального окружения
echo 📦 Активация виртуального окружения...
call venv\Scripts\activate.bat

REM Запуск программы
echo 🎬 Запуск главного модуля...
python start.py

REM Пауза перед закрытием
echo.
echo 👋 Скрипт завершен. Нажмите любую клавишу для закрытия...
pause >nul