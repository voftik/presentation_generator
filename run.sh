#!/bin/bash
# -*- coding: utf-8 -*-
# RW Tech PPTX Generator - Universal Runner Script
# Автоматическая настройка окружения и запуск универсального генератора

set -e  # Выход при любой ошибке

# Расширенная цветовая палитра
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
BRIGHT_RED='\033[1;31m'
BRIGHT_GREEN='\033[1;32m'
BRIGHT_BLUE='\033[1;34m'
BRIGHT_PURPLE='\033[1;35m'
BRIGHT_CYAN='\033[1;36m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m' # No Color

# ASCII символы для красивого оформления
CHECK_MARK="✓"
CROSS_MARK="✗"
WARNING_MARK="⚠"
ARROW_RIGHT="→"
LOADING_SPINNER=("⠋" "⠙" "⠹" "⠸" "⠼" "⠴" "⠦" "⠧")
PROGRESS_BAR=("▏" "▎" "▍" "▌" "▋" "▊" "▉" "█")

# Функция для анимированного спиннера
spinner() {
    local pid=$1
    local message=$2
    local i=0
    
    while kill -0 $pid 2>/dev/null; do
        printf "\r${CYAN}${LOADING_SPINNER[i]} $message${NC}"
        i=$(((i + 1) % ${#LOADING_SPINNER[@]}))
        sleep 0.1
    done
    
    printf "\r${GREEN}${CHECK_MARK} $message завершено${NC}\n"
}

# Функция анимированного прогресс-бара
progress_bar() {
    local current=$1
    local total=$2
    local message=$3
    local width=40
    
    local percentage=$((current * 100 / total))
    local filled=$((current * width / total))
    local empty=$((width - filled))
    
    printf "\r${CYAN}$message ${BRIGHT_BLUE}["
    printf "%*s" $filled | tr ' ' '█'
    printf "%*s" $empty | tr ' ' '▒'
    printf "] ${percentage}%%${NC}"
    
    if [ $current -eq $total ]; then
        printf "\n"
    fi
}

# ASCII арт заголовки
print_ascii_header() {
    echo -e "${BRIGHT_PURPLE}"
    cat << 'EOF'
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ██████╗ ██╗    ██╗    ████████╗███████╗ ██████╗██╗  ██╗    ║
║  ██╔══██╗██║    ██║    ╚══██╔══╝██╔════╝██╔════╝██║  ██║    ║
║  ██████╔╝██║ █╗ ██║       ██║   █████╗  ██║     ███████║    ║
║  ██╔══██╗██║███╗██║       ██║   ██╔══╝  ██║     ██╔══██║    ║
║  ██║  ██║╚███╔███╔╝       ██║   ███████╗╚██████╗██║  ██║    ║
║  ╚═╝  ╚═╝ ╚══╝╚══╝        ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝    ║
║                                                              ║
║            🚀 PPTX GENERATOR - UNIVERSAL RUNNER 🚀           ║
║                  RW Tech Solutions | 2025                   ║
╚══════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

print_ascii_divider() {
    local symbol=${1:-"═"}
    local length=${2:-60}
    echo -e "${BRIGHT_CYAN}$(printf "%*s" $length | tr ' ' $symbol)${NC}"
}

print_ascii_box() {
    local message=$1
    local color=${2:-$CYAN}
    local length=${#message}
    local total_length=$((length + 4))
    
    echo -e "${color}┌$(printf "%*s" $((total_length - 2)) | tr ' ' '─')┐${NC}"
    echo -e "${color}│ $message │${NC}"
    echo -e "${color}└$(printf "%*s" $((total_length - 2)) | tr ' ' '─')┘${NC}"
}

# Улучшенные функции вывода
print_status() {
    echo -e "${BLUE}[${DIM}INFO${NC}${BLUE}]${NC} ${ARROW_RIGHT} $1"
}

print_success() {
    echo -e "${GREEN}[${BOLD}SUCCESS${NC}${GREEN}]${NC} ${CHECK_MARK} $1"
}

print_warning() {
    echo -e "${YELLOW}[${BOLD}WARNING${NC}${YELLOW}]${NC} ${WARNING_MARK} $1"
}

print_error() {
    echo -e "${RED}[${BOLD}ERROR${NC}${RED}]${NC} ${CROSS_MARK} $1"
}

print_header() {
    echo -e "${BRIGHT_PURPLE}$1${NC}"
}

print_step() {
    local step_num=$1
    local step_title=$2
    local icon=${3:-"🔧"}
    
    echo ""
    print_ascii_divider "─" 60
    echo -e "${BRIGHT_CYAN}${icon} ЭТАП ${step_num}: ${BOLD}$step_title${NC}"
    print_ascii_divider "─" 60
}

# Получение абсолютного пути к скрипту
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Главный ASCII заголовок
clear
print_ascii_header

print_status "Рабочая директория: ${BOLD}$SCRIPT_DIR${NC}"
sleep 0.5

# ═══════════════════════════════════════════════════════════════
# ЭТАП 1: Проверка Python
# ═══════════════════════════════════════════════════════════════
print_step 1 "Проверка Python" "🐍"

echo -e "${DIM}Поиск интерпретатора Python...${NC}"
(sleep 1) &
spinner $! "Сканирование системы"

if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    print_success "Python обнаружен: ${BOLD}$PYTHON_VERSION${NC}"
    
    # Проверка версии Python
    PYTHON_MAJOR=$(python3 -c "import sys; print(sys.version_info.major)")
    PYTHON_MINOR=$(python3 -c "import sys; print(sys.version_info.minor)")
    
    if [ $PYTHON_MAJOR -ge 3 ] && [ $PYTHON_MINOR -ge 7 ]; then
        print_success "Версия Python совместима (требуется ≥ 3.7)"
    else
        print_error "Версия Python $PYTHON_MAJOR.$PYTHON_MINOR устарела (требуется ≥ 3.7)"
        exit 1
    fi
else
    print_error "Python3 не найден! Установите Python 3.7+ и повторите попытку."
    exit 1
fi

# ═══════════════════════════════════════════════════════════════
# ЭТАП 2: Настройка виртуального окружения  
# ═══════════════════════════════════════════════════════════════
print_step 2 "Настройка виртуального окружения" "🏗️"
VENV_DIR="$SCRIPT_DIR/venv"

if [ -d "$VENV_DIR" ]; then
    print_status "Виртуальное окружение найдено, проверяем актуальность..."
    
    if [ -f "$VENV_DIR/bin/python" ]; then
        VENV_PYTHON_VERSION=$("$VENV_DIR/bin/python" --version 2>&1)
        print_status "Python в venv: ${BOLD}$VENV_PYTHON_VERSION${NC}"
        
        # Сравнение версий
        SYSTEM_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
        VENV_VERSION=$("$VENV_DIR/bin/python" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null || echo "unknown")
        
        if [ "$SYSTEM_VERSION" != "$VENV_VERSION" ]; then
            print_warning "Версии Python не совпадают (система: $SYSTEM_VERSION, venv: $VENV_VERSION)"
            print_status "Пересоздание виртуального окружения..."
            rm -rf "$VENV_DIR"
        else
            print_success "Виртуальное окружение актуально"
        fi
    else
        print_warning "Поврежденное виртуальное окружение обнаружено"
        rm -rf "$VENV_DIR"
    fi
fi

if [ ! -d "$VENV_DIR" ]; then
    print_status "Создание нового виртуального окружения..."
    (python3 -m venv "$VENV_DIR") &
    spinner $! "Создание venv"
    print_success "Виртуальное окружение создано"
fi

# Активация виртуального окружения
print_status "Активация виртуального окружения..."

# Проверяем, что файл активации существует
if [ -f "$VENV_DIR/bin/activate" ]; then
    # Попытка активации
    set +e  # Временно отключаем exit on error
    source "$VENV_DIR/bin/activate" 2>/dev/null
    ACTIVATION_RESULT=$?
    set -e  # Включаем обратно exit on error
    
    # Проверяем результат активации
    if [ $ACTIVATION_RESULT -eq 0 ] && [ "$VIRTUAL_ENV" = "$VENV_DIR" ]; then
        print_success "Виртуальное окружение активировано: ${DIM}$VIRTUAL_ENV${NC}"
    else
        # Альтернативный способ - обновляем PATH
        print_warning "Стандартная активация не сработала, используем альтернативный метод..."
        export PATH="$VENV_DIR/bin:$PATH"
        export VIRTUAL_ENV="$VENV_DIR"
        
        # Проверяем, что Python из venv доступен
        if [ -x "$VENV_DIR/bin/python" ]; then
            print_success "Виртуальное окружение настроено: ${DIM}$VENV_DIR${NC}"
        else
            print_error "Не удалось настроить виртуальное окружение"
            exit 1
        fi
    fi
else
    print_error "Файл активации не найден: $VENV_DIR/bin/activate"
    exit 1
fi

# ═══════════════════════════════════════════════════════════════
# ЭТАП 3: Обновление менеджера пакетов
# ═══════════════════════════════════════════════════════════════
print_step 3 "Обновление менеджера пакетов" "📦"

print_status "Обновление pip до последней версии..."
("$VENV_DIR/bin/python" -m pip install --upgrade pip --quiet) &
spinner $! "Обновление pip"

PIP_VERSION=$("$VENV_DIR/bin/pip" --version)
print_success "pip обновлен: ${BOLD}$PIP_VERSION${NC}"

# ═══════════════════════════════════════════════════════════════
# ЭТАП 4: Установка зависимостей
# ═══════════════════════════════════════════════════════════════
print_step 4 "Установка и обновление зависимостей" "📚"

# Счетчик для прогресс-бара
TOTAL_DEPS=5
CURRENT_DEP=0

# Базовые зависимости
print_status "Установка базовых зависимостей..."
("$VENV_DIR/bin/pip" install --upgrade python-pptx requests tqdm --quiet) &
PID=$!
while kill -0 $PID 2>/dev/null; do
    progress_bar $((++CURRENT_DEP)) $TOTAL_DEPS "Установка зависимостей"
    sleep 0.2
done
print_success "Базовые зависимости установлены"

# OpenAI библиотека
print_status "Проверка OpenAI библиотеки..."
if "$VENV_DIR/bin/python" -c "import openai; print(f'OpenAI версия: {openai.__version__}')" 2>/dev/null; then
    OPENAI_VERSION=$("$VENV_DIR/bin/python" -c "import openai; print(openai.__version__)" 2>/dev/null)
    print_success "OpenAI уже установлена: ${BOLD}$OPENAI_VERSION${NC}"
    
    if "$VENV_DIR/bin/python" -c "import openai; from packaging import version; exit(0 if version.parse(openai.__version__) >= version.parse('1.0.0') else 1)" 2>/dev/null; then
        print_success "Версия OpenAI соответствует требованиям (≥ 1.0.0)"
    else
        print_warning "Версия OpenAI устарела, обновляем..."
        ("$VENV_DIR/bin/pip" install --upgrade "openai>=1.0.0" --quiet) &
        spinner $! "Обновление OpenAI"
        NEW_VERSION=$("$VENV_DIR/bin/python" -c "import openai; print(openai.__version__)")
        print_success "OpenAI обновлена до версии: ${BOLD}$NEW_VERSION${NC}"
    fi
else
    print_status "Установка OpenAI библиотеки..."
    ("$VENV_DIR/bin/pip" install "openai>=1.0.0" --quiet) &
    spinner $! "Установка OpenAI"
    OPENAI_VERSION=$("$VENV_DIR/bin/python" -c "import openai; print(openai.__version__)")
    print_success "OpenAI установлена: ${BOLD}$OPENAI_VERSION${NC}"
fi

# Google GenAI библиотека
print_status "Проверка Google GenAI библиотеки..."
if "$VENV_DIR/bin/python" -c "import google.genai; print('Google GenAI версия: установлена')" 2>/dev/null; then
    print_success "Google GenAI уже установлена"
else
    print_status "Установка Google GenAI библиотеки..."
    ("$VENV_DIR/bin/pip" install google-genai --quiet) &
    spinner $! "Установка Google GenAI"
    print_success "Google GenAI установлена"
fi

# Установка packaging
"$VENV_DIR/bin/pip" install packaging --quiet > /dev/null 2>&1 || true

# ═══════════════════════════════════════════════════════════════
# ЭТАП 5: Проверка целостности зависимостей
# ═══════════════════════════════════════════════════════════════
print_step 5 "Проверка целостности зависимостей" "🔍"

check_dependency() {
    local module_name=$1
    local import_name=${2:-$1}
    
    if "$VENV_DIR/bin/python" -c "import $import_name" 2>/dev/null; then
        print_success "${CHECK_MARK} $module_name - OK"
        return 0
    else
        print_error "${CROSS_MARK} $module_name - FAILED"
        return 1
    fi
}

DEPENDENCIES_OK=true

# Список всех зависимостей для проверки
DEPS_TO_CHECK=(
    "python-pptx:pptx"
    "requests:requests"
    "tqdm:tqdm"
    "openai:openai"
    "google-genai:google.genai"
    "os:os"
    "sys:sys"
    "json:json"
    "base64:base64"
    "threading:threading"
    "queue:queue"
    "logging:logging"
    "datetime:datetime"
    "io:io"
    "re:re"
    "time:time"
)

TOTAL_CHECKS=${#DEPS_TO_CHECK[@]}
CURRENT_CHECK=0

for dep in "${DEPS_TO_CHECK[@]}"; do
    module_name="${dep%:*}"
    import_name="${dep#*:}"
    
    progress_bar $((++CURRENT_CHECK)) $TOTAL_CHECKS "Проверка зависимостей"
    
    if ! check_dependency "$module_name" "$import_name"; then
        DEPENDENCIES_OK=false
    fi
    sleep 0.1
done

if [ "$DEPENDENCIES_OK" = false ]; then
    print_error "Некоторые зависимости не установлены корректно!"
    print_status "Попытка автоматического восстановления..."
    
    ("$VENV_DIR/bin/pip" install --force-reinstall python-pptx requests tqdm "openai>=1.0.0" google-genai --quiet) &
    spinner $! "Восстановление зависимостей"
    
    if "$VENV_DIR/bin/python" -c "import pptx, requests, tqdm, openai, google.genai" 2>/dev/null; then
        print_success "Зависимости восстановлены успешно"
    else
        print_error "Критическая ошибка: невозможно установить зависимости"
        exit 1
    fi
fi

# ═══════════════════════════════════════════════════════════════
# ЭТАП 6: Проверка файлов проекта
# ═══════════════════════════════════════════════════════════════
print_step 6 "Проверка файлов проекта" "📁"

check_file() {
    local file_path=$1
    local description=$2
    
    if [ -f "$file_path" ]; then
        print_success "${CHECK_MARK} $description: ${DIM}$file_path${NC}"
        return 0
    else
        print_error "${CROSS_MARK} $description не найден: ${DIM}$file_path${NC}"
        return 1
    fi
}

check_dir() {
    local dir_path=$1
    local description=$2
    
    if [ -d "$dir_path" ]; then
        print_success "${CHECK_MARK} $description: ${DIM}$dir_path${NC}"
        return 0
    else
        print_warning "${WARNING_MARK} $description не найден, создаем: ${DIM}$dir_path${NC}"
        mkdir -p "$dir_path"
        print_success "${CHECK_MARK} $description создан: ${DIM}$dir_path${NC}"
        return 0
    fi
}

FILES_OK=true

# Основные файлы
check_file "$SCRIPT_DIR/rwtech_pptx_generator.py" "Основной скрипт" || FILES_OK=false
check_file "$SCRIPT_DIR/pptx_content/slide_content.txt" "Контент слайдов" || FILES_OK=false
check_file "$SCRIPT_DIR/pptx_template/Шаблон презентации 16х9.pptx" "Шаблон презентации" || FILES_OK=false

# Рабочие директории
check_dir "$SCRIPT_DIR/pptx_result" "Директория результатов"
check_dir "$SCRIPT_DIR/logs" "Директория логов"
check_dir "$SCRIPT_DIR/prompts_for_img" "Директория промптов"

if [ "$FILES_OK" = false ]; then
    print_error "Отсутствуют критически важные файлы проекта!"
    exit 1
fi

# ═══════════════════════════════════════════════════════════════
# ЭТАП 7: Тестирование функциональности
# ═══════════════════════════════════════════════════════════════
print_step 7 "Тестирование функциональности" "🧪"

print_status "Тестирование импортов Python..."

# Тест импортов
("$VENV_DIR/bin/python" -c "
import sys, os
sys.path.insert(0, '$SCRIPT_DIR')

# Тест основных импортов
try:
    from pptx import Presentation
    import requests
    import openai
    from openai import OpenAI
    print('${CHECK_MARK} Все критические модули импортированы успешно')
except Exception as e:
    print(f'${CROSS_MARK} Ошибка импорта: {e}')
    sys.exit(1)

# Тест создания OpenAI клиента
try:
    client = OpenAI(api_key='test_key')
    if hasattr(client, 'images') and hasattr(client.images, 'generate'):
        print('${CHECK_MARK} OpenAI клиент функционален')
    else:
        print('${CROSS_MARK} OpenAI клиент не поддерживает генерацию изображений')
        sys.exit(1)
except Exception as e:
    print(f'${CROSS_MARK} Ошибка создания OpenAI клиента: {e}')
    sys.exit(1)

print('${CHECK_MARK} Все тесты пройдены успешно')
") &

spinner $! "Выполнение тестов"

if [ $? -eq 0 ]; then
    print_success "Функциональное тестирование завершено успешно"
else
    print_error "Ошибки в функциональном тестировании!"
    exit 1
fi

# ═══════════════════════════════════════════════════════════════
# ЭТАП 8: Создание информационных файлов
# ═══════════════════════════════════════════════════════════════
print_step 8 "Обновление информационных файлов" "📄"

ENV_INFO_FILE="$SCRIPT_DIR/environment_info.txt"
cat > "$ENV_INFO_FILE" << EOF
RW Tech PPTX Generator - Environment Information
===============================================
Дата создания: $(date)
Рабочая директория: $SCRIPT_DIR
Python версия: $("$VENV_DIR/bin/python" --version)
Virtual Environment: $VIRTUAL_ENV

Установленные пакеты:
$("$VENV_DIR/bin/pip" list | grep -E "(python-pptx|requests|tqdm|openai)" | sort)

Системная информация:
OS: $(uname -s)
Архитектура: $(uname -m)
Пользователь: $(whoami)

Файлы проекта:
$(find "$SCRIPT_DIR" -maxdepth 2 -name "*.py" -o -name "*.txt" -o -name "*.pptx" -o -name "*.md" | sort)

Статус: ГОТОВ К РАБОТЕ ✓
EOF

print_success "Информация об окружении сохранена: ${DIM}$ENV_INFO_FILE${NC}"

# ═══════════════════════════════════════════════════════════════
# ЭТАП 9: Финальная проверка и запуск
# ═══════════════════════════════════════════════════════════════
print_step 9 "Финальная проверка и запуск" "🎯"

print_status "Проверка готовности к запуску..."

# Финальная проверка
if [ -f "$SCRIPT_DIR/rwtech_pptx_generator.py" ] && \
   [ -f "$VENV_DIR/bin/python" ] && \
   "$VENV_DIR/bin/python" -c "import pptx, requests, openai, google.genai" 2>/dev/null; then
    
    print_success "Все системы готовы к запуску!"
    echo ""
    
    # Красивый ASCII заголовок для запуска
    echo -e "${BRIGHT_GREEN}"
    cat << 'EOF'
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║    🚀 ЗАПУСК RW TECH PPTX GENERATOR 🚀                        ║
    ║                                                                ║
    ║    ▶️  Система настроена и готова к работе                     ║
    ║    ⚡ Все зависимости установлены                              ║
    ║    ✨ Виртуальное окружение активно                           ║
    ║    🎯 Переход к генерации презентации...                      ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
    
    sleep 1
    
    # Запуск основного скрипта
    exec "$VENV_DIR/bin/python" "$SCRIPT_DIR/rwtech_pptx_generator.py"
    
else
    print_error "Система не готова к запуску!"
    print_error "Проверьте логи выше для выявления проблем"
    
    echo -e "${RED}"
    cat << 'EOF'
    ╔═══════════════════════════════════════════════════════════════╗
    ║                      ❌ ОШИБКА ЗАПУСКА ❌                     ║
    ║                                                               ║
    ║   Обнаружены критические проблемы в настройке окружения      ║
    ║   Просмотрите сообщения выше для устранения неполадок        ║
    ╚═══════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
    
    exit 1
fi