# Google AI Models Integration

## ⚠️ ВАЖНОЕ ОБНОВЛЕНИЕ

**Gemini 2.0 Flash Preview Image Generation больше не доступна в Google Gemini API.**

Goznak PPTX Generator теперь поддерживает **один основной Google AI инструмент** для генерации изображений:

- **💎 Imagen 3** - высококачественная генерация изображений (ОСНОВНАЯ МОДЕЛЬ)
- **🔄 Gemini 2.0 Flash** - автоматически перенаправляется на Imagen 3

## 🎯 Текущее состояние моделей

### 💎 Imagen 3 (РЕКОМЕНДУЕТСЯ):

- ✅ **Высокое качество изображений** - превосходная детализация и фотореализм
- ✅ **Стабильная работа** - модель полностью функциональна в API
- ✅ **Оптимальный формат** - поддержка 16:9 для презентаций
- ✅ **Художественные стили** - поддержка различных визуальных стилей
- ✅ **Профессиональный результат** - подходит для корпоративных презентаций

**Идеально для**: всех типов изображений в презентациях

### 🔄 Gemini 2.0 Flash (DEPRECATED):

- ❌ **Модель недоступна** - Google удалила image generation из API
- 🔄 **Автоматическое перенаправление** - запросы автоматически идут в Imagen 3
- ⚠️ **Только для совместимости** - опция оставлена для обратной совместимости

## 🔧 Технические характеристики

| Характеристика | Gemini 2.0 Flash | Imagen 3 |
|---------------|------------------|----------|
| **API Model** | ❌ `Недоступна` | ✅ `imagen-3.0-generate-002` |
| **API Method** | ❌ `Недоступна` | ✅ `generate_images` |
| **Configuration** | ❌ `Недоступна` | ✅ `GenerateImagesConfig` |
| **Response Format** | ❌ `Недоступна` | ✅ Images only |
| **Status** | 🔄 Redirects to Imagen 3 | ✅ Fully functional |
| **Best For** | 🔄 Redirected | Все типы изображений |

## 🚀 Реализация

### Gemini 2.0 Flash Implementation (DEPRECATED)

```python
def _generate_with_gemini_flash(self, clean_prompt, slide_number):
    """
    DEPRECATED: Gemini 2.0 Flash image generation is not available.
    Redirects to Imagen 3 for image generation.
    """
    print("⚠️  Gemini 2.0 Flash image generation is not available in the current API")
    print("🔄 Redirecting to Imagen 3 for image generation...")
    
    if self.logger:
        self.logger.warning(f"Gemini 2.0 Flash не доступен для слайда {slide_number}, используем Imagen 3")
    
    # Redirect to Imagen 3 which actually works
    return self._generate_with_imagen_3(clean_prompt, slide_number)
```

### Imagen 3 Implementation

```python
def _generate_with_imagen_3(self, clean_prompt, slide_number):
    """Генерирует изображение с помощью Google Imagen 3"""
    
    # Конфигурация для высококачественной генерации
    config = types.GenerateImagesConfig(
        number_of_images=1,
        aspect_ratio="16:9",              # Оптимально для презентаций
        person_generation="allow_adult"   # Разрешаем взрослых людей
    )
    
    # Генерация через Imagen 3
    response = client.models.generate_images(
        model='imagen-3.0-generate-002',
        prompt=clean_prompt,
        config=config
    )
    
    # Прямое получение изображения
    generated_image = response.generated_images[0]
    image_bytes = generated_image.image.image_bytes
```

## 🎨 Пользовательский интерфейс

### Выбор модели в программе

```
🎨 Выберите модель для генерации изображений:
1. 🔥 DALL-E 3 (рекомендуется) - высокое качество, отличное понимание промптов
2. ⚡ GPT-Image-1 (новая) - быстрая генерация, больше возможностей настройки  
3. ✨ Google Gemini 2.0 Flash (DEPRECATED) - автоматически перенаправляется на Imagen 3
4. 💎 Google Imagen 3 (рекомендуется для Google) - высокое качество, стабильная работа

🎯 Ваш выбор (1-4): 
```

### Статус сообщения

**Gemini 2.0 Flash (DEPRECATED):**
```
⚠️  Gemini 2.0 Flash image generation is not available in the current API
🔄 Redirecting to Imagen 3 for image generation...
✅ Выбрана модель Google Imagen 3 💎 (перенаправлено с Gemini 2.0 Flash)
✓ Изображение Imagen 3 сохранено: slide_10_illustration.png
```

**Imagen 3:**
```
✅ Выбрана модель Google Imagen 3 💎
✓ Изображение Imagen 3 сохранено: slide_10_illustration.png
```

## 🔑 API Configuration

### Общий API Key
Обе модели используют **один и тот же Google Gemini API ключ**:

```json
{
  "gemini_api_key": "AIzaSyAx3AtOdrqJZ1fnqIE8fSrfiQWS3nHTs2I"
}
```

### Умная валидация
Система автоматически определяет необходимость валидации Gemini API:

```python
# Определяем, нужна ли валидация Gemini API
need_gemini = (self.image_model in ['gemini-2.0-flash', 'imagen-3'])

if need_gemini:
    model_name = "Gemini 2.0 Flash" if self.image_model == 'gemini-2.0-flash' else "Imagen 3"
    print(f"🔍 Проверка Google {model_name} API...")
```

## 📊 Сравнение результатов

### Для презентаций АО "Гознак"

| Тип контента | Рекомендуемая модель | Обоснование |
|-------------|---------------------|-------------|
| **Схемы процессов** | ✨ Gemini 2.0 Flash | Лучше понимает логические связи |
| **Диаграммы архитектур** | ✨ Gemini 2.0 Flash | Контекстное понимание структур |
| **Концептуальные модели** | ✨ Gemini 2.0 Flash | Отличное абстрактное мышление |
| **Художественные элементы** | 💎 Imagen 3 | Высочайшее визуальное качество |
| **Фотореалистичные объекты** | 💎 Imagen 3 | Превосходная детализация |
| **Брендинговые материалы** | 💎 Imagen 3 | Профессиональный внешний вид |

## 🔧 Troubleshooting

### Общие проблемы

#### 1. "Не получено изображений от Gemini 2.0 Flash"
```python
# Проблема: response_modalities не включены
# Решение: Обязательно использовать ['TEXT', 'IMAGE']
config = types.GenerateContentConfig(
    response_modalities=['TEXT', 'IMAGE']  # ✅ Обязательно!
)
```

#### 2. "Не получено изображений от Imagen 3"
```python
# Проблема: неправильная конфигурация
# Решение: Использовать GenerateImagesConfig
config = types.GenerateImagesConfig(
    number_of_images=1,     # ✅ Минимум 1
    aspect_ratio="16:9"     # ✅ Подходящий формат
)
```

#### 3. "Доступ к модели ограничен"
- Imagen 3 доступна только на **платном уровне**
- Убедитесь, что у вас настроен биллинг в Google AI Studio
- Некоторые регионы могут иметь ограничения

### Диагностика

```bash
# Тест интеграции Google моделей
python test_four_models.py

# Проверка Gemini API
python -c "from google import genai; print('Gemini OK')"
```

## 🌍 Региональные ограничения

### Доступность моделей
- **Gemini 2.0 Flash**: доступен в большинстве регионов
- **Imagen 3**: ограниченная доступность, требует платного плана

### Языковая поддержка
- **Gemini 2.0 Flash**: 
  - Лучшая производительность: EN, es-MX, ja-JP, zh-CN, hi-IN
  - Поддерживает многоязычные промпты
- **Imagen 3**: 
  - Только английские промпты
  - Автоматический перевод промптов в системе

## 🚀 Performance Metrics

### Скорость генерации
- **Gemini 2.0 Flash**: ~8-12 секунд
- **Imagen 3**: ~10-15 секунд
- **Parallel processing**: поддерживается для обеих моделей

### Качество результатов
- **Gemini 2.0 Flash**: отлично для концептуальных изображений
- **Imagen 3**: превосходно для фотореалистичных изображений

## 🔮 Рекомендации использования

### Для корпоративных презентаций:
1. **✨ Gemini 2.0 Flash** - для схем, диаграмм, процессов
2. **💎 Imagen 3** - для обложек, художественных элементов
3. **🔥 DALL-E 3** - универсальный выбор для смешанного контента
4. **⚡ GPT-Image-1** - для быстрого прототипирования

### Оптимальная стратегия:
- Используйте **Gemini 2.0 Flash** для 70% слайдов (концептуальные)
- Используйте **Imagen 3** для 30% слайдов (художественные акценты)

---

*Интеграция Google AI моделей предоставляет пользователям максимальную гибкость и качество для создания профессиональных презентаций.*