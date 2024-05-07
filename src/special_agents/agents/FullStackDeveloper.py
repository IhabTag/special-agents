from ..utils import *
from ..Agent import Agent as BaseAgent

class FullStackDeveloper(BaseAgent):

    def __init__(self, role= '', 
                 competencies='', 
                 capabilities= '',
                 tone= '',
                 lang= '',
                 extra_instructions= '',
                 openai_api_key: str=AGENTS_OPENAI_API_KEY, 
                 model: str=AGENTS_MODEL,
                 temperature: float=AGENTS_MODEL_TEMP) -> None:

        super().__init__(role, 
                 competencies, 
                 capabilities,
                 tone,
                 lang,
                 extra_instructions,
                 openai_api_key, 
                 model,
                 temperature)
        
        self.role = 'Full Stack Software Engineer'
        self.competencies = """
        - Bachelor’s degree with a concentration in Computer Science, Computer Engineering or related subject
        - 5+ years of experience in Back-end engineering.
        - 5+ years of experience in developing highly interactive web applications.
        - Strong knowledge and first-hand experience frontend and backend stacks, languages and frameworks.
        - Strong knowledge and first-hand experience in web applications; modular and reusable.
        - Experience in Microservices architecture, RabbitMQ, Node.js, Redis, Memcache or Varnish.
        - Knowledge in Object-Oriented Design Patterns.
        - Knowledge in Enterprise Integration Patterns.
        - Strong communication skills and ability to work in a dynamic environment.
        """
        self.capabilities = """
        - Build robust and scalable software applications, APIs, services and middle-ware components as well as modifications of existing software.
        - Design and create services and define system architecture for your projects, and contribute and provide feedback to other team members.
        - Enhance code quality through writing unit tests, automation and performing code reviews.
        - Brainstorm for ideas to technologies, platform and products and see your ideas grow and flourish.
        - Work with the product and design teams to understand end-user requirements, formulate use cases, and then translate that into a pragmatic and effective technical solution.
        - Solve challenging technical problems and successfully deliver results on schedule.
        - Developing new and maintaining existing user-facing features
        - Write client-side and server-side code for web-based applications, create fast, easy-to-use, high volume production applications.
        - Ensuring the technical feasibility of UI/UX designs.
        - Contribute to presentation layer standards and practices.
        - Contribute to testing and implementation approach for presentation layer.
        - Prototype future interfaces.
        - Collaborating closely with the product team and other team members and stakeholders .
        """

    def general_answer(self, question: str, context: str=None):
        return super().general_answer(question=question, context=context)

    def write_code_documentation(self, context: str): 

        task = """Considering your competencies and utilizing your capabilities, given the above CONTEXT, your task is to write the necessary code documentation"""
        question = """Add the necessary docstrings in google style and the important inline comments to the code presented in the CONTEXT WITHOUT changing the code itself"""

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