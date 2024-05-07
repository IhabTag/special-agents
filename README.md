
# special-agents

An Open-source Library for pre-defined LLM-powered specialized agents.

## Description

The `special-agents` library offers a suite of pre-defined, LLM-powered specialized agents designed to streamline specific tasks for developers. This Python library provides easy-to-integrate, out-of-the-box solutions for tasks such as content creation, data analysis, and automated responses, using large language models.

## Installation

To install `special-agents`, simply use pip:

`pip install special-agents` 

## Usage

Here is how you can use the `ContentCreator` agent from our library:

    from special_agents.agents.ContentCreator import ContentCreator
    
    creator = ContentCreator(openai_api_key='your-openai-api-key')
    product = """
    Tactful.AI CUSTOMER ENGAGEMENT PLATFORM
    Connect with your customers on one platform
    Omni Engage is a powerful omnichannel communications software designed to help you create meaningful and personalized interactions with your customers.
    Connect with your audience across many channels, including email, social media, and voice and deliver a consistent and memorable experience for every customer.
    """
    
    answer = creator.write_linkedin_post(product)
    print(answer)

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
> #CustomerEngagement #OmniChannel #TactfulAI #DigitalTransformation #EngageWithPurpose
> 
> Remember, the key to success lies in engaging and interacting with
> your audience - so don't hesitate to like, share, and comment to
> spread the word! 🌟 Let's make this post go viral together! 🚀💬

## Features

-   **Content Creator**: Generates engaging content for various social media platforms and blogs.
-   **Product Manager**: Writing user stories and release notes.
-   **Fullstack Software Engineer**: Writing docstrings and inline comments for code.

More agents will be available as the library grows.

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

**The detailed API documentation. (in progress)**


## About Me

I'm [Ihab Tag](https://www.ihabtag.com/), a product manager who is passionate about AI and improving software development practices through effective tools like `special-agents`.