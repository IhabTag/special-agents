from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r", encoding="utf-8") as f:
    req = f.readlines()
req = [x.strip() for x in req if x.strip()]

setup(
    name="special-agents", 
    version="1.0.9",
    author="Ihab Tag",
    author_email="contact@ihabtag.com",
    description="An Open-source Library for pre-defined LLM powered specialized agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IhabTag/special-agents",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages = ['special_agents', 'special_agents.agents'],
    python_requires='>=3.6',
    license='MIT license',
    install_requires=req
)