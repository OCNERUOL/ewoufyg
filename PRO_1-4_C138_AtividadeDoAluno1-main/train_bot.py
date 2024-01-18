import json  # para trabalhar com arquivos JSON
import random  # para selecionar respostas aleatorias

with open('intents.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
intents = dados['intents']
def obter_respostas(input_usuario):
    input_usuario = input_usuario.lower()
    resposta = "desculpe nao consegui entender voce."  # resposta
    # Percorre todas as intencoes definidas no arquivo JSON
    for intent in intents:
        patterns = intent['patterns']
        responses = intents['responses']
        for pattern in patterns:
            if pattern.lower() in input_usuario:
                resposta = random.choice(responses)
                break
        if resposta != "desculapa nao entendi nada":
            break
    return resposta
while True:
    imput_usuario = input("Voce: ")
    if imput_usuario.lower() == "sair":
        print("Chat bot: ate mais")
        break
    resposta_bot = obter_respostas(imput_usuario)
    print("Chat bot:", resposta_bot)

