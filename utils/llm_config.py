from langchain_openai import ChatOpenAI
#connect to external genAI model LLM APIs
def get_llm():
    #creates the LLM object
    model = ChatOpenAI(
         
        #model is Claude Sonnet model (via Capgemini endpoint)
        model="us.anthropic.claude-sonnet-4-5-20250929-v1:0",  
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        #this connects you to the LLM service
        api_key="gUwe8hjt6y3ZGXy6zLxs36Xkf6OSv7lj4mL7WTNQ",
        #the model is hosted / capgemini genai platform
        #your API requests are sent to access the LLM servic
        base_url="https://openai.generative.engine.capgemini.com/v1",
    )
    return model 