class llm:
    def __init__(self,  name, model,api):
        self.name = name
        self.model = model
        self.api= api

llm1=llm("Gemini","gemini-pro","aasdasdasdasdsadsadsadasdasdsadasdsa")
print(f"We want a {llm1.name} llm model {llm1.model} for chat our own document its api is {llm1.api}")