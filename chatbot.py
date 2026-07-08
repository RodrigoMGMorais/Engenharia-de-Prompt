from openai import OpenAI

# 1. Configurar o cliente para apontar para o Ollama local (Grátis)
# Se quisesse usar OpenAI real, bastaria remover o base_url e colocar a api_key
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" # chave fictícia exigida pela biblioteca
)

# 2. Definir o System Prompt (Regras de Ouro do Bot)
system_prompt = """
Você é um Engenheiro de Suporte Técnico Nível 3 pragmático e direto.
Sua missão é ajudar analistas de sistemas a diagnosticar erros de infraestrutura, SQL e redes.
Responda de forma objetiva, técnica e sempre em Português do Brasil.
"""

# 3. Inicializar a lista de histórico da conversa
historico_conversa = [
    {"role": "system", "content": system_prompt}
]

def enviar_mensagem(mensagem_usuario):
    # Passo A: Adiciona a mensagem do usuário ao histórico
    historico_conversa.append({"role": "user", "content": mensagem_usuario})
    
    # Passo B: Envia todo o histórico para a LLM
    response = client.chat.completions.create(
        model="llama3.2",  # Nome do modelo no Ollama
        messages=historico_conversa,
        temperature=0.2    # Baixa aleatoriedade para respostas técnicas precisas
    )
    
    # Passo C: Extrai a resposta gerada pela IA
    resposta_ia = response.choices[0].message.content
    
    # Passo D: Guarda a resposta da IA no histórico para manter a memória!
    historico_conversa.append({"role": "assistant", "content": resposta_ia})
    
    return resposta_ia

# 4. Loop de Execução no Terminal (Interface de Chat)
print("=== ASSISTENTE TÉCNICO INICIADO (Digite 'sair' para encerrar) ===\n")

while True:
    pergunta = input("\nVocê: ")
    if pergunta.lower() in ['sair', 'exit']:
        print("Encerrando sessão...")
        break
        
    resposta = enviar_mensagem(pergunta)
    print(f"\nAssistente IA:\n{resposta}")
