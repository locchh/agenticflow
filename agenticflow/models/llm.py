"""LLM integration for AgenticFlow framework."""

from typing import Dict, Any, List, Optional
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


class LLMProvider:
    """Provider for LLM integration."""
    
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gpt-3.5-turbo-instruct"):
        """Initialize the LLM provider."""
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set it via the api_key parameter or OPENAI_API_KEY environment variable.")
        
        self.model_name = model_name
        self.llm = OpenAI(openai_api_key=self.api_key, model_name=model_name)
    
    def create_chain(self, prompt_template: str, output_key: str = "result") -> LLMChain:
        """Create an LLM chain with the given prompt template."""
        prompt = PromptTemplate(
            input_variables=self._extract_variables(prompt_template),
            template=prompt_template
        )
        return LLMChain(llm=self.llm, prompt=prompt, output_key=output_key)
    
    def _extract_variables(self, template: str) -> List[str]:
        """Extract variables from a prompt template."""
        import re
        # Find all occurrences of {variable_name}
        matches = re.findall(r'\{([^}]+)\}', template)
        return matches
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate a response from the LLM."""
        return self.llm(prompt)
    
    def generate_with_template(self, template: str, **kwargs) -> str:
        """Generate a response using a template and variables."""
        chain = self.create_chain(template)
        result = chain.run(**kwargs)
        return result
