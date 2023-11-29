# !pip install -q google-generativeai

import pprint
import google.generativeai as palm

palm.configure(api_key='add_your_palm_api_key_here')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
# print(model)

def chat_with_palm(prompt):
    response = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )
    return response.result


print("Welcome to PaLM Bot! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("PaLM Bot: Goodbye!")
        break

    response = chat_with_palm(user_input)
    print("PaLM Bot:", response)
