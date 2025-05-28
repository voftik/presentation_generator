#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Presentation Enhancer - модуль для интеллектуального улучшения презентации
Анализирует готовую презентацию и расширяет контент ключевых слайдов
для руководителей Гознака с помощью экспертного промпта Claude
"""

import os
import sys
import re
import random
from pathlib import Path
from typing import List, Dict, Tuple, Optional

try:
    import anthropic
    from content_optimizer import ProgressBar
except ImportError as e:
    print(f"❌ ОШИБКА: Не удается импортировать зависимости: {e}")
    print("Убедитесь что установлены: anthropic")
    sys.exit(1)


class SlideContent:
    """Структура данных для слайда"""
    def __init__(self, slide_number: int, title: str, content: str, slide_type: str = "content"):
        self.slide_number = slide_number
        self.title = title
        self.content = content
        self.slide_type = slide_type
        self.enhanced_content = ""
        self.is_enhanced = False


class PresentationEnhancer:
    """Улучшатор презентаций с экспертным анализом и расширением контента"""
    
    def __init__(self, api_key: str, model: str = "claude-sonnet-4-20250514"):
        self.api_key = api_key
        self.model = model
        self.client = anthropic.Anthropic(api_key=api_key)
        self.target_enhanced_slides = 22  # Целевое количество улучшенных слайдов
        
    def analyze_presentation(self, content_path: str) -> List[SlideContent]:
        """Анализирует структуру презентации и извлекает слайды"""
        print("📊 Анализируем структуру готовой презентации...")
        
        with open(content_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        slides = []
        current_slide = None
        current_content_lines = []
        slide_number = 0
        
        for line in lines:
            line = line.rstrip()
            
            # H1 заголовки - титульные слайды
            if line.startswith('# '):
                if current_slide:
                    current_slide.content = '\n'.join(current_content_lines).strip()
                    slides.append(current_slide)
                
                slide_number += 1
                title = line[2:].strip()
                current_slide = SlideContent(slide_number, title, "", "section")
                current_content_lines = []
            
            # H3 заголовки - контентные слайды
            elif line.startswith('### '):
                if current_slide:
                    current_slide.content = '\n'.join(current_content_lines).strip()
                    slides.append(current_slide)
                
                slide_number += 1
                title = line[4:].strip()
                current_slide = SlideContent(slide_number, title, "", "content")
                current_content_lines = []
            
            elif line.strip():
                # Обычный текст
                current_content_lines.append(line)
        
        # Не забываем последний слайд
        if current_slide:
            current_slide.content = '\n'.join(current_content_lines).strip()
            slides.append(current_slide)
        
        print(f"✅ Найдено {len(slides)} слайдов ({len([s for s in slides if s.slide_type == 'content'])} контентных)")
        return slides
    
    def select_slides_for_enhancement(self, slides: List[SlideContent]) -> List[SlideContent]:
        """Интеллектуально выбирает слайды для улучшения"""
        print("🎯 Выбираем ключевые слайды для улучшения...")
        
        # Фильтруем только контентные слайды
        content_slides = [s for s in slides if s.slide_type == "content"]
        
        if len(content_slides) <= self.target_enhanced_slides:
            selected = content_slides
        else:
            # Стратегия выбора: ключевые темы + случайное распределение
            priority_keywords = [
                'внедрения', 'применения', 'кейс', 'примеры', 'результат',
                'ROI', 'экономия', 'эффективность', 'стратегия', 'планирование',
                'команда', 'проекты', 'данные', 'риски', 'этика', 'российские'
            ]
            
            # Приоритетные слайды (содержат ключевые слова)
            priority_slides = []
            regular_slides = []
            
            for slide in content_slides:
                slide_text = (slide.title + " " + slide.content).lower()
                if any(keyword in slide_text for keyword in priority_keywords):
                    priority_slides.append(slide)
                else:
                    regular_slides.append(slide)
            
            # Выбираем комбинацию приоритетных и обычных
            priority_count = min(len(priority_slides), self.target_enhanced_slides // 2)
            regular_count = self.target_enhanced_slides - priority_count
            
            selected = priority_slides[:priority_count]
            if regular_count > 0:
                random.shuffle(regular_slides)
                selected.extend(regular_slides[:regular_count])
            
            # Перемешиваем финальный список для неупорядоченного улучшения
            random.shuffle(selected)
        
        print(f"📋 Выбрано {len(selected)} слайдов для улучшения:")
        for i, slide in enumerate(selected[:5]):  # Показываем первые 5
            print(f"   • Слайд {slide.slide_number}: {slide.title[:50]}...")
        if len(selected) > 5:
            print(f"   ... и еще {len(selected) - 5} слайдов")
        
        return selected
    
    def create_enhancement_prompt(self, slide: SlideContent, context_slides: List[SlideContent]) -> str:
        """Создает экспертный промпт для улучшения слайда"""
        
        # Определяем контекст презентации
        total_slides = len(context_slides)
        slide_position = f"{slide.slide_number}/{total_slides}"
        
        prompt = f"""Ты - ведущий эксперт по корпоративному обучению ИИ-трансформации с 15-летним опытом работы с топ-менеджментом крупных государственных и частных компаний. Ты специализируешься на адаптации сложных технологических концепций для руководителей разного уровня.

КОНТЕКСТ ЗАДАЧИ:
Ты улучшаешь презентацию об искусственном интеллекте для руководителей ФГУП "Гознак" - ведущего предприятия защищенной полиграфии России. Аудитория: директора департаментов, начальники отделов, главные специалисты - люди с техническим образованием, но без глубокого понимания ИИ.

СПЕЦИФИКА ГОЗНАКА:
- Государственное предприятие с высокими требованиями безопасности
- Производство банкнот, паспортов, защищенных документов
- Консервативная корпоративная культура, но стремление к инновациям
- Необходимость соблюдения государственных требований и регуляций
- Фокус на качество, безопасность, технологическое превосходство

ЦЕЛЕВАЯ АУДИТОРИЯ:
- Возраст: 35-55 лет
- Образование: техническое/инженерное
- Опыт: управление производством, качеством, проектами
- Менталитет: ответственность, системность, осторожность к инновациям
- Мотивация: повышение эффективности, снижение рисков, соответствие требованиям

ТЕКУЩИЙ СЛАЙД ДЛЯ УЛУЧШЕНИЯ:
Позиция: {slide_position}
Заголовок: {slide.title}
Текущий контент:
{slide.content}

ТВОЯ ЭКСПЕРТНАЯ ЗАДАЧА:
Расширь контент этого слайда, добавив 2-4 абзаца живого, понятного, профессионального текста который:

1. РАСКРЫВАЕТ СУТЬ простым языком с конкретными примерами
2. СВЯЗЫВАЕТ с реальностью Гознака и защищенной полиграфии
3. МОТИВИРУЕТ через практические выгоды и снижение рисков
4. ИСПОЛЬЗУЕТ образные сравнения и метафоры для лучшего понимания
5. ВКЛЮЧАЕТ конкретные цифры, сроки, результаты где уместно

ПРИНЦИПЫ ЭКСПЕРТНОГО ИЗЛОЖЕНИЯ:
• Человечность: пиши как опытный коллега, а не как учебник
• Конкретность: реальные примеры, а не абстрактные концепции  
• Релевантность: все примеры должны резонировать с Гознаком
• Мотивация: каждый тезис должен отвечать на "зачем это нам?"
• Доверие: признавай ограничения, не обещай невозможного

СТИЛЬ КОММУНИКАЦИИ:
- Уверенный, но не снисходительный
- Профессиональный, но живой и увлекательный  
- Структурированный, но не механистичный
- Мотивирующий, но реалистичный

ФОРМАТ ОТВЕТА:
Добавь к существующему контенту 2-4 абзаца расширяющего текста. Сохрани оригинальные bullet points, но дополни их развернутыми объяснениями. Используй параграфы, начинающиеся с ключевых слов типа "Представьте...", "Например...", "Важно понимать...", "На практике это означает...".

ОТВЕТЬ ТОЛЬКО ДОПОЛНИТЕЛЬНЫМ КОНТЕНТОМ БЕЗ КОММЕНТАРИЕВ."""

        return prompt
    
    def enhance_slide_content(self, slide: SlideContent, context_slides: List[SlideContent]) -> str:
        """Улучшает контент слайда с помощью Claude"""
        
        prompt = self.create_enhancement_prompt(slide, context_slides)
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,  # Достаточно для качественного расширения
                temperature=0.7,  # Баланс между креативностью и точностью
                timeout=120.0,  # 2 минуты на слайд
                messages=[
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ]
            )
            
            enhanced_content = response.content[0].text.strip()
            return enhanced_content
            
        except Exception as e:
            print(f"⚠️  Ошибка улучшения слайда {slide.slide_number}: {e}")
            return ""
    
    def enhance_presentation(self, input_path: str, output_path: str) -> bool:
        """Основной метод улучшения презентации"""
        print("🚀 ЗАПУСК УЛУЧШЕНИЯ ПРЕЗЕНТАЦИИ")
        print("=" * 60)
        
        try:
            # 1. Анализируем структуру
            slides = self.analyze_presentation(input_path)
            
            # 2. Выбираем слайды для улучшения
            selected_slides = self.select_slides_for_enhancement(slides)
            
            # 3. Улучшаем выбранные слайды
            print(f"\n🧠 Улучшаем {len(selected_slides)} слайдов с помощью Claude...")
            
            enhanced_count = 0
            progress = ProgressBar(f"🎨 Улучшение слайдов экспертным контентом")
            progress.start()
            
            for slide in selected_slides:
                enhanced_content = self.enhance_slide_content(slide, slides)
                if enhanced_content:
                    slide.enhanced_content = enhanced_content
                    slide.is_enhanced = True
                    enhanced_count += 1
            
            progress.stop(f"Улучшено {enhanced_count} слайдов из {len(selected_slides)}")
            
            # 4. Создаем улучшенную версию
            self._create_enhanced_content(slides, output_path)
            
            print("=" * 60)
            print("✅ УЛУЧШЕНИЕ ЗАВЕРШЕНО УСПЕШНО!")
            print(f"📊 Всего слайдов: {len(slides)}")
            print(f"📊 Улучшено слайдов: {enhanced_count}")
            print(f"🎯 Качество улучшения: {enhanced_count/len(selected_slides)*100:.1f}%")
            
            return True
            
        except Exception as e:
            print(f"❌ ОШИБКА ПРИ УЛУЧШЕНИИ: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def _create_enhanced_content(self, slides: List[SlideContent], output_path: str):
        """Создает файл с улучшенным контентом"""
        print(f"💾 Создаем улучшенную версию: {output_path}")
        
        enhanced_content = []
        
        for slide in slides:
            if slide.slide_type == "section":
                # Титульный слайд
                enhanced_content.append(f"# {slide.title}")
            else:
                # Контентный слайд
                enhanced_content.append(f"### {slide.title}")
                enhanced_content.append(slide.content)
                
                # Добавляем улучшенный контент если есть
                if slide.is_enhanced and slide.enhanced_content:
                    enhanced_content.append("")  # Пустая строка для разделения
                    enhanced_content.append(slide.enhanced_content)
            
            enhanced_content.append("")  # Пустая строка между слайдами
        
        # Сохраняем файл
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(enhanced_content))
        
        print("✅ Улучшенная версия сохранена")


def main():
    """Главная функция для тестирования"""
    script_dir = Path(__file__).parent
    
    # Настройки
    import os
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY environment variable is required")
        return
    model = "claude-sonnet-4-20250514"
    
    input_path = script_dir / "content" / "content_optimized.md"
    output_path = script_dir / "content" / "content_enhanced.md"
    
    print("🎨 PRESENTATION ENHANCER")
    print(f"📂 Входной файл: {input_path}")
    print(f"📂 Выходной файл: {output_path}")
    print(f"🤖 Модель: {model}")
    print()
    
    # Создаем улучшатор
    enhancer = PresentationEnhancer(api_key, model)
    
    # Запускаем улучшение
    success = enhancer.enhance_presentation(str(input_path), str(output_path))
    
    if success:
        print("🎉 Готово! Используйте улучшенный файл для финальной генерации")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()