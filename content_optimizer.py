#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Content Optimizer - модуль для оптимизации контента с помощью Claude API
Цель: Преобразовать content.md в оптимальную структуру для ~60 слайдов
"""

import os
import sys
import re
import time
import threading
from pathlib import Path
from typing import Dict, List, Tuple, Optional

try:
    import anthropic
except ImportError:
    print("❌ ОШИБКА: Не установлена библиотека anthropic")
    print("Запустите: pip install anthropic")
    sys.exit(1)


class ProgressBar:
    """Красивый прогресс-бар для консоли"""
    
    def __init__(self, title: str, width: int = 50):
        self.title = title
        self.width = width
        self.running = False
        self.thread = None
        self.start_time = None
        
    def start(self):
        """Запуск анимированного прогресс-бара"""
        self.running = True
        self.start_time = time.time()
        self.thread = threading.Thread(target=self._animate, daemon=True)
        self.thread.start()
        
    def stop(self, success_message: str = ""):
        """Остановка прогресс-бара"""
        self.running = False
        if self.thread:
            self.thread.join()
        
        elapsed = time.time() - self.start_time if self.start_time else 0
        
        # Очищаем строку и выводим результат
        print(f"\r{' ' * (self.width + 50)}", end='')
        if success_message:
            print(f"\r✅ {success_message} (завершено за {elapsed:.1f}с)")
        else:
            print(f"\r✅ Завершено за {elapsed:.1f}с")
    
    def _animate(self):
        """Анимация прогресс-бара"""
        chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        i = 0
        
        while self.running:
            elapsed = time.time() - self.start_time
            
            # Создаем анимированный индикатор
            spinner = chars[i % len(chars)]
            
            # Создаем прогресс-бар
            filled = int((elapsed % 3) / 3 * self.width)
            bar = "█" * filled + "░" * (self.width - filled)
            
            # Выводим прогресс
            print(f"\r{spinner} {self.title} [{bar}] {elapsed:.1f}с", end='', flush=True)
            
            time.sleep(0.1)
            i += 1


class ContentOptimizer:
    """Оптимизатор контента с помощью Claude API"""
    
    def __init__(self, api_key: str, model: str = "claude-sonnet-4-20250514"):
        self.api_key = api_key
        self.model = model
        self.client = anthropic.Anthropic(api_key=api_key)
        self.target_slides = 60  # Целевое количество слайдов
        
    def analyze_current_content(self, content_path: str) -> Dict:
        """Анализирует текущую структуру контента"""
        print("🔍 Анализируем текущую структуру контента...")
        
        with open(content_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        
        # Подсчитываем структуру
        h1_count = len([l for l in lines if l.startswith('# ')])
        h2_count = len([l for l in lines if l.startswith('## ')])
        h3_count = len([l for l in lines if l.startswith('### ')])
        
        # Согласно нашей логике: H1 (титульный) + H3 (контентные слайды)
        estimated_slides = 1 + h3_count  # H1 = титульный, H3 = контентные
        
        analysis = {
            'h1_count': h1_count,
            'h2_count': h2_count, 
            'h3_count': h3_count,
            'estimated_slides': estimated_slides,
            'content_length': len(content),
            'lines_count': len([l for l in lines if l.strip()])
        }
        
        print(f"📊 Текущая структура:")
        print(f"   H1 заголовков: {h1_count}")
        print(f"   H2 заголовков: {h2_count}")
        print(f"   H3 заголовков: {h3_count}")
        print(f"   Ожидаемо слайдов: {estimated_slides}")
        print(f"   Длина контента: {analysis['content_length']} символов")
        
        return analysis
    
    def create_optimization_prompt(self, content: str, analysis: Dict) -> str:
        """Создает экспертный промпт для интеллектуальной оптимизации контента"""
        
        prompt = f"""Ты эксперт по созданию высококачественных бизнес-презентаций и структурированию сложного контента. Твоя задача - провести ЭКСПЕРТНУЮ ОПТИМИЗАЦИЮ markdown контента об искусственном интеллекте для руководителей.

КРИТИЧЕСКАЯ ЗАДАЧА: Преобразовать {analysis['h3_count']} слайдов в ТОЧНО {self.target_slides-1} слайдов (59 + титульный = 60).

ЭКСПЕРТНЫЕ ПРИНЦИПЫ ОПТИМИЗАЦИИ:

1. СТРАТЕГИЧЕСКОЕ МЫШЛЕНИЕ:
   - Группируй взаимосвязанные концепции
   - Создавай логические прогрессии от простого к сложному
   - Сохраняй причинно-следственные связи

2. СОХРАНЕНИЕ ЦЕННОСТИ:
   - ВСЕ ключевые данные, цифры, кейсы должны остаться
   - Каждый процент, доллар, время - критически важны
   - Конкретные примеры компаний (Netflix, Amazon и др.) обязательны

3. ЭКСПЕРТНАЯ СТРУКТУРИЗАЦИЯ:
   - H1 (#): ОДИН титульный заголовок
   - H2 (##): Логические разделы (10-12 разделов)
   - H3 (###): ТОЧНО 59 слайдов контента
   - Каждый H3 = отдельная завершенная мысль

4. ИНТЕЛЛЕКТУАЛЬНОЕ ОБЪЕДИНЕНИЕ:
   - Объединяй технически родственные темы
   - Группируй по бизнес-функциям
   - Сочетай теорию с практикой в одном слайде

5. КАЧЕСТВО КОНТЕНТА:
   - 3-5 bullet points на слайд
   - Конкретные факты, а не общие фразы
   - Акционабельные инсайты для руководителей

ИСХОДНЫЙ КОНТЕНТ ({analysis['h3_count']} слайдов → нужно {self.target_slides-1} слайдов):
{content}

ЭКСПЕРТНЫЙ АНАЛИЗ И ОПТИМИЗАЦИЯ:
Проанализируй контент, выдели ключевые темы, создай логическую структуру из 59 слайдов, сохранив ВСЮ критически важную информацию.

РЕЗУЛЬТАТ: ТОЛЬКО оптимизированный markdown. Никаких объяснений."""

        return prompt
    
    def _extract_markdown_from_response(self, response: str) -> str:
        """Извлекает только markdown контент из ответа Claude"""
        lines = response.split('\n')
        
        # Ищем первую строку с заголовком H1
        start_idx = None
        for i, line in enumerate(lines):
            if line.strip().startswith('# '):
                start_idx = i
                break
        
        # Если не нашли H1, ищем первую строку с H2 или H3
        if start_idx is None:
            for i, line in enumerate(lines):
                if line.strip().startswith('## ') or line.strip().startswith('### '):
                    start_idx = i
                    break
        
        # Если ничего не нашли, возвращаем весь ответ
        if start_idx is None:
            return response.strip()
        
        # Возвращаем все строки начиная с найденной
        return '\n'.join(lines[start_idx:]).strip()
    
    def optimize_content_with_claude(self, content: str, analysis: Dict) -> str:
        """Оптимизирует контент с помощью Claude API"""
        
        # Создаем прогресс-бар
        progress = ProgressBar("🧠 Claude анализирует и оптимизирует контент")
        
        prompt = self.create_optimization_prompt(content, analysis)
        
        try:
            # Запускаем прогресс-бар
            progress.start()
            
            response = self.client.messages.create(
                model=self.model,
                max_tokens=20000,  # Достаточно для 60 качественных слайдов
                temperature=0.9,  # Высокая температура для креативности и вариативности
                timeout=300.0,  # 5 минут таймаут для долгой обработки
                messages=[
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ]
            )
            
            raw_response = response.content[0].text
            
            # Очищаем ответ от лишнего текста, оставляем только markdown
            optimized_content = self._extract_markdown_from_response(raw_response)
            
            # Останавливаем прогресс-бар
            progress.stop("Контент успешно оптимизирован Claude Sonnet 4")
            
            return optimized_content
            
        except Exception as e:
            progress.stop()
            print(f"❌ Ошибка при обращении к Claude API: {e}")
            raise
    
    def validate_optimized_structure(self, content: str) -> Dict:
        """Проверяет структуру оптимизированного контента"""
        print("🔍 Проверяем структуру оптимизированного контента...")
        
        lines = content.split('\n')
        
        h1_count = len([l for l in lines if l.startswith('# ')])
        h2_count = len([l for l in lines if l.startswith('## ')])  
        h3_count = len([l for l in lines if l.startswith('### ')])
        
        estimated_slides = 1 + h3_count  # H1 = титульный, H3 = контентные
        
        validation = {
            'h1_count': h1_count,
            'h2_count': h2_count,
            'h3_count': h3_count,
            'estimated_slides': estimated_slides,
            'is_valid': True,
            'issues': []
        }
        
        # Проверки
        if h1_count != 1:
            validation['is_valid'] = False
            validation['issues'].append(f"Должен быть ровно 1 H1 заголовок, найдено: {h1_count}")
        
        if h3_count == 0:
            validation['is_valid'] = False
            validation['issues'].append("Не найдено H3 заголовков (слайдов)")
        
        if estimated_slides > self.target_slides + 10:
            validation['is_valid'] = False
            validation['issues'].append(f"Слишком много слайдов: {estimated_slides}, цель: ~{self.target_slides}")
        
        if estimated_slides < 30:
            validation['issues'].append(f"Мало слайдов: {estimated_slides}, возможно потеряна важная информация")
        
        print(f"📊 Структура после оптимизации:")
        print(f"   H1 заголовков: {h1_count}")
        print(f"   H2 заголовков: {h2_count}")
        print(f"   H3 заголовков: {h3_count}")
        print(f"   Ожидаемо слайдов: {estimated_slides}")
        
        if validation['is_valid']:
            print("✅ Структура корректна")
        else:
            print("❌ Найдены проблемы в структуре:")
            for issue in validation['issues']:
                print(f"   • {issue}")
        
        if validation['issues'] and validation['is_valid']:
            print("⚠️  Предупреждения:")
            for issue in validation['issues']:
                print(f"   • {issue}")
        
        return validation
    
    def save_optimized_content(self, content: str, output_path: str):
        """Сохраняет оптимизированный контент"""
        print(f"💾 Сохраняем оптимизированный контент: {output_path}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Оптимизированный контент сохранен")
    
    def optimize(self, input_path: str, output_path: str) -> bool:
        """Основной метод оптимизации"""
        print("🚀 ЗАПУСК ОПТИМИЗАЦИИ КОНТЕНТА")
        print("=" * 50)
        
        try:
            # 1. Анализируем текущий контент
            with open(input_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            analysis = self.analyze_current_content(input_path)
            
            # 2. Проверяем, нужна ли оптимизация
            if analysis['estimated_slides'] <= self.target_slides + 5:
                print(f"ℹ️  Контент уже близок к целевому размеру ({analysis['estimated_slides']} слайдов)")
                print("Пропускаем оптимизацию...")
                
                # Просто копируем оригинальный файл
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(original_content)
                return True
            
            # 3. Оптимизируем с помощью Claude
            optimized_content = self.optimize_content_with_claude(original_content, analysis)
            
            # 4. Проверяем результат
            validation = self.validate_optimized_structure(optimized_content)
            
            if not validation['is_valid']:
                print("❌ Оптимизированный контент не прошел валидацию")
                return False
            
            # 5. Сохраняем результат
            self.save_optimized_content(optimized_content, output_path)
            
            print("=" * 50)
            print("✅ ОПТИМИЗАЦИЯ ЗАВЕРШЕНА УСПЕШНО!")
            print(f"📊 Было слайдов: {analysis['estimated_slides']}")
            print(f"📊 Стало слайдов: {validation['estimated_slides']}")
            print(f"🎯 Экономия: {analysis['estimated_slides'] - validation['estimated_slides']} слайдов")
            
            return True
            
        except Exception as e:
            print(f"❌ ОШИБКА ПРИ ОПТИМИЗАЦИИ: {e}")
            import traceback
            traceback.print_exc()
            return False


def main():
    """Главная функция для тестирования"""
    script_dir = Path(__file__).parent
    
    # Настройки
    import os
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY environment variable is required")
        return
    model = "claude-sonnet-4-20250514"  # Используем актуальную модель
    
    input_path = script_dir / "content" / "content.md"
    output_path = script_dir / "content" / "content_optimized.md"
    
    print("🎯 CONTENT OPTIMIZER")
    print(f"📂 Входной файл: {input_path}")
    print(f"📂 Выходной файл: {output_path}")
    print(f"🤖 Модель: {model}")
    print()
    
    # Создаем оптимизатор
    optimizer = ContentOptimizer(api_key, model)
    
    # Запускаем оптимизацию
    success = optimizer.optimize(str(input_path), str(output_path))
    
    if success:
        print("🎉 Готово! Используйте оптимизированный файл для генерации слайдов")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()