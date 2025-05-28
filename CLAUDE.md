# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python application that automatically generates PowerPoint presentations from RTF content files using PowerPoint templates. The system parses structured RTF documents, processes the content, and creates formatted slides using a provided POTM template.

### Core Architecture

The system consists of four main modules:
- **RTF Parser**: Extracts headings and content from RTF files, preserving document structure
- **Content Processor**: Optimizes text for slide format, handles bullet points, and splits long content
- **PowerPoint Engine**: Creates slides using POTM templates and applies formatting
- **Main Controller**: Orchestrates the entire process from input to output

### Key Components

- Input: `content/content1` (RTF file with structured content)
- Template: `tempate/tempate1.potm` (PowerPoint template - note the typo in directory name)
- Processing: Python modules for parsing, content optimization, and slide generation
- Output: Generated PPTX presentations

### Data Flow

1. RTF file is parsed to extract headings (Heading 1, Heading 2) and associated content
2. Content is processed and optimized for slide format (max 500 chars per slide)
3. Slides are created using the POTM template with proper formatting
4. Final presentation is saved as PPTX

## Development Commands

```bash
# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install python-pptx striprtf python-docx pathlib2

# Run the application
python main.py

# Run with custom parameters
python main.py --input content/content1 --template tempate/tempate1.potm --output output/presentation.pptx
```

## Project Structure

The planned structure includes:
- `src/` - Core modules (rtf_parser.py, content_processor.py, powerpoint_engine.py, main_controller.py, data_models.py)
- `content/` - Input RTF files
- `tempate/` - PowerPoint templates (note: directory name has typo)
- `output/` - Generated presentations
- `config/` - Configuration settings
- `tests/` - Test files

## Configuration

Default configuration expects:
- Input RTF: `/Users/NVE/Documents/my_program/goznak_adhoc/content/content1`
- Template: `/Users/NVE/Documents/my_program/goznak_adhoc/tempate/tempate1.potm`
- Output directory: `/Users/NVE/Documents/my_program/goznak_adhoc/output/`
- Max slides: 100
- Max text per slide: 500 characters

## Important Notes

- The template directory is named `tempate/` (missing 'l') - maintain this naming for consistency
- RTF content file lacks extension but is in RTF format (version 1, ANSI, code page 1251)
- System is designed to handle Russian/Cyrillic content (code page 1251)
- Target output is approximately 100 slides from structured RTF content