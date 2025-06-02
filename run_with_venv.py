#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Запуск Goznak PPTX Generator с виртуальным окружением
"""

import os
import sys
import subprocess

def main():
    """Запускает генератор с активированным виртуальным окружением"""
    
    # Путь к текущей директории
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Путь к виртуальному окружению
    venv_python = os.path.join(script_dir, 'venv', 'bin', 'python')
    
    # Путь к основному скрипту
    main_script = os.path.join(script_dir, 'goznak_pptx_generator.py')
    
    # Проверяем существование виртуального окружения
    if not os.path.exists(venv_python):
        print("❌ Виртуальное окружение не найдено!")
        print(f"   Ожидается: {venv_python}")
        print("\n🔧 Создайте виртуальное окружение:")
        print("   python3 -m venv venv")
        print("   source venv/bin/activate")
        print("   pip install openai>=1.0.0")
        sys.exit(1)
    
    # Проверяем существование основного скрипта
    if not os.path.exists(main_script):
        print(f"❌ Основной скрипт не найден: {main_script}")
        sys.exit(1)
    
    print("🚀 Запуск Goznak PPTX Generator с виртуальным окружением...")
    print(f"   Python: {venv_python}")
    print(f"   Скрипт: {main_script}")
    print()
    
    try:
        # Запускаем основной скрипт с Python из виртуального окружения
        result = subprocess.run([venv_python, main_script], 
                              cwd=script_dir,
                              check=False)
        
        # Возвращаем код выхода основного скрипта
        sys.exit(result.returncode)
        
    except KeyboardInterrupt:
        print("\n⚠️  Выполнение прервано пользователем")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Ошибка запуска: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()