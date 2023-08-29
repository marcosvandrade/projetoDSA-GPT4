# Data Science Academy - www.datascienceacademy.com.br
# Projeto 3 - Construindo Chatbot Personalizado com GPT-4 e Linguagem Python

# Import
import openai

# Chave
openai.api_key = "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"

# Função para gerar texto a partir do modelo de linguagem
df gera_texto(texto):

# Obtém a resposta do modelo de linguagem
response = openai.Completion.create(

    # Modelo usado
    # Outros modelos estão disponíveis em https://platform.openai.com/account/rate-limits
    engine = "text-davinci-003",

    # Texto inicial da conversa com o chatbot
    prompt = texto,

    # Comprimento da resposta gerada pelo modelo
    max_tokens = 150,

    # Quantas conclusões gerar para cada prompt
    n =  5,

    # O texto retornado não conterá a sequência de parada
    stop = None,

    # Uma medida da aleatoriedade de um texto gerado pelo modelo. Seu valor está entre 0 e 1.
    # Valores próximos a 1 significam que a saída é mais aleatória, enquanto valores próximos a 0 significam que a saída é muito identificável
    temperature = 0.8,
)

return response.choices[0].text.strip()