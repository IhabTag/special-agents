from ..utils import *
from ..Agent import Agent as BaseAgent

class ProductManager(BaseAgent):

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
        
        self.role = 'Product Manager'
        self.competencies = """
        -BS in Computer Science or equivalent industry experience
        -2+ years of product management or related industry experience
        -1+ years of experience working on a B2B SaaS product
        -High level of understanding of web development practices
        -Strong understanding of digital analytics and conversion rate optimization processes
        -Strong ability to refine and priorities product backlog in fast-moving environment
        -Strong understanding of the Digital ecosystem, website design, content types, mobile and tablet applications, web technologies and digital marketing best practices.
        -Proficient at writing user stories and defining acceptance criteria
        -Experience going through a full product lifecycle, integrating customer feedback into product requirements.
        -Excellent analytical skills, with the ability to interrogate project metrics to identify areas for continuous improvement
        -Excellent written and verbal communication skills with business and technicalstakeholders at all levels
        """
        self.capabilities = """
        -Owning the product vision and key objectives ensuring this aligns to the overall Business goals.
        -Delivering and maintaining the roadmap and product strategy
        -Producing product performance reports
        -Partnering with UX team to build delightful features with solid designs
        -Transforming ideas and feedback into a product vision and roadmap
        -Understanding with customer problems in order to collect user needs, requirements, and pain points
        -Utilizing performance metrics and data analysis to refine and improve product impact
        -Working closely with the Technical team to execute and deliver roadmap milestones.
        -Understand, communicate and drive optimization of all leading metrics and KPIs 
        """

    def general_answer(self, question: str, context: str=None):
        return super().general_answer(question=question, context=context)


    def write_user_story(self, context: str):
        """
        Write the best user story based on the given context.

        Args:
            context (str): The context for writing the user story.

        Returns:
            str: The detailed user story including acceptance criteria.
        """

        # Define the task and question for the user story
        task = """Considering your competencies and utilizing your capabilities, given the above CONTEXT, your task is to write the best user story."""
        question = """Write the detailed user story including its acceptance criteria in the following format:
        Background: [one sentence]
        Scenario: [the user story]
        Acceptance Criteria: [bullet points]"""

        # Call the openai_answer function to generate the user story
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
    
    def write_release_notes(self, context: str):
        """
        Write the release notes based on the given context.

        Args:
            context (str): The context for writing the release notes.

        Returns:
            str: The detailed release notes.
        """

        # Define the task and question for the release notes
        task = """Considering your competencies and utilizing your capabilities, given the above CONTEXT, your task is to write the release notes."""
        question = """Write the detailed release notes including its acceptance criteria in the following format:
        Overview
        [brief overview in less than 5 sentences]
        
        New Features 
        [review of the new features in bullet points]
        
        Features Enhancements
        [review of the enhancements in bullet points]
        
        Fixed Issues
        [review of the bug fixes and fixed issues in bullet points]"""

        # Call the openai_answer function to generate the user story
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