from pathlib import Path

AUTHOR = "Antonia Scherz"
CONFERENCE_DATE = "April 19th, 2022"
CONFERENCE_NAME = "PyCon Berlin 2022"
TITLE = "Unlocking Information 🔓 Creating Synthetic Data for Open Access"
TITLE_SHORT = "Synthetic Data 🔓"

ROOT_DIR = Path(__file__).resolve().parent
IMAGES_DIR = ROOT_DIR / "images"
PAGES_DIR = ROOT_DIR / "pages"
CODE_SAMPLES_DIR = ROOT_DIR / "code_snippets"

CONFERENCE_LOGO_PATH = IMAGES_DIR / "PyConDE_PyDataBer_circle_trans_500.png"
#CONFERENCE_FULL_LOGO_PATH = IMAGES_DIR / "PyConDEPyDataBER-1800-transparent.png"

# CSS STYLES
#FULL_HEIGHT_PIXELS = 760
#
## Pipeline code
#CODE_DIR = ROOT_DIR / "src"
#PIPELINE_PATH = CODE_DIR / "dvc.yaml"
#PARAMS_PATH = CODE_DIR / "params.yaml"

# Pages
CHAPTER_INTRO = "🙋 Intro"
CHAPTER_GENERATION= "👷🏿 Generate"
CHAPTER_EVALUATION = "🕵️ Evaluate"
CHAPTER_SCALE = "🧑🏽‍🚀 Scale"
CHAPTER_APPLICATION= "🧑🏽‍🎨 Apply"
CHAPTER_OUTRO = "🏃 Outro"

CHAPTERS = [
    CHAPTER_INTRO,
    CHAPTER_GENERATION,
    CHAPTER_EVALUATION,
    CHAPTER_SCALE,
    CHAPTER_APPLICATION,
    CHAPTER_OUTRO,
]

PATH_INTRO="pages/generation/generation.py"
PATH_GENERATION = "pages/ray.py"
PATH_EVALUATION = "pages/evaluation",
PATH_SCALE = "pages/ray.py"
PATH_APPLICATION = "pages/public_data.py"
PATH_OUTRO = "pages/outro"

PAGE_PATHS = [
    PATH_INTRO,
    PATH_GENERATION,
    PATH_EVALUATION,
    PATH_SCALE,
    PATH_APPLICATION,
    PATH_OUTRO
]