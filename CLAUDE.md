# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI-powered Python application that automatically generates professional PowerPoint presentations from Markdown content using AI optimization and PowerPoint templates. The system features multi-layered AI processing with Claude for content optimization and Gemini + Imagen 3.0 for image generation.

### Core Architecture

The system consists of five main modules:
- **Content Optimizer**: Uses Claude AI to optimize and reduce large content (300+ slides to ~60)
- **Presentation Enhancer**: Expert-level AI improvement of key slides with specialized prompts
- **Layer 2 Enhancer**: Final optimization of titles, text, and visual layout
- **Image Generator**: AI-powered contextual image generation using Gemini + Imagen 3.0
- **PowerPoint Engine**: Creates slides using PPTX templates with advanced formatting

### Key Components

- Input: `content/content.md` (Markdown file with structured content)
- Template: `tempate/Шаблон презентации 16х9.pptx` (PowerPoint template - note the typo in directory name)
- Processing: Multi-stage AI optimization and presentation generation
- Output: Professional PPTX presentations with AI-generated images

### Data Flow

1. Markdown content is AI-optimized using Claude API (reduces volume by 80-85%)
2. Key slides are enhanced with expert-level analysis and recommendations
3. Titles and layout are optimized in a second enhancement layer
4. Contextual images are generated using Gemini + Imagen 3.0
5. Final presentation is assembled with professional formatting

## Development Commands

```bash
# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export ANTHROPIC_API_KEY="your-anthropic-api-key"
export GEMINI_API_KEY="your-gemini-api-key"

# Run full automated pipeline
python smart_generator.py

# Run individual modules
python content_optimizer.py      # AI content optimization
python presentation_enhancer.py  # Expert enhancement layer 1
python presentation_enhancer_layer2.py  # Enhancement layer 2
python image_generator.py        # AI image generation
python main.py                   # Presentation generation
python test_presentation.py      # Quality testing
```

## API Configuration

The system requires API keys from:
- **Anthropic Claude API** - For content optimization and enhancement
- **Google Gemini API** - For AI image generation with Imagen 3.0

Default model: `claude-sonnet-4-20250514` (most advanced model for content analysis)

## Project Structure

Current implementation includes:
- `content/` - Input Markdown files and optimized versions
- `tempate/` - PowerPoint templates (note: directory name has typo)
- `result/` - Generated presentations and images
- Root level Python modules for each processing stage

## File Processing Pipeline

1. `content.md` → `content_optimized.md` (AI optimization)
2. `content_optimized.md` → `content_enhanced.md` (Expert enhancement)
3. `content_enhanced.md` → `presentation.pptx` (Slide generation)
4. `presentation.pptx` → Enhanced with AI images (Image generation)

## Configuration

Default paths:
- Input: `content/content.md`
- Template: `tempate/Шаблон презентации 16х9.pptx`
- Output: `result/presentation.pptx`
- Max slides: ~60 (optimized from 300+)
- Text optimization: Expert-level content for executives

## Important Notes

- The template directory is named `tempate/` (missing 'l') - maintain this naming for consistency
- System handles Russian/Cyrillic content with proper encoding
- AI models use high creativity (temperature 0.9) for expert-level content
- Image generation targets key slides for maximum visual impact
- Final presentations include alternating text alignment and dynamic layouts