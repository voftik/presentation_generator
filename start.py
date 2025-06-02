#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RW Tech PPTX Generator - Main Startup File
Главный стартовый файл универсального генератора презентаций PowerPoint

Компания: RW Tech - Revolutionary Workflows & Technology Solutions
Версия: 4.0 - Universal Edition
Дата: 2025-06-02
"""

import sys
import os
import platform
from datetime import datetime

def check_python_version():
    """Проверка версии Python"""
    if sys.version_info < (3, 7):
        print("❌ ОШИБКА: Требуется Python 3.7 или выше")
        print(f"   Текущая версия: {sys.version}")
        print("   Пожалуйста, обновите Python и повторите попытку.")
        sys.exit(1)
    else:
        print(f"✓ Python {sys.version.split()[0]} - OK")

def check_virtual_environment():
    """Проверка активации виртуального окружения"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✓ Виртуальное окружение активировано")
        return True
    else:
        print("⚠️  Виртуальное окружение не активировано")
        return False

def check_dependencies():
    """Проверка установленных зависимостей"""
    required_packages = [
        ('python-pptx', 'pptx'),
        ('requests', 'requests'),
        ('tqdm', 'tqdm')
    ]
    
    missing_packages = []
    
    for package_name, import_name in required_packages:
        try:
            __import__(import_name)
            print(f"✓ {package_name} - установлен")
        except ImportError:
            print(f"❌ {package_name} - НЕ установлен")
            missing_packages.append(package_name)
    
    return missing_packages

def print_system_info():
    """Вывод информации о системе"""
    print("\n" + "="*60)
    print("🚀 RW TECH PPTX GENERATOR v4.0")
    print("   Универсальный генератор презентаций PowerPoint")
    print("   с поддержкой AI-иллюстраций и передовыми технологиями")
    print("="*60)
    
    print(f"\n📋 Информация о системе:")
    print(f"   ОС: {platform.system()} {platform.release()}")
    print(f"   Архитектура: {platform.machine()}")
    print(f"   Python: {sys.version.split()[0]}")
    print(f"   Дата запуска: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   Рабочая директория: {os.getcwd()}")

def check_file_structure():
    """Проверка структуры файлов проекта"""
    print(f"\n📁 Проверка структуры проекта:")
    
    required_files = [
        ("rwtech_pptx_generator.py", "Основной модуль генератора"),
        ("pptx_content/slide_content.txt", "Файл с контентом слайдов"),
        ("pptx_template/Шаблон презентации 16х9.pptx", "Шаблон презентации")
    ]
    
    required_dirs = [
        ("pptx_result", "Директория результатов"),
        ("prompts_for_img", "Директория промптов AI"),
        ("img_generated", "Директория AI-изображений"),
        ("logs", "Директория логов"),
        ("venv", "Виртуальное окружение")
    ]
    
    all_ok = True
    
    # Проверка файлов
    for file_path, description in required_files:
        if os.path.exists(file_path):
            print(f"   ✓ {file_path} - {description}")
        else:
            print(f"   ❌ {file_path} - ОТСУТСТВУЕТ ({description})")
            all_ok = False
    
    # Проверка директорий
    for dir_path, description in required_dirs:
        if os.path.exists(dir_path):
            print(f"   ✓ {dir_path}/ - {description}")
        else:
            print(f"   ⚠️  {dir_path}/ - будет создана ({description})")
    
    return all_ok

def install_dependencies_prompt(missing_packages):
    """Предложение установки недостающих пакетов"""
    if not missing_packages:
        return
        
    print(f"\n⚠️  Обнаружены недостающие зависимости:")
    for package in missing_packages:
        print(f"   - {package}")
    
    print(f"\n💡 Для установки выполните команды:")
    if check_virtual_environment():
        print(f"   pip install {' '.join(missing_packages)}")
    else:
        print(f"   # Сначала активируйте виртуальное окружение:")
        if platform.system() == "Windows":
            print(f"   venv\\Scripts\\activate")
        else:
            print(f"   source venv/bin/activate")
        print(f"   # Затем установите пакеты:")
        print(f"   pip install {' '.join(missing_packages)}")
    
    try:
        response = input("\nУстановить недостающие пакеты автоматически? (да/нет): ").strip().lower()
        if response in ['да', 'yes', 'y', 'д']:
            import subprocess
            try:
                print("\n📦 Установка пакетов...")
                cmd = [sys.executable, '-m', 'pip', 'install'] + missing_packages
                result = subprocess.run(cmd, check=True, capture_output=True, text=True)
                print("✓ Пакеты успешно установлены!")
                return True
            except subprocess.CalledProcessError as e:
                print(f"❌ Ошибка установки: {e}")
                print("Пожалуйста, установите пакеты вручную.")
                return False
        else:
            print("Установите недостающие пакеты вручную перед запуском.")
            return False
    except EOFError:
        print("Автоматический режим: пропуск установки пакетов.")
        return False

def show_configuration_info():
    """Показать информацию о конфигурации"""
    print(f"\n⚙️  Конфигурация:")
    
    config_file = "config.json"
    if os.path.exists(config_file):
        print(f"   ✓ Найден файл конфигурации: {config_file}")
        try:
            import json
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                if config.get('claude_api_key'):
                    print(f"   ✓ Claude API ключ: настроен")
                else:
                    print(f"   ⚠️  Claude API ключ: не задан")
                    
                if config.get('openai_api_key'):
                    print(f"   ✓ OpenAI API ключ: настроен")
                else:
                    print(f"   ⚠️  OpenAI API ключ: не задан")
        except Exception as e:
            print(f"   ❌ Ошибка чтения конфигурации: {e}")
    else:
        print(f"   ⚠️  Файл конфигурации отсутствует (будет создан при необходимости)")
    
    # Проверка переменных окружения
    env_keys = ['CLAUDE_API_KEY', 'OPENAI_API_KEY']
    for key in env_keys:
        if os.environ.get(key):
            print(f"   ✓ Переменная окружения {key}: задана")
        else:
            print(f"   ⚠️  Переменная окружения {key}: не задана")

def show_usage_instructions():
    """Показать инструкции по использованию"""
    print(f"\n📚 Возможности программы:")
    print(f"   🎯 Генерация 60-слайдовой презентации из текстового контента")
    print(f"   🎨 Корпоративный дизайн с соотношением сторон 16:9")
    print(f"   🤖 AI-иллюстрации с помощью Claude + DALL-E 3 (опционально)")
    print(f"   📊 Адаптивные макеты с чередованием позиций текста")
    print(f"   📝 Детальное логирование и отчеты об ошибках")
    
    print(f"\n🎮 Режимы работы:")
    print(f"   1️⃣  Стандартный режим: только текст и шаблонные изображения")
    print(f"   2️⃣  AI режим: + автоматическая генерация иллюстраций")
    
    print(f"\n🔧 Для настройки AI-иллюстраций потребуются:")
    print(f"   • API ключ Claude (для генерации промптов)")
    print(f"   • API ключ OpenAI (для создания изображений)")

def run_main_generator():
    """Запуск основного генератора"""
    try:
        print(f"\n🚀 Запуск генератора презентаций...")
        print("-" * 60)
        
        # Импортируем и запускаем основной модуль
        from rwtech_pptx_generator import RWTechPPTXGenerator
        
        generator = RWTechPPTXGenerator()
        generator.run()
        
        print("-" * 60)
        print("🎉 Программа завершена успешно!")
        
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        print("Убедитесь, что файл rwtech_pptx_generator.py находится в той же директории.")
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"\n\n⏹️  Программа прервана пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {type(e).__name__}: {e}")
        print("Проверьте логи для получения подробной информации.")
        sys.exit(1)

def main():
    """Главная функция запуска"""
    try:
        # Системная информация
        print_system_info()
        
        # Проверки системы
        print(f"\n🔍 Системные проверки:")
        check_python_version()
        venv_ok = check_virtual_environment()
        
        # Проверка зависимостей
        print(f"\n📦 Проверка зависимостей:")
        missing_packages = check_dependencies()
        
        if missing_packages:
            deps_installed = install_dependencies_prompt(missing_packages)
            if not deps_installed and not venv_ok:
                print(f"\n❌ Установите недостающие зависимости для продолжения.")
                sys.exit(1)
        
        # Проверка файлов
        files_ok = check_file_structure()
        if not files_ok:
            print(f"\n❌ Отсутствуют критически важные файлы!")
            print("Убедитесь, что все файлы проекта находятся в правильных местах.")
            
            try:
                response = input("\nПродолжить несмотря на отсутствующие файлы? (да/нет): ").strip().lower()
                if response not in ['да', 'yes', 'y', 'д']:
                    sys.exit(1)
            except EOFError:
                print("Автоматический режим: продолжение...")
        
        # Информация о конфигурации
        show_configuration_info()
        
        # Инструкции
        show_usage_instructions()
        
        # Запрос на продолжение
        print(f"\n" + "="*60)
        try:
            input("📋 Нажмите Enter для запуска генератора или Ctrl+C для выхода...")
        except EOFError:
            print("Автоматический режим: запуск генератора...")
        
        # Запуск основной программы
        run_main_generator()
        
    except KeyboardInterrupt:
        print(f"\n\n👋 До свидания!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Критическая ошибка в стартовом модуле: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()