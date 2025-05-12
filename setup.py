"""Setup script for AgenticFlow package."""

from setuptools import setup, find_packages

setup(
    name="agenticflow",
    version="0.1.0",
    description="Strategic AI Agent Framework",
    author="AgenticFlow Team",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "openai",
        "networkx",
        "matplotlib",
        "pydantic",
        "requests",
    ],
    python_requires=">=3.8",
)
