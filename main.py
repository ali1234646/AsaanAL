import openai

openai.api_key = "YOUR_API_KEY_HERE"

print("AsaanAI is ready!")

while True:
    question = input("Ask anything: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are AsaanAI, a friendly assistant."},
            {"role": "user", "content": question}
        ]
    )

    print("AsaanAI:", response['choices'][0]['message']['content'])
