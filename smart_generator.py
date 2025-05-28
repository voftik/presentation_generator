#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart PowerPoint Generator - полный цикл с оптимизацией контента
1. Оптимизация контента с Claude API  
2. Валидация структуры
3. Генерация презентации
4. Тестирование качества
"""

import sys
import subprocess
import time
from pathlib import Path

try:
    from content_optimizer import ContentOptimizer, ProgressBar
    from presentation_enhancer import PresentationEnhancer
    from presentation_enhancer_layer2 import PresentationEnhancerLayer2
    from main import AdvancedPowerPointGenerator
except ImportError as e:
    print(f"❌ ОШИБКА: Не удается импортировать модули: {e}")
    sys.exit(1)


class SmartPresentationGenerator:
    """Умный генератор презентаций с оптимизацией контента"""
    
    def __init__(self):
        self.script_dir = Path(__file__).parent
        
        # Настройки Claude API
        import os
        self.api_key = os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is required")
        self.model = "claude-sonnet-4-20250514"
        
        # Пути к файлам
        self.original_content = self.script_dir / "content" / "content.md"
        self.optimized_content = self.script_dir / "content" / "content_optimized.md"
        self.enhanced_content = self.script_dir / "content" / "content_enhanced.md"
        self.template_path = self.script_dir / "tempate" / "Шаблон презентации 16х9.pptx"
        self.output_dir = self.script_dir / "result"
        
    def step1_optimize_content(self) -> bool:
        """Шаг 1: Оптимизация контента с помощью Claude API"""
        print("🤖 ШАГ 1: ОПТИМИЗАЦИЯ КОНТЕНТА")
        print("=" * 60)
        
        try:
            optimizer = ContentOptimizer(self.api_key, self.model)
            success = optimizer.optimize(str(self.original_content), str(self.optimized_content))
            
            if success:
                print("✅ Шаг 1 завершен: контент оптимизирован")
                return True
            else:
                print("❌ Шаг 1 провален: ошибка оптимизации")
                return False
                
        except Exception as e:
            print(f"❌ Ошибка в шаге 1: {e}")
            return False
    
    def step2_validate_structure(self) -> bool:
        """Шаг 2: Валидация структуры оптимизированного контента"""
        print("\n🔍 ШАГ 2: ВАЛИДАЦИЯ СТРУКТУРЫ")
        print("=" * 60)
        
        try:
            # Проверяем, что файл создался
            if not self.optimized_content.exists():
                print("❌ Оптимизированный файл не найден")
                return False
            
            # Проводим детальную проверку структуры
            with open(self.optimized_content, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            h1_lines = [l for l in lines if l.startswith('# ')]
            h2_lines = [l for l in lines if l.startswith('## ')]
            h3_lines = [l for l in lines if l.startswith('### ')]
            
            print(f"📊 Структура файла:")
            print(f"   H1 заголовков: {len(h1_lines)}")
            print(f"   H2 заголовков: {len(h2_lines)}")
            print(f"   H3 заголовков: {len(h3_lines)}")
            print(f"   Ожидаемо слайдов: {1 + len(h3_lines)}")
            
            # Проверяем критические требования
            issues = []
            
            if len(h1_lines) != 1:
                issues.append(f"Должен быть ровно 1 H1 заголовок, найдено: {len(h1_lines)}")
            
            if len(h3_lines) == 0:
                issues.append("Не найдено H3 заголовков для создания слайдов")
            
            if len(h3_lines) > 70:
                issues.append(f"Слишком много H3 заголовков: {len(h3_lines)} (будет >70 слайдов)")
            
            # Проверяем качество контента
            avg_content_per_slide = len(content) / max(1, len(h3_lines))
            if avg_content_per_slide < 50:
                issues.append("Слишком мало контента на слайд - возможна потеря информации")
            
            if issues:
                print("❌ Найдены проблемы:")
                for issue in issues:
                    print(f"   • {issue}")
                return False
            else:
                print("✅ Шаг 2 завершен: структура валидна")
                return True
                
        except Exception as e:
            print(f"❌ Ошибка в шаге 2: {e}")
            return False
    
    def step3_enhance_content(self) -> bool:
        """Шаг 3: Улучшение контента экспертным анализом"""
        print("\n🎨 ШАГ 3: УЛУЧШЕНИЕ КОНТЕНТА")
        print("=" * 60)
        
        try:
            # Создаем улучшатор
            enhancer = PresentationEnhancer(self.api_key, self.model)
            success = enhancer.enhance_presentation(str(self.optimized_content), str(self.enhanced_content))
            
            if success:
                print("✅ Шаг 3 завершен: контент улучшен экспертным анализом")
                return True
            else:
                print("❌ Шаг 3 провален: ошибка улучшения")
                return False
                
        except Exception as e:
            print(f"❌ Ошибка в шаге 3: {e}")
            return False
    
    def step4_enhance_layer2(self) -> bool:
        """Шаг 4: Применение второго слоя улучшений"""
        print("\n🎯 ШАГ 4: ВТОРОЙ СЛОЙ УЛУЧШЕНИЙ")
        print("=" * 60)
        
        try:
            # Сначала создаем базовую презентацию
            generator = AdvancedPowerPointGenerator(
                str(self.enhanced_content),
                str(self.template_path), 
                str(self.output_dir)
            )
            
            generator.generate()
            
            # Проверяем, что базовая презентация создалась
            base_presentation_path = self.output_dir / "presentation.pptx"
            if not base_presentation_path.exists():
                print("❌ Базовая презентация не создалась")
                return False
            
            # Применяем второй слой улучшений
            enhancer_layer2 = PresentationEnhancerLayer2(self.api_key)
            final_presentation_path = self.output_dir / "presentation_layer2.pptx"
            
            results = enhancer_layer2.enhance_layer2(
                str(base_presentation_path), 
                str(final_presentation_path)
            )
            
            print(f"📊 Результаты второго слоя:")
            print(f"   Оптимизировано заголовков: {results['optimized_titles']}")
            print(f"   Оптимизировано текстов: {results['optimized_text']}")
            print(f"   Декорировано макетов: {results['decorated_layouts']}")
            
            if results['errors']:
                print(f"   ⚠️ Ошибки: {len(results['errors'])}")
            
            # Переименовываем финальную презентацию
            if final_presentation_path.exists():
                final_path = self.output_dir / "presentation.pptx"
                if final_path.exists():
                    final_path.unlink()  # Удаляем старую версию
                final_presentation_path.rename(final_path)
                
                print("✅ Шаг 4 завершен: второй слой улучшений применен")
                return True
            else:
                print("❌ Шаг 4 провален: второй слой не применился")
                return False
                
        except Exception as e:
            print(f"❌ Ошибка в шаге 4: {e}")
            return False
    
    def step6_test_quality(self) -> bool:
        """Шаг 6: Тестирование качества презентации"""
        print("\n🔍 ШАГ 6: ТЕСТИРОВАНИЕ КАЧЕСТВА")
        print("=" * 60)
        
        try:
            # Запускаем тест качества
            result = subprocess.run([
                sys.executable, 
                str(self.script_dir / "test_presentation.py")
            ], capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                print("✅ Шаг 6 завершен: тест качества пройден")
                
                # Извлекаем оценку из вывода
                output_lines = result.stdout.split('\n')
                grade_line = [l for l in output_lines if "ИТОГОВАЯ ОЦЕНКА:" in l]
                if grade_line:
                    print(f"🏆 {grade_line[0].strip()}")
                
                return True
            else:
                print("❌ Шаг 6 провален: тест качества не пройден")
                print("Вывод ошибки:")
                print(result.stderr)
                return False
                
        except subprocess.TimeoutExpired:
            print("⏱️  Тест качества превысил время ожидания (60с)")
            return False
        except Exception as e:
            print(f"❌ Ошибка в шаге 6: {e}")
            return False
    
    def generate_smart_presentation(self) -> bool:
        """Полный цикл умной генерации презентации"""
        print("🧠 УМНЫЙ ГЕНЕРАТОР ПРЕЗЕНТАЦИЙ")
        print("Полный цикл: Оптимизация → Валидация → Улучшение → Второй слой → Тестирование")
        print("=" * 80)
        
        # Проверяем наличие исходного файла
        if not self.original_content.exists():
            print(f"❌ Исходный файл не найден: {self.original_content}")
            return False
        
        # Шаг 1: Оптимизация контента
        if not self.step1_optimize_content():
            return False
        
        # Шаг 2: Валидация структуры
        if not self.step2_validate_structure():
            return False
        
        # Шаг 3: Улучшение контента
        if not self.step3_enhance_content():
            return False
        
        # Шаг 4: Второй слой улучшений  
        if not self.step4_enhance_layer2():
            return False
        
        # Шаг 6: Тестирование качества
        quality_passed = self.step6_test_quality()
        
        # Финальный отчет
        print("\n🎉 ФИНАЛЬНЫЙ ОТЧЕТ")
        print("=" * 80)
        
        if quality_passed:
            print("✅ ВСЕ ЭТАПЫ УСПЕШНО ЗАВЕРШЕНЫ!")
            print("🎯 Результат: Высококачественная презентация готова")
            
            # Выводим статистику
            presentation_path = self.output_dir / "presentation.pptx"
            if presentation_path.exists():
                size_mb = presentation_path.stat().st_size / 1024 / 1024
                print(f"📁 Файл: {presentation_path}")
                print(f"💾 Размер: {size_mb:.1f} MB")
        else:
            print("⚠️  ГЕНЕРАЦИЯ ЗАВЕРШЕНА С ПРЕДУПРЕЖДЕНИЯМИ")
            print("🎯 Результат: Презентация создана, но тест качества не пройден")
        
        print(f"📂 Оптимизированный контент: {self.optimized_content}")
        print(f"📂 Улучшенный контент: {self.enhanced_content}")
        print(f"📂 Результат: {self.output_dir}/presentation.pptx")
        print("=" * 80)
        
        return True


def main():
    """Главная функция"""
    generator = SmartPresentationGenerator()
    success = generator.generate_smart_presentation()
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()