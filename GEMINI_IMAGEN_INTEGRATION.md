# Google Gemini + Imagen 3 Integration

## Обзор

Добавлена поддержка Google Gemini + Imagen 3 как третьей опции для генерации AI-изображений в Goznak PPTX Generator. Это дает пользователям доступ к передовым технологиям Google AI для создания высококачественных иллюстраций.

## 🌟 Возможности Google Gemini + Imagen 3

### Технические характеристики
- **Модель**: `imagen-3.0-generate-002`
- **Разрешение**: 16:9 (оптимально для презентаций)
- **Качество**: Высокое
- **Формат выхода**: PNG
- **Генерация людей**: Разрешена (только взрослые)

### Преимущества
- 🚀 **Передовые технологии**: Новейшие разработки Google AI
- 🎨 **Высокое качество**: Детализированные и реалистичные изображения
- ⚡ **Оптимизация**: Специально настроено для презентаций
- 🔧 **Гибкость**: Больше параметров настройки

## 🔧 Установка и настройка

### 1. Установка зависимостей

#### Автоматическая установка (рекомендуется)
```bash
./run.sh
```
Скрипт автоматически установит все необходимые библиотеки.

#### Ручная установка
```bash
# Активация виртуального окружения
source venv/bin/activate

# Установка Google GenAI
pip install google-genai
```

### 2. Настройка API ключа

#### Вариант 1: Переменная окружения
```bash
export GEMINI_API_KEY="your_gemini_api_key_here"
```

#### Вариант 2: Конфигурационный файл
Добавьте ключ в `config.json`:
```json
{
  "claude_api_key": "your_claude_key",
  "openai_api_key": "your_openai_key", 
  "gemini_api_key": "your_gemini_key",
  "image_model": "gemini-imagen-3"
}
```

### 3. Получение API ключа Google

1. Перейдите на [Google AI Studio](https://aistudio.google.com)
2. Создайте новый проект или выберите существующий
3. Получите API ключ для Gemini
4. Убедитесь, что у вас есть доступ к Imagen 3

## 🎨 Использование

### Выбор модели в интерфейсе

При запуске программы выберите модель:
```
🎨 Выберите модель для генерации изображений:
1. 🔥 DALL-E 3 (рекомендуется) - высокое качество, отличное понимание промптов
2. ⚡ GPT-Image-1 (новая) - быстрая генерация, больше возможностей настройки  
3. 🌟 Google Gemini + Imagen 3 (инновационная) - передовые технологии Google AI

🎯 Ваш выбор (1-3): 3
✅ Выбрана модель Google Gemini + Imagen 3
```

### Параметры генерации

```python
# Конфигурация для Imagen 3
config = types.GenerateImagesConfig(
    number_of_images=1,               # Одно изображение на слайд
    aspect_ratio="16:9",              # Соотношение для презентаций
    person_generation="allow_adult"   # Разрешаем взрослых людей
)
```

## 📊 Сравнение с другими моделями

| Характеристика | DALL-E 3 | GPT-Image-1 | Gemini + Imagen 3 |
|---------------|----------|-------------|-------------------|
| **Разрешение** | 1792x1024 | 1536x1024 | 16:9 (адаптивное) |
| **Соотношение** | 16:9 | 3:2 | 16:9 |
| **Скорость** | Средняя | Высокая | Высокая |
| **Качество** | Отличное | Хорошее | Отличное |
| **Понимание промптов** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Настройки** | Базовые | Расширенные | Продвинутые |
| **Новизна** | Стабильная | Новая | Инновационная |

## 🔍 Технические детали

### Архитектура интеграции

```python
def _generate_with_gemini_imagen(self, clean_prompt, slide_number):
    """Генерирует изображение с помощью Google Gemini + Imagen 3"""
    
    # 1. Импорт библиотек
    from google import genai
    from google.genai import types
    
    # 2. Инициализация клиента
    client = genai.Client(api_key=self.gemini_api_key)
    
    # 3. Настройка параметров
    config = types.GenerateImagesConfig(
        number_of_images=1,
        aspect_ratio="16:9",
        person_generation="allow_adult"
    )
    
    # 4. Генерация изображения
    response = client.models.generate_images(
        model='imagen-3.0-generate-002',
        prompt=clean_prompt,
        config=config
    )
    
    # 5. Сохранение результата
    return self._save_generated_image(response, slide_number)
```

### Обработка ошибок

Система включает комплексную обработку ошибок:

1. **ImportError**: Отсутствие библиотеки google-genai
2. **AuthenticationError**: Неверный API ключ
3. **APIError**: Ошибки API Gemini
4. **NetworkError**: Проблемы с соединением

### Логирование

```python
# Логи генерации
self.logger.info(f"Gemini + Imagen 3 запрос для слайда {slide_number}")
self.logger.info(f"Изображение успешно создано: {image_path}")

# Статистика
self.execution_stats.increment('images_generated')
self.generation_stats['images_generated'] += 1
```

## 🎯 Оптимизация промптов

### Особенности Imagen 3

1. **Английские промпты**: Только английский язык
2. **Детальные описания**: Чем подробнее, тем лучше
3. **Белый фон**: Автоматически добавляется инструкция
4. **4K качество**: Указание разрешения в промпте

### Пример оптимизированного промпта

```
NEURAL NETWORK ARCHITECTURE DIAGRAM, isometric 3D view, WHITE BACKGROUND, 
connected components with arrows, tech stack visualization, 
blue and gray color scheme, ultra minimalist design, 
studio lighting, professional technical illustration,
hi-res 4K resolution, content highly relevant to context and instructions.
```

## 🔄 Интеграция с существующей системой

### Диспетчеризация моделей

```python
# Выбор модели в зависимости от настройки
if self.image_model == 'gpt-image-1':
    return self._generate_with_gpt_image_1(clean_prompt, slide_number)
elif self.image_model == 'gemini-imagen-3':
    return self._generate_with_gemini_imagen(clean_prompt, slide_number)
else:
    return self._generate_with_dalle_3(clean_prompt, slide_number)
```

### Сохранение конфигурации

```json
{
  "claude_api_key": "your_claude_api_key_here",
  "openai_api_key": "your_openai_api_key_here",
  "gemini_api_key": "AIza...",
  "image_model": "gemini-imagen-3"
}
```

## 🚨 Troubleshooting

### Распространенные проблемы

#### 1. Ошибка импорта
```
❌ Для использования Gemini + Imagen 3 необходимо установить библиотеку google-genai
```
**Решение**: `pip install google-genai`

#### 2. Отсутствие API ключа
```
❌ Для использования Gemini + Imagen 3 необходимо настроить GEMINI_API_KEY
```
**Решение**: Настройте переменную окружения или config.json

#### 3. Ошибка авторизации
```
❌ Ошибка генерации с Gemini + Imagen 3: 401 Unauthorized
```
**Решение**: Проверьте правильность API ключа

### Диагностика

```bash
# Тест интеграции
python test_gemini_integration.py

# Проверка зависимостей
python -c "import google.genai; print('OK')"

# Тест API ключа
python -c "from google import genai; genai.Client(api_key='your_key')"
```

## 📈 Производительность

### Метрики
- **Время генерации**: ~10-15 секунд на изображение
- **Качество**: Высокое (субъективно)
- **Соответствие промпту**: Отличное
- **Стабильность**: Высокая

### Оптимизации
- Параллельная обработка поддерживается
- Кэширование промптов
- Автоматическое восстановление при ошибках

## 🔮 Будущие улучшения

1. **Больше параметров**: Дополнительные настройки генерации
2. **Стили**: Предустановленные художественные стили
3. **Пакетная обработка**: Генерация нескольких изображений сразу
4. **Кэширование**: Сохранение результатов для повторного использования

---

*Google Gemini + Imagen 3 представляет собой мощное дополнение к Goznak PPTX Generator, предоставляя пользователям доступ к новейшим технологиям AI для создания профессиональных презентаций.*