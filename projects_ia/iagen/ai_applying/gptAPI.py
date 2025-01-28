from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=200,
    temperature=0.4,
    messages=[
        {"role": "system", "content": "Você é um experiente programador. Retorne apenas códigos limpos e reutílizáveis"},
        {
            "role": "user",
            "content": "Escreva um hello world em python."
        }
    ]
)

print(completion.choices[0].message.content)