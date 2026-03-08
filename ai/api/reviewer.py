import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


class Reviewer:

    def ask_llm(self, prompt):

        payload = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }

        r = requests.post(OLLAMA_URL, json=payload)

        return r.json()["response"]

    def review(self, code):

        prompt = f"""
        このコードに問題があるかレビューしてください。

        {code}

        問題がなければ OK とだけ答える
        """

        return self.ask_llm(prompt)