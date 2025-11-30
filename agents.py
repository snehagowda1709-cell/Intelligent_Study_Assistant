from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class StudyAgent:
    def __init__(self, api_key):
        self.notes = ""

        # ✔ Correct Gemini model for LangChain
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            google_api_key=api_key,
            temperature=0.4
        )

        template = """
        You are an intelligent study assistant.

        NOTES:
        {notes}

        QUESTION:
        {question}

        Provide a clear, short, and accurate answer based ONLY on the notes.
        """

        self.prompt = PromptTemplate(
            template=template,
            input_variables=["notes", "question"]
        )

        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt
        )

    def load_notes(self, text):
        self.notes = text

    def answer_question(self, query):
        return self.chain.run({
            "notes": self.notes,
            "question": query
        })
