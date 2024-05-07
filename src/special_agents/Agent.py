
from .utils import *
from .config import *

class Agent:

    def __init__(self, role= '', 
                 competencies='', 
                 capabilities= '',
                 tone= '',
                 lang= 'same',
                 extra_instructions= '',
                 openai_api_key: str=AGENTS_OPENAI_API_KEY, 
                 model: str=AGENTS_MODEL,
                 temperature: float=AGENTS_MODEL_TEMP) -> None:
        
        self.role = role
        self.competencies = competencies
        self.capabilities = capabilities
        self.tone = tone
        self.lang = lang
        self.extra_instructions = extra_instructions
        self.openai_api_key = openai_api_key
        self.model = model
        self.temperature = temperature

    def general_answer(self, question: str, context: str=None):

        task = """Given the above CONTEXT, your task is to answer the following question: """

        response = openai_answer(role=self.role,
                                 competencies=self.competencies,
                                 capabilities=self.capabilities,
                                 task=task,
                                 question=question,
                                 context=context,
                                 lang=self.lang,
                                 tone=self.tone,
                                 extra_instructions=self.extra_instructions,
                                 openai_api_key=self.openai_api_key,
                                 model=self.model)
        return response