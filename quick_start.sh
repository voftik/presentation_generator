#!/bin/bash
# -*- coding: utf-8 -*-
# RW Tech PPTX Generator - Quick Start Script (Simplified)

set -e

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Получение пути к скрипту
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${PURPLE}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║        🚀 RW TECH PPTX GENERATOR - QUICK START 🚀           ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo -e "${CYAN}📂 Рабочая директория: ${SCRIPT_DIR}${NC}"

# Проверка Python
echo -e "\n${BLUE}🐍 Проверка Python...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Python найден: ${PYTHON_VERSION}${NC}"
else
    echo -e "${RED}❌ Python3 не найден!${NC}"
    exit 1
fi

# Настройка виртуального окружения
VENV_DIR="$SCRIPT_DIR/venv"
echo -e "\n${BLUE}🏗️ Настройка виртуального окружения...${NC}"

if [ ! -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}⚠️  Создание виртуального окружения...${NC}"
    python3 -m venv "$VENV_DIR"
fi

# Простая активация через PATH
export PATH="$VENV_DIR/bin:$PATH"
export VIRTUAL_ENV="$VENV_DIR"

if [ -x "$VENV_DIR/bin/python" ]; then
    echo -e "${GREEN}✓ Виртуальное окружение готово${NC}"
else
    echo -e "${RED}❌ Ошибка настройки виртуального окружения${NC}"
    exit 1
fi

# Проверка и установка зависимостей
echo -e "\n${BLUE}📦 Проверка зависимостей...${NC}"

# Функция для проверки пакета
check_and_install() {
    local package=$1
    local import_name=${2:-$1}
    
    if "$VENV_DIR/bin/python" -c "import $import_name" 2>/dev/null; then
        echo -e "${GREEN}✓ $package установлен${NC}"
    else
        echo -e "${YELLOW}📦 Установка $package...${NC}"
        "$VENV_DIR/bin/pip" install "$package" --quiet
        if "$VENV_DIR/bin/python" -c "import $import_name" 2>/dev/null; then
            echo -e "${GREEN}✓ $package успешно установлен${NC}"
        else
            echo -e "${RED}❌ Ошибка установки $package${NC}"
            exit 1
        fi
    fi
}

# Обновление pip
"$VENV_DIR/bin/python" -m pip install --upgrade pip --quiet

# Проверка основных зависимостей
check_and_install "python-pptx" "pptx"
check_and_install "requests" "requests"
check_and_install "tqdm" "tqdm"

# Опциональные зависимости для AI
echo -e "${CYAN}🤖 Проверка AI зависимостей (опционально)...${NC}"
check_and_install "openai>=1.0.0" "openai" || echo -e "${YELLOW}⚠️  OpenAI пропущен${NC}"
check_and_install "google-genai" "google.genai" || echo -e "${YELLOW}⚠️  Google GenAI пропущен${NC}"

# Проверка файлов проекта
echo -e "\n${BLUE}📁 Проверка файлов проекта...${NC}"

if [ -f "$SCRIPT_DIR/rwtech_pptx_generator.py" ]; then
    echo -e "${GREEN}✓ Основной скрипт найден${NC}"
else
    echo -e "${RED}❌ rwtech_pptx_generator.py не найден!${NC}"
    exit 1
fi

if [ -f "$SCRIPT_DIR/pptx_content/slide_content.txt" ]; then
    echo -e "${GREEN}✓ Контент для слайдов найден${NC}"
else
    echo -e "${YELLOW}⚠️  slide_content.txt не найден в pptx_content/${NC}"
fi

if [ -f "$SCRIPT_DIR/pptx_template/Шаблон презентации 16х9.pptx" ]; then
    echo -e "${GREEN}✓ Шаблон презентации найден${NC}"
else
    echo -e "${YELLOW}⚠️  Шаблон презентации не найден в pptx_template/${NC}"
fi

# Создание необходимых директорий
mkdir -p "$SCRIPT_DIR/pptx_result" "$SCRIPT_DIR/logs" "$SCRIPT_DIR/prompts_for_img" "$SCRIPT_DIR/img_generated"

echo -e "\n${GREEN}🎉 Система готова к запуску!${NC}"
echo -e "${PURPLE}"
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║    🚀 ЗАПУСК RW TECH PPTX GENERATOR 🚀                        ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Запуск основного скрипта
echo -e "${CYAN}🔄 Запуск генератора...${NC}"
exec "$VENV_DIR/bin/python" "$SCRIPT_DIR/rwtech_pptx_generator.py"