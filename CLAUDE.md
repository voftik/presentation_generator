# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a universal Python console utility for automatically generating PowerPoint presentations from text content and design templates. The script is developed by RW Tech (Revolutionary Workflows & Technology Solutions) as a versatile presentation creation system. The generator creates professional presentations with proper 16:9 aspect ratio, dynamic layouts, AI-powered illustrations, and modern branding.

## Architecture

### Enhanced Class Architecture
The application uses multiple specialized classes for improved user experience and functionality:

```python
class ProgressBar:              # Animated progress tracking
class ASCIIArt:                # Beautiful console headers and UI
class ColorfulUI:              # Enhanced user experience with colors/animations  
class PromptTemplates:         # AI prompt management system
class ExecutionStats:          # Comprehensive statistics tracking
class ExecutionCheckpoints:    # Validation checkpoint system
class RWTechPPTXGenerator:     # Main generator class
    def __init__(self):
        # Configuration and state management
        self.slides_data = []        # Parsed slide content
        self.template_images = []    # Extracted template images
        self.prs = None             # Active presentation object
```

### Core Components

#### 1. **Strict Validation and Quality Control System**
**ExecutionStats Class** - Comprehensive statistics tracking:
- Tracks API validation attempts and success
- Monitors prompts generation (attempted/successful/failed)
- Tracks images generation (attempted/successful/failed)
- Records images inserted into presentation
- Calculates success rates and execution time
- Provides detailed final reports with 80% success rate requirements

**ExecutionCheckpoints Class** - Mandatory validation points:
- `api_validation` - Ensures API keys are valid before proceeding
- `prompts_generation` - Requires minimum 80% success rate
- `images_generation` - Requires minimum 80% success rate  
- `presentation_update` - Validates images were actually inserted into presentation
- `final_validation` - Comprehensive result verification with file integrity checks

#### 2. **API Key Validation System** (`_validate_and_update_api_keys()`)
- Strict validation loop with maximum 3 attempts per API
- Real connection testing to Claude and OpenAI endpoints
- Interactive error recovery with specific recommendations
- Automatic configuration saving for valid keys
- **CRITICAL**: Program terminates with `sys.exit()` on validation failure

#### 3. **File Validation** (`validate_files()`)
- Checks existence of source files before processing
- Creates output directories if missing (including history)
- Provides informative Russian error messages
- Stops execution on critical errors

#### 4. **Content Parser** (`parse_content()`, `_parse_slide_content()`)
- Reads and parses `slide_content.txt` using regex patterns
- Extracts slide numbers, titles, and body content
- Determines slide types automatically
- Ignores illustration descriptions marked with `**Иллюстрация:**`
- Handles 60 slides in structured format

#### 5. **Template Handler** (`load_template()`)
- Loads PowerPoint template and preserves 16:9 aspect ratio
- Extracts images from first slide with all properties (position, size, rotation)
- Stores template presentation object for consistent sizing
- Maintains corporate styling and branding elements

#### 6. **Slide Generation Engine** (`generate_presentation()`, `_create_slide()`)
- Creates presentation based on template to preserve aspect ratio
- Removes template slides while keeping layouts and sizing
- Generates each slide with appropriate content and styling
- Maintains slide numbering and type determination

#### 7. **AI Illustrations System** (`_process_ai_illustrations_parallel()`)
- **Multiple AI Models**: DALL-E 3, GPT-Image-1, Gemini 2.0 Flash, Imagen 3
- **Parallel Processing**: Threading support for 2.4x speed improvement
- **Claude API Integration**: Generates intelligent image prompts with context awareness
- **Advanced Prompt Templates**: Structured prompt generation system
- **Smart Filtering**: Skips special slides (title, quotes, breaks)
- **Configurable Intervals**: Every 3rd, 5th, 10th, or custom slide
- **Quality Control**: Enforces 80% success rate requirement with mandatory stops

#### 8. **Image Processing and Insertion System** (`_update_presentation_with_images()`)
- **Presentation Loading**: Opens existing base presentation for image insertion
- **Adaptive Positioning**: Places images opposite to text blocks (40% slide width)
- **Dynamic Layout**: Even slides (text left, image right), odd slides (text right, image left)  
- **Aspect Ratio Preservation**: Maintains 16:9 ratio for all AI-generated images
- **File Creation**: Generates `Goznak_AI_training_1_illustrated.pptx` as final output
- **Statistics Integration**: Updates `images_inserted` counter for validation

#### 9. **Enhanced UI System**
- **ProgressBar Class**: Animated progress tracking with spinners and bars
- **ASCIIArt Class**: Beautiful console headers and visual elements
- **ColorfulUI Class**: Enhanced user experience with colors, animations, and emojis
- **Interactive Prompts**: User-friendly configuration and error recovery
- **Real-time Status**: Live updates during long-running operations

#### 10. **History Management System** (`_save_generation_history()`)
- **Timestamped Archives**: Creates `/history/generation_YYYYMMDD_HHMMSS/` directories
- **Metadata Preservation**: Comprehensive JSON with all generation statistics
- **Asset Archiving**: Copies prompts, images, presentations, and logs
- **Smart Cleanup**: Removes temporary files only after history is saved
- **Recovery Support**: Enables reuse of previous generations for debugging/modification

#### 11. **Content Rendering System**
Two distinct rendering pathways:

**Special Slides** (`_add_special_slide_content()`):
- Handles title slide (СЛАЙД 1), quotes, and breaks
- Centers content both horizontally and vertically
- Uses larger font size (40pt Montserrat)
- Combines title and body into single text block
- Removes all borders and backgrounds

**Normal Slides** (`_add_normal_slide_content()`, `_add_styled_body_text()`):
- Creates dynamic layouts with alternating text positions
- Uses 50% slide width for text blocks
- Implements 1.5 line spacing for better readability
- Alternates left/right positioning based on slide number
- Maintains separate title and body sections

### Directory Structure
```
/Users/NVE/Documents/my_program/RW_slide_generator/
├── pptx_content/
│   └── slide_content.txt                    # 60 slides in structured format
├── pptx_template/
│   └── Шаблон презентации 16х9.pptx        # Corporate template (16:9)
├── pptx_result/                             # Presentation output directory
│   ├── RWTech_Universal_Presentation.pptx  # Base presentation (always created)
│   └── RWTech_Universal_Presentation_Illustrated.pptx # Final presentation with AI images
├── history/                                 # Persistent generation history
│   ├── generation_20250602_142530/         # Timestamped generation archive
│   │   ├── metadata.json                   # Complete generation statistics
│   │   ├── prompts/                        # Archived AI prompts
│   │   │   ├── slide_05_prompt.txt         # Claude-generated prompts
│   │   │   ├── slide_10_prompt.txt
│   │   │   └── ...
│   │   ├── images/                         # Archived AI images
│   │   │   ├── slide_05_illustration.png   # DALL-E 3 generated images
│   │   │   ├── slide_10_illustration.png
│   │   │   └── ...
│   │   ├── presentation_20250602_142530.pptx # Final presentation copy
│   │   └── generation.log                  # Execution log copy
│   ├── generation_20250602_151245/         # Another generation archive
│   └── ...
├── prompts_for_img/                         # Temporary AI prompts (cleaned after success)
├── img_generated/                           # Temporary AI images (cleaned after success)
├── logs/                                    # Active execution logs
│   └── generation_YYYYMMDD_HHMMSS.log      # Current operation logs
├── venv/                                    # Virtual environment
├── rwtech_pptx_generator.py                # Main RW Tech script
├── start.py                                 # Main startup script with checks
├── run.sh                                   # Quick start script (macOS/Linux)
├── run.bat                                  # Quick start script (Windows)
├── config.json                             # API keys configuration (auto-created)
├── CLAUDE.md                               # Technical documentation
├── README.md                               # User documentation
├── ЗАПУСК.md                               # Complete user guide (Russian)
├── КОМАНДЫ_ЗАПУСКА.md                      # Quick start commands (Russian)
└── ИТОГ.md                                 # Final system documentation
```

## Development Environment

### Setup Commands
```bash
# RECOMMENDED: Universal runner (full automation)
./run.sh

# Alternative: Comprehensive startup with checks
python start.py

# Manual setup:
python3 -m venv venv
source venv/bin/activate
pip install python-pptx requests tqdm openai google-genai
python rwtech_pptx_generator.py
```

### Dependencies
- **Python 3.7+**
- **python-pptx >= 0.6.21** - PowerPoint manipulation library
- **requests** - HTTP requests for API communication
- **tqdm** - Progress bars for AI generation
- **openai >= 1.0.0** - Updated OpenAI API client for DALL-E 3
- **google-genai** - Google Gemini and Imagen 3 integration
- **packaging** - Version comparison utilities
- **Standard libraries**: os, re, sys, io, json, base64, time, datetime, logging, threading, queue
- **Optional**: BytesIO for image stream handling

## Content Format Specifications

### Input File Structure (`slide_content.txt`)
Each slide follows this exact pattern:
```
### СЛАЙД N: slide_title
**Заголовок:** actual_title_text
**Тело слайда:**
• Bullet point 1
• Bullet point 2
Regular paragraph text
**Иллюстрация:** [description - automatically ignored]
```

### Slide Type Detection
The system automatically detects slide types based on content:

1. **Title Slide**: СЛАЙД 1 or contains "титульный"
2. **Quote Slides**: Contains "цитата" in title
3. **Break Slides**: Contains "перерыв" in title  
4. **Normal Slides**: All others (default)

### Content Processing Rules
- Ignores `**Иллюстрация:**` sections completely
- Preserves bullet points marked with `•`
- Maintains paragraph structure and line breaks
- Processes Cyrillic text correctly

## Visual Design System

### Special Slides Styling
- **Font**: Montserrat 40pt
- **Alignment**: Center (horizontal and vertical)
- **Layout**: Single unified text block
- **Content**: Title and body combined
- **Borders**: None (transparent)

### Normal Slides Styling
- **Title**: Montserrat 30pt, bold, top of slide
- **Body**: Montserrat 18pt, 1.5 line spacing
- **Width**: 50% of slide width
- **Position**: Alternates left (even slides) / right (odd slides)
- **Margins**: 5% from slide edges

### Layout Algorithm
```python
# Position determination
is_left_aligned = (slide_number % 2 == 0)  # Even = left, Odd = right

# Text block sizing
text_width = slide_width * 0.5              # 50% width
margin = slide_width * 0.05                 # 5% margin

# Positioning calculation
if is_left_aligned:
    left = margin
else:
    left = slide_width - text_width - margin
```

## Key Processing Workflow

### 1. Initialization Phase
```python
def __init__(self):
    # Set up file paths
    # Initialize ExecutionStats and ExecutionCheckpoints
    # Load configuration (API keys)
    # Set up logging system
```

### 2. Strict Validation Phase
```python
def validate_files(self):
    # Check content file exists
    # Check template file exists  
    # Create output directories
```

### 3. AI Setup Phase (if enabled)
```python
def setup_ai_illustrations(self):
    # Interactive or automatic mode selection
    # Configure generation intervals
    # Set AI illustration parameters
```

### 4. API Validation Phase (CRITICAL)
```python
def _validate_and_update_api_keys(self):
    # Test Claude API connection (real request)
    # Test OpenAI API connection (real request) 
    # Interactive error recovery
    # Maximum 3 attempts per API
    # MANDATORY: sys.exit() on failure
```

### 5. Content Processing Phase
```python
def parse_content(self):
    # Read slide_content.txt
    # Parse using regex: r'### СЛАЙД (\d+): (.+?)(?=### СЛАЙД \d+:|$)'
    # Extract titles and bodies
    # Determine slide types
    # Update statistics
```

### 6. Template Analysis Phase
```python
def load_template(self):
    # Load template presentation
    # Extract images from first slide
    # Store image properties (position, size, rotation)
    # Verify aspect ratio (should be 1.78 for 16:9)
```

### 7. Base Presentation Generation Phase
```python
def generate_presentation(self):
    # Create presentation from template (preserves 16:9)
    # Clear template slides
    # Generate each slide with content
    # Apply appropriate styling based on type
    # Save base presentation: Goznak_AI_training_1.pptx
```

### 8. AI Illustrations Phase (if enabled)
```python
def _process_ai_illustrations(self):
    # CHECKPOINT: Validate API keys
    # Generate prompts with Claude API (80% success required)
    # CHECKPOINT: Validate prompts generation
    # Generate images with DALL-E 3 (80% success required)  
    # CHECKPOINT: Validate images generation
    # Insert images into presentation
    # CHECKPOINT: Validate presentation update
    # MANDATORY: sys.exit() on critical failures
```

### 9. Image Processing and Insertion Phase
```python
def _update_presentation_with_images(self):
    # Load existing base presentation
    # Calculate adaptive positioning for each image
    # Insert images with proper scaling and positioning
    # Save illustrated presentation: Goznak_AI_training_1_illustrated.pptx
    # Update statistics: images_inserted counter
```

### 10. Final Validation Phase (CRITICAL)
```python
def validate_final_result(self):
    # Determine final file (illustrated vs base)
    # Check file exists and size is adequate
    # Verify slide count matches expected
    # Validate AI images were actually inserted (if enabled)
    # Test presentation can be opened without corruption
    # MANDATORY: sys.exit() on validation failure
```

### 11. History Management Phase
```python
def _save_generation_history(self):
    # Create timestamped directory: /history/generation_YYYYMMDD_HHMMSS/
    # Save metadata.json with complete statistics
    # Archive prompts directory
    # Archive images directory  
    # Archive final presentation
    # Archive execution log
```

### 12. Cleanup and Success Reporting Phase
```python
def _cleanup_partial_results(save_history=True/False):
    # Save generation history (if requested)
    # Remove temporary prompts directory
    # Remove temporary images directory
    # Keep only final results and history

def execution_stats.print_final_report(self):
    # Detailed statistics report
    # Success rate calculations
    # Performance metrics
    # Final validation status
```

## Error Handling Strategy

### Strict Validation and Quality Control
**CRITICAL PRINCIPLE**: Program NEVER reports success unless ALL validation checkpoints pass

#### Exit Codes System
- `sys.exit(0)` - Complete success (all validations passed)
- `sys.exit(1)` - API validation checkpoint failure
- `sys.exit(2)` - Prompts generation checkpoint failure  
- `sys.exit(3)` - Prompts success rate below 80%
- `sys.exit(4)` - Images generation checkpoint failure
- `sys.exit(5)` - Images success rate below 80%
- `sys.exit(6)` - Presentation update checkpoint failure
- `sys.exit(7)` - Final validation failure
- `sys.exit(8)` - Final checkpoint validation failure
- `sys.exit(9)` - Success with warnings
- `sys.exit(10)` - Invalid API keys (user aborted)

#### API Validation Errors
- **401 Unauthorized** → Interactive key replacement + detailed diagnostics
- **429 Rate Limited** → Wait recommendation + balance check
- **404 Not Found** → Endpoint verification + key validation
- **Connection Errors** → Network troubleshooting + retry options
- **Timeout** → Server status check + retry with delay

#### Quality Control Checkpoints
- **API Validation**: Must pass before AI generation starts
- **Prompts Generation**: Minimum 80% success rate required
- **Images Generation**: Minimum 80% success rate required  
- **Presentation Update**: All generated images must be inserted
- **Final Validation**: File integrity and completeness check

#### Cleanup on Failure
- **Partial Results Cleanup**: `_cleanup_partial_results()` removes incomplete files
- **Graceful Degradation**: Falls back to standard mode if AI fails
- **Resource Management**: Proper cleanup of API connections and file handles

### File Validation
- Missing content file → Exit with Russian error message
- Missing template file → Exit with Russian error message  
- Invalid template → Exit with validation error
- Missing output directory → Auto-create

### Content Processing
- No slides found → Exit with parsing error
- Invalid slide format → Skip and continue
- Empty content → Create slide with title only

### Image Processing
- Missing images in template → Continue without images
- Invalid image data → Skip problematic image
- Image positioning errors → Use default positioning

## Technical Implementation Details

### Aspect Ratio Preservation
```python
# CRITICAL: Use template as base to preserve 16:9
self.prs = Presentation(self.template_file)  # Not Presentation()

# Verify aspect ratio
ratio = self.prs.slide_width / self.prs.slide_height  # Should be ~1.78
```

### Image Extraction and Replication
```python
# Extract from template
for shape in first_slide.shapes:
    if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
        image_data = {
            'image_blob': shape.image.blob,  # Binary data
            'left': shape.left,              # X position
            'top': shape.top,                # Y position  
            'width': shape.width,            # Width
            'height': shape.height,          # Height
            'rotation': getattr(shape, 'rotation', 0)  # Rotation
        }

# Apply to each slide
for img_data in self.template_images:
    image_stream = BytesIO(img_data['image_blob'])
    pic = slide.shapes.add_picture(image_stream, ...)
```

### Dynamic Text Positioning
```python
def _add_styled_body_text(self, slide, body_text, is_left_aligned):
    # Calculate position based on slide dimensions
    slide_width = self.prs.slide_width
    text_width = slide_width * 0.5
    
    # Position logic
    if is_left_aligned:
        left = margin
    else:
        left = slide_width - text_width - margin
```

### AI Image Processing Architecture

#### Image Generation Pipeline
```python
# 1. Prompt Generation
def _generate_image_prompt(self, slide_data):
    # Send slide content to Claude API
    # Generate contextual DALL-E prompt
    # Save prompt to prompts_for_img/slide_XX_prompt.txt
    
# 2. Image Generation  
def _generate_image_with_dalle(self, prompt, slide_number):
    # Send prompt to DALL-E 3 API
    # Request 1792x1024 format (16:9 aspect ratio)
    # Save image to img_generated/slide_XX_illustration.png
    
# 3. Image Insertion
def _update_presentation_with_images(self, slides_to_process):
    # Load base presentation
    # For each generated image:
    #   - Calculate adaptive position (opposite to text)
    #   - Scale to 40% slide width
    #   - Maintain aspect ratio
    #   - Insert into presentation
    # Save as Goznak_AI_training_1_illustrated.pptx
```

#### Adaptive Image Positioning System
```python
# Position Calculation Algorithm
slide_width = prs.slide_width
slide_height = prs.slide_height

# Image dimensions (40% of slide width)
image_width = int(slide_width * 0.4)
margin = int(slide_width * 0.05)

# Position logic (opposite to text)
if slide_number % 2 == 0:  # Even slides
    # Text on left, image on right
    image_left = slide_width - image_width - margin
else:  # Odd slides  
    # Text on right, image on left
    image_left = margin

# Vertical centering with header compensation
title_height = int(slide_height * 0.15)
available_height = slide_height - title_height - int(slide_height * 0.1)
image_top = title_height + (available_height - image_height) // 2
```

#### History Management Architecture
```python
# Directory Structure Creation
history_base = "/path/to/history"
generation_dir = f"{history_base}/generation_{timestamp}"

# Metadata Preservation
metadata = {
    'timestamp': timestamp,
    'date': datetime.now().isoformat(),
    'total_slides': 60,
    'ai_mode': True/False,
    'slide_interval': 5,
    'prompts_attempted': count,
    'prompts_generated': count,
    'images_attempted': count,
    'images_generated': count,
    'images_inserted': count,
    'success': boolean
}

# Asset Archival Process
1. Copy prompts_for_img/ -> history/generation_XXX/prompts/
2. Copy img_generated/ -> history/generation_XXX/images/  
3. Copy final presentation -> history/generation_XXX/presentation_XXX.pptx
4. Copy execution log -> history/generation_XXX/generation.log
5. Clean temporary directories
```

## Testing and Validation

### Expected Outputs

#### Standard Mode
- **Base Presentation**: `Goznak_AI_training_1.pptx`
- **Slide Count**: Exactly 60 slides
- **Aspect Ratio**: 1.78 (16:9 format)
- **Images Per Slide**: 2 (from template)
- **File Size**: ~150KB (base presentation)
- **Exit Code**: 0 for success, 9 for success with warnings

#### AI Illustrations Mode
- **Base Presentation**: `Goznak_AI_training_1.pptx` (created first)
- **Illustrated Presentation**: `Goznak_AI_training_1_illustrated.pptx` (final output)
- **AI Images**: ~12 images (every 5th slide by default)
- **Image Format**: 1792x1024 PNG files
- **Total File Size**: ~10-50MB (depending on image content)
- **History Archive**: `/history/generation_YYYYMMDD_HHMMSS/`
- **AI Success Rate**: Minimum 80% for prompts and images
- **Exit Code**: 0 for complete success, 1-10 for various error types

#### Generated Assets
```
pptx_result/
├── Goznak_AI_training_1.pptx                # Base presentation (always)
└── Goznak_AI_training_1_illustrated.pptx    # With AI images (if AI enabled)

history/generation_YYYYMMDD_HHMMSS/
├── metadata.json                             # Complete statistics
├── prompts/                                  # Archived prompts
├── images/                                   # Archived images  
├── presentation_YYYYMMDD_HHMMSS.pptx        # Final presentation copy
└── generation.log                            # Execution log
```

### Visual Verification Checklist
1. **Slide 1**: Centered title slide with 40pt text
2. **Slide 2**: Left-aligned text block, 50% width, 1.5 spacing
3. **Slide 3**: Right-aligned text block, 50% width, 1.5 spacing
4. **Quote slides** (5, 35, 55): Centered 40pt text
5. **Break slides** (19, 39, 50, 56): Centered 40pt text

### Technical Verification
```bash
# Standard mode (recommended for testing)
echo "" | python rwtech_pptx_generator.py

# Expected successful output:
# ✓ Найдено слайдов: 60
# ✓ Извлечено изображений: 2  
# ✓ Соотношение сторон: 1.78
# ✅ ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ УСПЕШНО!
# 🎉 ПРОГРАММА ЗАВЕРШЕНА УСПЕШНО!
# Exit code: 0

# AI mode testing (requires valid API keys)
python rwtech_pptx_generator.py
# Answer "да" to AI illustrations
# Provide valid Claude and OpenAI API keys
# Expected: 80%+ success rate for AI generation

# Check exit codes
echo $?  # Should be 0 for success, 1-10 for various errors
```

### Validation Commands
```bash
# Check file structure after generation
ls -la pptx_result/
ls -la logs/
ls -la prompts_for_img/  # If AI enabled
ls -la img_generated/    # If AI enabled

# Verify presentation integrity
python -c "
from pptx import Presentation
prs = Presentation('pptx_result/Goznak_AI_training_1.pptx')
print(f'Slides: {len(prs.slides)}')
print(f'Ratio: {prs.slide_width/prs.slide_height:.2f}')
"
```

## Critical Path Configuration Issue

**URGENT FIX REQUIRED**: The main script contains a hardcoded path that will prevent execution:

```python
# Line 590 in goznak_pptx_generator.py - INCORRECT:
self.base_path = "/Users/NVE/Documents/my_program/goznak_adhoc_script"

# Should be:
self.base_path = os.getcwd()  # Use current working directory
```

This hardcoded path must be changed to ensure the script works for all users.

## Startup Scripts

### Enhanced Startup Options
The project provides multiple startup methods with increasing levels of automation:

1. **Universal Runner** (`./run.sh`) - **RECOMMENDED**
   - Full dependency management and environment setup
   - Automatic virtual environment creation/update
   - Comprehensive system validation
   - Beautiful animated UI with progress tracking

2. **Comprehensive Startup** (`python start.py`)
   - System checks and validation
   - Interactive dependency installation
   - Configuration verification
   - Manual control over the process

3. **Direct Execution** (`python rwtech_pptx_generator.py`)
   - Expert mode for experienced users
   - Assumes environment is properly configured

## Troubleshooting

### Common Issues

#### Path Configuration Problems
1. **Error**: `FileNotFoundError: slide_content.txt not found`
   - **Cause**: Hardcoded path in __init__ method
   - **Solution**: Update line 590 in goznak_pptx_generator.py:
     ```python
     self.base_path = os.getcwd()
     ```

#### System Dependencies
1. **ModuleNotFoundError: pptx**
   - Solution: `pip install python-pptx requests tqdm` in virtual environment

2. **Python version incompatibility**
   - Required: Python 3.7+
   - Check: `python --version`

#### Presentation Generation
3. **Aspect ratio 1.33 instead of 1.78**
   - Issue: Creating new presentation instead of using template
   - Solution: Ensure using `Presentation(template_file)`

4. **Images not appearing**
   - Check template has images on first slide
   - Verify image extraction logs show count > 0

5. **Text positioning issues**
   - Verify slide numbering starts from 1
   - Check left/right alternation logic

#### AI Illustrations Issues  
6. **API validation failure (Exit code 10)**
   - Invalid API keys → Check key format and permissions
   - Network issues → Verify internet connection
   - Rate limits → Check account balance and limits

7. **Low success rate errors (Exit codes 3, 5)**
   - Prompts < 80% success → Check Claude API key and quotas
   - Images < 80% success → Check OpenAI API key and credits
   - Network instability → Retry with better connection

8. **Final validation failure (Exit code 7)**
   - File size too small → Check AI images were generated
   - Wrong slide count → Verify content parsing worked
   - Corrupted file → Check available disk space

#### Quality Control Issues
9. **Program exits with error codes 1-8**
   - **Systematic approach**: Check logs in `/logs/` directory
   - **Specific diagnostics**: Each exit code has detailed error messages
   - **Recovery options**: Program provides interactive recovery paths

### Debug Information
The script outputs detailed logging:
```
Размер слайда в шаблоне: 12192000 x 6858000
Соотношение сторон шаблона: 1.78
Размер слайда в новой презентации: 12192000 x 6858000
Соотношение сторон новой презентации: 1.78
```

## Performance Characteristics

### Processing Speed
- **Content parsing**: ~0.1 seconds
- **Template loading**: ~0.2 seconds  
- **Slide generation**: ~2-3 seconds (60 slides)
- **Image replication**: ~1-2 seconds (120 total images)
- **Total runtime**: ~3-5 seconds

### Memory Usage
- **Base script**: ~5-10MB
- **Template images**: ~2-5MB per slide
- **Peak usage**: ~50-100MB during generation

## Performance Characteristics

#### Standard Mode
- **Content parsing**: ~0.1 seconds
- **Template loading**: ~0.2 seconds  
- **Slide generation**: ~2-3 seconds (60 slides)
- **Image replication**: ~1-2 seconds (120 total images)
- **Validation**: ~0.1 seconds
- **Total runtime**: ~3-5 seconds

#### AI Mode  
- **API validation**: ~5-10 seconds (both APIs)
- **Prompt generation**: ~2-5 minutes (12 slides with delays)
- **Image generation**: ~3-8 minutes (12 images with delays)
- **Quality control**: ~10-30 seconds
- **Total runtime**: ~5-15 minutes

#### Memory Usage
- **Base script**: ~5-10MB
- **Template images**: ~2-5MB per slide
- **AI images**: ~2-10MB per generated image
- **Peak usage**: ~50-100MB (standard) / ~200-500MB (AI mode)

## Future Enhancement Possibilities

### Potential Improvements
1. **Enhanced Quality Control**: Even stricter validation with custom thresholds
2. **Advanced Error Recovery**: Automatic retry mechanisms for transient failures
3. **Performance Optimization**: Parallel API calls and caching
4. **Multiple AI Providers**: Support for additional image generation APIs
5. **Template Management**: Dynamic template selection and customization
6. **Monitoring Dashboard**: Real-time statistics and performance tracking

### Quality Control Extensions
- **Custom Success Thresholds**: User-configurable minimum success rates
- **Progressive Validation**: Multi-stage validation with early termination
- **Health Monitoring**: API endpoint health checks and status reporting
- **Audit Trails**: Comprehensive operation logging and replay capability

### Extension Points
- Add new validation checkpoints in `ExecutionCheckpoints`
- Enhance statistics tracking in `ExecutionStats`
- Implement additional AI providers in the illustration system
- Add new slide types in `_determine_slide_type()`
- Modify positioning logic in `_add_styled_body_text()`

## Security Considerations

### API Key Management
- Never commit API keys to version control
- Use environment variables or secure configuration files
- Implement key rotation mechanisms
- Monitor for key exposure in logs

### Input Validation
- Sanitize all user inputs for prompt generation
- Validate file paths to prevent directory traversal
- Check file sizes to prevent resource exhaustion
- Implement content filtering for inappropriate material

### Security Issues to Address
**CRITICAL**: The current implementation contains hardcoded API keys in the source code (lines 833-836 in goznak_pptx_generator.py). This is a major security vulnerability that should be fixed immediately:

```python
# NEVER include hardcoded keys in source code:
# fallback_claude_key = "sk-ant-api03-..."  # ❌ SECURITY RISK
# fallback_openai_key = "sk-proj-..."       # ❌ SECURITY RISK

# ✅ Use only environment variables or secure config files:
fallback_claude_key = None   # Will be prompted interactively
fallback_openai_key = None   # Will be prompted interactively
```

**Recommended approach**:
1. Remove all hardcoded API keys from source code
2. Use environment variables: `CLAUDE_API_KEY`, `OPENAI_API_KEY`
3. Use secure config files with proper permissions
4. Never commit API keys to version control

## Development Commands Summary

```bash
# Quick development commands:
./run.sh                    # Full automated setup and run (recommended)
python start.py             # Comprehensive startup with checks
python rwtech_pptx_generator.py  # Direct execution (expert mode)

# Environment management:
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
pip install python-pptx requests tqdm openai google-genai

# Testing and validation:
echo "" | python rwtech_pptx_generator.py  # Standard mode test
python -c "from pptx import Presentation; print('Dependencies OK')"
echo $?  # Check exit code (0 = success)

# File structure validation:
ls -la pptx_result/ logs/ prompts_for_img/ img_generated/
```

This documentation provides comprehensive guidance for maintaining, extending, and troubleshooting the Goznak PPTX Generator with strict validation and quality control.