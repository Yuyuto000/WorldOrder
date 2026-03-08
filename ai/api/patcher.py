import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


class Patcher:

    def ask_llm(self, prompt):

        payload = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }

        r = requests.post(OLLAMA_URL, json=payload)

        return r.json()["response"]

    def generate_patch(self, file_path, code, error):

        prompt = f"""
        このPythonコードのバグを修正してください。

        Error:
        {error}

        Code:
        {code}

        修正後のコードのみ出力
        """

        return self.ask_llm(prompt)