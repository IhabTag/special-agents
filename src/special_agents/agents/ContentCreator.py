from ..utils import *
from ..Agent import Agent as BaseAgent

class ContentCreator(BaseAgent):

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
        
        self.role = 'Content Creator'
        self.competencies = """
        Expert in personal and business branding tactics
        Outstanding copywriting, social media, or video production skills
        Strong knowledge of SEO best practices
        Significant experience creating high-quality marketing content
        Capable of managing multiple competing priorities
        Comprehensive understanding of impactful marketing tactics
        Identify customers’ needs and recommend new topics

        """
        self.capabilities = """
        
        Create and publish engaging content for various platforms such as website, social media, blog, etc.
        Use SEO best practices to drive traffic to digital channels
        Collaborate across teams to determine and solve campaign objectives
        Monitor digital engagement metrics
        Promote offerings to reach new audiences
        Research market trends and developments relevant to campaign subject matter

        """

    def general_answer(self, question: str, context: str=None):
        return super().general_answer(question=question, context=context)

    def write_linkedin_post(self, context: str): 

        task = """Considering your competencies and utilizing your capabilities, given the above CONTEXT, your task is to write a social media post that suits LinkedIn."""
        question = """Write a compelling LinkedIn post rich in details that considers the best practices and promotes users to engage and interact for the post to go viral for the audience most relevant to the CONTEXT."""

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
    
    def write_facebook_post(self, context: str): 

        task = """Considering your competencies and utilizing your capabilities, given the above CONTEXT, your task is to write a social media post that suits Facebook."""
        question = """Write a compelling rich in details Facebook post that considers the best practices and promotes users to engage and interact for the post to go viral for the audience most relevant to the CONTEXT."""

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
    
    def write_blog_article(self, context: str): 

        task = """Considering your competencies and utilizing your capabilities, given the above CONTEXT, your task is to write a blog article."""
        question = """Write a compelling long blog article rich in details that considers the best SEO practices using the appropriate keywords for the audience most relevant to the CONTEXT."""

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