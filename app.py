class llm:
    def __init__(self,  name, model,api):
        self.name = name
        self.model = model
        self.api= api

llm1=llm("Gemini","gemini-pro","aasdasdasdasdsadsadsadasdasdsadasdsa")
print(llm1.name)