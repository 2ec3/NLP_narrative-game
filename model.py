from transformers import AutoModelForCausalLM, AutoTokenizer

class Model:
    def __init__(self, model_name: str = "Qwen/Qwen2.5-1.5B-Instruct", messages = [], max_content = 21):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

        self.messages = messages
        self.user_content = ""
        self.assistant_content = ""
        self.max_content = max_content

    def init_history(self, system_content):
        self.messages = [
            {
                "role": "system",
                "content": system_content
            }
        ]

    def add_content(self, role, content):
        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )
        while (len(self.messages) > self.max_content):
            self.messages.pop(1)

    def generate(self, max_new_tokens = 256, do_sample = True, temperature = 1, top_k = 30, top_p = 0.8):
        text = self.tokenizer.apply_chat_template(
            self.messages,
            tokenize=False,
            add_generation_prompt=True
        )
        inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        generated_ids = self.model.generate(
            **inputs,
            max_new_tokens = max_new_tokens,
            do_sample = do_sample, 
            temperature = temperature, 
            top_k = top_k, 
            top_p = top_p
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, generated_ids)
        ]

        self.assistant_content = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

        self.add_content("assistant", self.assistant_content)

    def run_cli(self):
        self.user_content = input("\nUser:\n")
        while self.user_content != ("EXIT"):
            self.add_content("user", self.user_content)
            
            self.generate()
            
            print("\nAssistant:\n", self.assistant_content)

            self.user_content = input("\nUser:\n")

if __name__ == "__main__":
    model = Model()
    model.init_history("Tu es le Game Master d'un jeu narratif.")
    model.run_cli()
