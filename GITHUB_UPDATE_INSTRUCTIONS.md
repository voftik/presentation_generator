# 📋 Инструкции по обновлению GitHub репозитория

## 🎯 Цель
Полностью заменить содержимое репозитория `presentation_generator` новым кодом RW Tech PPTX Generator v4.0

## 🚀 Способ 1: Через GitHub Web Interface (Рекомендуется)

### Шаг 1: Очистка старого репозитория
1. Перейдите в ваш репозиторий: `https://github.com/ВАШ_USERNAME/presentation_generator`
2. Удалите все старые файлы через веб-интерфейс GitHub
3. Или создайте новый пустой репозиторий

### Шаг 2: Загрузка новых файлов
1. В корне репозитория нажмите "Add file" → "Upload files"
2. Перетащите все файлы из локальной папки `/Users/NVE/Documents/my_program/RW_slide_generator/`
3. Исключите из загрузки:
   - Папку `venv/`
   - Папку `logs/`
   - Папку `history/`
   - Папку `prompts_for_img/`
   - Папку `img_generated/`
   - Файлы `*.log`
   - Файл `config.json`

### Шаг 3: Коммит изменений
Используйте это сообщение коммита:
```
🚀 RW Tech PPTX Generator v4.0 - Complete Rewrite

🎯 Major Features:
- ✨ Complete rebrand from Goznak to RW Tech Universal Generator
- 🎨 Beautiful animated ASCII UI with gradient colors and emojis
- 🤖 Multi-AI model support (DALL-E 3, GPT-Image-1, Gemini 2.0, Imagen 3)
- ⚡ Parallel processing for 2.4x faster AI generation
- 🔧 Enhanced error handling with 80% success rate requirements
- 📊 Comprehensive statistics and quality control system

🛠️ Technical Improvements:
- 🐍 Updated to use current working directory (no hardcoded paths)
- 🎭 New RWTechPPTXGenerator class with modular architecture
- 🎪 Enhanced UI classes: ProgressBar, ASCIIArt, ColorfulUI, PromptTemplates
- 🔄 Robust virtual environment handling in run scripts
- 📝 Universal file naming: RWTech_Universal_Presentation.pptx
- 🏗️ Improved project structure with history management

🎨 UI/UX Enhancements:
- 💎 Revolutionary Workflows & Technology Solutions branding
- 🌟 Gradient color schemes and animated banners
- ⚙️ Tech-themed emoji indicators (⚙️🔧⚡🌟💫✨)
- 🎭 Interactive loading animations and progress tracking
- 🏆 Professional success banners

🚀 New Startup Options:
- ./run.sh - Full automation with dependency management
- ./quick_start.sh - Simplified startup for problem cases  
- python start.py - Comprehensive system diagnostics
- python rwtech_pptx_generator.py - Direct expert mode
```

## 🛠️ Способ 2: Через командную строку (если знаете точный URL)

```bash
cd /Users/NVE/Documents/my_program/RW_slide_generator

# Замените YOUR_USERNAME и YOUR_REPO на правильные значения
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Если репозиторий не пустой, принудительно заменить содержимое
git push --force-with-lease origin main

# Или если репозиторий пустой
git push -u origin main
```

## 📁 Файлы для загрузки в репозиторий

### ✅ Основные файлы:
- `rwtech_pptx_generator.py` - Главный скрипт
- `start.py` - Стартовый модуль с диагностикой
- `run.sh` - Универсальный runner (macOS/Linux)
- `quick_start.sh` - Упрощенный runner
- `run.bat` - Windows runner
- `run_with_venv.py` - Python runner
- `README.md` - Основная документация
- `CLAUDE.md` - Техническая документация
- `.gitignore` - Git ignore правила

### ✅ Документация:
- `ADVANCED_PROMPTING.md`
- `GEMINI_IMAGEN_INTEGRATION.md`
- `GOOGLE_MODELS_INTEGRATION.md`
- `INSTALL_OPENAI.md`
- `PARALLEL_GENERATION.md`
- `UNIVERSAL_RUNNER.md`
- `ЗАПУСК.md`
- `ИТОГ.md`
- `КОМАНДЫ_ЗАПУСКА.md`

### ✅ Контент и шаблоны:
- `pptx_content/slide_content.txt`
- `pptx_template/Шаблон презентации 16х9.pptx`

### ❌ НЕ загружать:
- `venv/` - виртуальное окружение
- `logs/` - логи
- `history/` - история генерации
- `prompts_for_img/` - временные промпты
- `img_generated/` - временные изображения
- `config.json` - содержит API ключи
- `environment_info.txt` - системная информация
- `*.log` - файлы логов

## 🔧 После загрузки

1. Проверьте, что README.md отображается корректно
2. Убедитесь, что файлы `run.sh` и `quick_start.sh` имеют права на выполнение
3. Протестируйте клонирование репозитория и запуск

## 📞 Если нужна помощь

Предоставьте точный URL вашего GitHub репозитория, и я помогу с автоматической загрузкой через git команды.

---
*Создано RW Tech PPTX Generator v4.0* 🚀