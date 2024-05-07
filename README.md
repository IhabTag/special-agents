# special-agents

An Open-source Library for pre-defined LLM-powered specialized agents.

<!-- TOC start -->

* [Description](#description)
* [Installation](#installation)
* [Usage Example](#usage-example)
* [Features](#features)
* [Usage](#usage)
    + [Using a Special Agent](#using-a-special-agent)
    + [Available Special Agents](#available-special-agents)
        - [ProductManager](#productmanager)
        - [FullStackDeveloper](#fullstackdeveloper)
        - [ContentCreator](#contentcreator)
* [Contributing](#contributing)
* [License](#license)
* [Support](#support)
* [About Me](#about-me)

<!-- TOC end -->

---

## Description

The `special-agents` library offers a suite of pre-defined, LLM-powered specialized agents designed to streamline specific tasks for developers. This Python library provides easy-to-integrate, out-of-the-box solutions for tasks such as content creation, data analysis, and automated responses, using large language models.

---

## Installation

To install `special-agents`, simply use pip:

`pip install special-agents` 

---

## Usage Example

Here is how you can use the `ContentCreator` agent from our library:
```python
from special_agents.agents.ContentCreator import ContentCreator

creator = ContentCreator(openai_api_key='<your-openai-api-key>')

product = """
Tactful.AI CUSTOMER ENGAGEMENT PLATFORM
Connect with your customers on one platfor
Omni Engage is a powerful omnichannel communications software designed to help you create meaningful and personalized interactions with your customers.
Connect with your audience across many channels, including email, social media, and voice and deliver a consistent and memorable experience for every customer.
"""
answer = creator.write_linkedin_post(product)
print(answer)
```

This produces the following response

> 🌟 Exciting News! 🌟
> 
> Are you looking to revolutionize your customer engagement strategy?
> Look no further! 🚀
> 
> Introducing Tactful.AI's Omni Engage - the ultimate omnichannel
> communications software that will take your customer interactions to
> the next level! 🌐✨
> 
> With Omni Engage, you can seamlessly connect with your audience across
> multiple channels such as email, social media, and voice, ensuring a
> consistent and personalized experience for every customer. 📧💬📞
> 
> But that's not all! By leveraging our platform, you can drive traffic
> to your digital channels using SEO best practices, monitor engagement
> metrics, and reach new audiences with ease. 📈💡
> 
> Join the ranks of successful businesses who have transformed their
> customer engagement with Tactful.AI's Omni Engage. 💼💥
> 
> Ready to elevate your brand and create unforgettable customer
> experiences? Let's connect and explore the endless possibilities
> together! 🤝✨
> 
> **#CustomerEngagement #OmniChannel #TactfulAI #DigitalTransformation #EngageWithPurpose**
> 
> Remember, the key to success lies in engaging and interacting with
> your audience - so don't hesitate to like, share, and comment to
> spread the word! 🌟 Let's make this post go viral together! 🚀💬

---

## Features

-   **Content Creator**: Generates engaging content for various social media platforms and blogs.
-   **Product Manager**: Writing user stories and release notes.
-   **Fullstack Software Engineer**: Writing docstrings and inline comments for code.

**More agents will be available as the library grows.**

---

## Usage

### Using a Special Agent

**1. Set the following as env variables:**
- `OPENAI_API_KEY`: str : the API key provided by OpenAI.
- `AGENTS_MODEL` : str : default='gpt-3.5-turbo'  : the target OpenAI ChatCompletion model.
- `AGENTS_MODEL_TEMP`: float :  between 0 and 2 : default=0 : controls the randomness of the model response.

**2. Importing a sepcial agent:**

You can import one of the special agents available in this [list](#available-special-agents) (e.g. ProductManager
	
`from  special_agents.agents.ProductManager  import  ProductManager`
	
**3. Instantiate the special agent object:**

`product_manager = ProductManager()`

**"If the** **`OPENAI_API_KEY`** **env variable is not set, you must instantiate the special agent with the** - **`openai_api_key`** **parameter, otherwise it will through an error."**

**`product_manager = ProductManager(openai_api_key=<your-openai-api-key>)`**

**Optional Params:**
- `tone`: str : describe the required agent's tone of speech (e.g. friendly, professional, funny).
- `lang`: str : define the agent's required response language (e.g English, Egyptian Arabic).
- `extra_instructions`: str : any extra instructions to the agent (e.g avoid insults, be precise).
	
**4. Call the desired method from the special agent object passing the appropriate method params:**
`answer = product_manager.write_user_story(context='<some-context>')`


### Available Special Agents

#### ProductManager
- **Importing:** 
`from  special_agents.agents.ProductManager  import  ProductManager`
- **Methods:**
	- `ProductManager.write_user_story(context)`
		**Params**:
			- `context`: the context from which the user story will be written with it's acceptance criteria.
			
	- `ProductManager.write_release_notes(context)`
		**Params**:
			- `context`: the context from which the release notes will be written.


#### FullStackDeveloper
- **Importing:** 
`from  special_agents.agents.FullStackDeveloper import  FullStackDeveloper`
- **Methods:**
	- `FullStackDeveloper.write_code_documentation(context)`
		**Params**:
			- `context`: the context from which the code documentation will ne written in google style alongside the inline comments.

#### ContentCreator
- **Importing:** 
`from  special_agents.agents.ContentCreatorimport  ContentCreator`
- **Methods:**
	- `ContentCreator.write_linkedin_post(context)`
		**Params**:
			- `context`: the context from which the LinkedIn post will be created tuned for engagment and best practices.
			
	- `ContentCreator.write_facebook_post(context)`
		**Params**:
			- `context`: the context from which the Facebook post will be created tuned for engagment and best practices.
	
	- `ContentCreator.write_blog_article(context)`
		**Params**:
			- `context`: the context from which the blog article will be created tuned for SEO best practices and keywords.

**All the special agents are having another method** `general_answer`**:**

`Agent.general_answer(question, context)`

**Params**:
- `question`: the general question to be asked for the special agent.
- `context`: optional :the context to be considered by the agent when answering the question.

---

## Contributing

We welcome contributions from the community. Here are some ways you can contribute:

-   Reporting bugs
-   Suggesting enhancements
-   Pull requests

Please read [CONTRIBUTING.md](https://github.com/IhabTag/special-agents/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/IhabTag/special-agents/blob/master/LICENSE) file for details.

## Support

If you have any questions or need help integrating `special-agents` into your project, please open an issue here on GitHub.

## About Me

I'm [Ihab Tag](https://www.ihabtag.com/), a product manager who is passionate about AI and improving software development practices through effective tools like `special-agents`.