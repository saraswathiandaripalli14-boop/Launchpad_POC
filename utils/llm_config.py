from langchain_openai import ChatOpenAI

def get_llm():
    model = ChatOpenAI(
        model="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key="gUwe8hjt6y3ZGXy6zLxs36Xkf6OSv7lj4mL7WTNQ",
        base_url="https://openai.generative.engine.capgemini.com/v1",
    )
    return model