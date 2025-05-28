#!/usr/bin/env python3
"""
Быстрая проверка: работает ли Imagen 4 с моим ключом Gemini API.
"""

import os
from io import BytesIO
from pathlib import Path

try:
    from google import genai                # SDK
    from google.genai import types          # Типы конфигов
    from PIL import Image                   # Для просмотра результата
except ImportError as e:
    print("❌ Необходимо установить зависимости:")
    print("pip install google-genai pillow")
    exit(1)

def test_imagen_generation():
    """Тестирует генерацию изображений через Gemini + Imagen 4"""
    
    # 1) Забираем ключ из переменной окружения или используем прямо
    API_KEY = os.getenv("GEMINI_API_KEY") or "AIzaSyAx3AtOdrqJZ1fnqIE8fSrfiQWS3nHTs2I"
    if not API_KEY:
        raise SystemExit("❌ Установите переменную GEMINI_API_KEY или проверьте ключ")

    print("🔑 Используем API ключ:", API_KEY[:20] + "...")
    
    # 2) Создаём клиент
    try:
        client = genai.Client(api_key=API_KEY)
        print("✅ Клиент Gemini создан успешно")
    except Exception as e:
        print(f"❌ Ошибка создания клиента: {e}")
        return False

    # 3) Указываем идентификатор модели Imagen 4
    # Попробуем несколько вариантов моделей
    models_to_try = [
        "imagen-4.0-generate-preview-05-20",
        "imagen-3.0-generate-002", 
        "imagen-4.0-ultra-generate-exp-05-20"
    ]
    
    for model_id in models_to_try:
        print(f"\n🤖 Пробуем модель: {model_id}")
        
        try:
            # 4) Формируем запрос
            resp = client.models.generate_images(
                model=model_id,
                prompt="Professional business presentation slide background with abstract geometric patterns, corporate blue and white colors, clean minimal design, 16:9 aspect ratio",
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio="16:9",
                ),
            )

            # 5) Берём результат и сохраняем
            img_bytes = resp.generated_images[0].image.image_bytes
            out_file = Path(f"test_imagen_{model_id.replace('.', '_').replace('-', '_')}.png")
            out_file.write_bytes(img_bytes)

            print(f"✅ Готово! Файл сохранён: {out_file.resolve()}")
            
            # Опционально показываем картинку
            try:
                Image.open(BytesIO(img_bytes)).show()
            except:
                print("📷 Изображение сохранено (автопросмотр недоступен)")
            
            return True
            
        except Exception as e:
            print(f"❌ Ошибка с моделью {model_id}: {e}")
            continue
    
    print("❌ Ни одна модель не сработала")
    return False

def list_available_models():
    """Показывает доступные модели"""
    API_KEY = os.getenv("GEMINI_API_KEY") or "AIzaSyAx3AtOdrqJZ1fnqIE8fSrfiQWS3nHTs2I"
    
    try:
        client = genai.Client(api_key=API_KEY)
        models = client.models.list()
        
        print("\n📋 Доступные модели:")
        for model in models:
            if 'imagen' in model.name.lower() or 'generate' in model.name.lower():
                print(f"  🎨 {model.name}")
            elif 'gemini' in model.name.lower():
                print(f"  🤖 {model.name}")
        
    except Exception as e:
        print(f"❌ Не удалось получить список моделей: {e}")

if __name__ == "__main__":
    print("🎨 ТЕСТ GEMINI + IMAGEN 4")
    print("=" * 50)
    
    # Список моделей
    list_available_models()
    
    # Тест генерации
    print("\n🚀 Запуск теста генерации изображений...")
    success = test_imagen_generation()
    
    if success:
        print("\n🎉 ТЕСТ ПРОЙДЕН! Imagen работает с вашим ключом")
        print("✨ Готов к интеграции в проект презентаций")
    else:
        print("\n⚠️ ТЕСТ НЕ ПРОЙДЕН")
        print("Возможные причины:")
        print("- Ключ неактивен или неверный")
        print("- Нужен платный тариф")
        print("- Модель недоступна в вашем регионе")
        print("- Превышен rate limit")