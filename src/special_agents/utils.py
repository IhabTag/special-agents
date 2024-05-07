from openai import OpenAI
from .config import *

def openai_answer(role, 
                  competencies, 
                  capabilities, 
                  task, 
                  question, 
                  context=None, 
                  lang='same', 
                  tone='friendly', 
                  temperature=AGENTS_MODEL_TEMP, 
                  extra_instructions='', 
                  openai_api_key=AGENTS_OPENAI_API_KEY, 
                  model=AGENTS_MODEL):
    

    """
    Generate a response from OpenAI's model based on specified user role, competencies, capabilities, and a given task.

    This function configures a message to OpenAI's API portraying a specific user role, its competencies, and capabilities,
    then asks a question related to a task in a specified language and tone. The response is influenced by additional instructions and temperature settings.

    Args:
        role (str): The role of the virtual assistant.
        competencies (str): Describes what the assistant is competent to handle.
        capabilities (str): Describes the functional capabilities of the assistant.
        task (str): A specific task or the type of questions the assistant is expected to handle.
        question (str): The actual question posed to the assistant.
        context (str): Additional context to help the assistant understand the scenario.
        lang (str): The language in which the assistant should respond.
        tone (str): The desired tone of the response (e.g., formal, friendly).
        temperature (float): Controls the randomness of the response. Higher values mean more random responses.
        extra_instructions (str, optional): Additional instructions to fine-tune the assistant's response.
        openai_api_key (str): The API key for OpenAI. Defaults to AGENTS_OPENAI_API_KEY.
        model (str, optional): The model used to generate the response. Defaults to AGENTS_MODEL.

    Returns:
        str: The response from the OpenAI model as a text string.

    Examples:
        >>> response = openai_answer(
                role="Technical Support",
                competencies="Software troubleshooting and customer support",
                capabilities="Answering technical queries, providing solutions",
                task="Assist users in resolving software issues",
                question="How do I fix a connection issue?",
                context="The user is experiencing intermittent connection.",
                lang="English",
                tone="professional",
                extra_instructions="Be concise and direct.",
                temperature=0.5
            )
        >>> print(response)
        "To fix a connection issue, you should first check if your internet service provider..."
    """
    
    # TODO: 
    # wrap in a back off function to handle OpenAIrate limits.
    # add context and question compression function to not exceed max allowed tokens 
    
    try:
        client=OpenAI(
                api_key = openai_api_key
            )
            
        if context:
            system_content = f"""
                ROLE: You are a {role}. 
                Your competencies are: {competencies}. 
                Your capabilities are: {capabilities}. 
                CONTEXT: {context}.
                TASK: {task}.
                INSTRUCTIONS:
                - Make your answer in a {tone} tone.
                {extra_instructions}"""
        else:
            system_content = f"""
                ROLE: You are a {role}. 
                Your competencies are: {competencies}. 
                Your capabilities are: {capabilities}. 
                TASK: {task}
                INSTRUCTIONS:
                - Make your answer in a {tone} tone.
                {extra_instructions}"""
        
        
        response = client.chat.completions.create(
            model = model,
            temperature = temperature,
            messages = [
                {"role": "system", "content": system_content},
                {"role": "user", "content": question}
            ]
        )
        if lang == 'same':
            return response.choices[0].message.content
        else:
            translated_response = client.chat.completions.create(
            model = model,
            temperature = temperature,
            messages = [
                {"role": "system", "content": f'You are a translator, translate the following into the {lang} language'},
                {"role": "user", "content": response.choices[0].message.content}
            ]
            )
            return translated_response.choices[0].message.content
            
    except Exception as err:
        return(f"Unexpected {err=}, {type(err)=}")