import os

# OpenAI
AGENTS_OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
AGENTS_MODEL = os.environ.get('AGENTS_MODEL') if os.environ.get('AGENTS_MODEL') is not None else "gpt-3.5-turbo"
AGENTS_MODEL_TEMP = os.environ.get('AGENTS_MODEL_TEMP') if os.environ.get('AGENTS_MODEL_TEMP') is not None else 0
