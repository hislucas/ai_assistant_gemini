# Lucas Ferreira Simoes
# 2 de jul de 2025
# Arquivo IA no projeto jarvis

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from gerenciador_logs import abrir_log

def configurar():
    """
    Carrega e configura a chave da API do Gemini a partir do arquivo .env
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Chave da API não encontrada. Verifique o arquivo .env")
        return None
    
    client = genai.Client(api_key=api_key)
    return client

def fazer_pergunta(cliente, prompt):
    
    conteudo_dos_logs = abrir_log()
    """
    Envia o prompt para a API do Gemini e retorna a resposta.
    """
    if not cliente:
        return "Cliente da API não foi inicializado."
    
    configuracao_geracao = types.GenerateContentConfig(
        # Instrução de sistema - lê as logs para memória
        system_instruction=str(f'Você está em um laboratório, portanto seja objetivo e responda com poucas palavras, mas pode aumentar se considerar necessário. Fale apenas um texto corrido, exclarecendo como resolver à questão do usuário, e sempre considere a memória [{conteudo_dos_logs}] em suas respostas.'),
        # Controla a aleatoriedade. Valores baixos (ex: 0.2) = respostas mais diretas e factuais.
        # Valores altos (ex: 0.9) = respostas mais criativas e diversas.
        temperature=0.7,
        # Limita o tamanho máximo da resposta em tokens (aprox. 4 caracteres por token).
        max_output_tokens=300,
        # Outros parâmetros que você pode experimentar:
        # stop_sequences = [], # (lista de palavras ou caracteres que, se gerados, fazem a resposta parar imediatamente))
        # top_p=0.95, 
        # top_k=40
    )

    try:
        response = cliente.models.generate_content(
            model='gemini-2.5-flash-lite-preview-06-17', # https://ai.google.dev/gemini-api/docs/models?hl=pt-br
            contents=prompt,
            config=configuracao_geracao

        )
        return response.text
    except Exception as e:
        return f"Erro ao contatar a API do Gemini: {e}"
