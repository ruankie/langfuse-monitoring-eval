from langfuse.decorators import observe


class MockLLM:
    """Mock LLM that can be invoked."""

    def invoke(self, prompt: str):
        """Mock invocation that always returns the same response."""
        static_response = "In a forgotten library, a young girl opened a dusty book and discovered it was writing her life story as she lived it, each turn of the page revealing her next decision."
        return static_response


@observe()
def call_llm(prompt: str):
    llm = MockLLM()
    response: str = llm.invoke(prompt)
    return response


@observe()
def get_story():
    story = call_llm(prompt="Tell me a story")
    return story


if __name__ == "__main__":
    get_story()
