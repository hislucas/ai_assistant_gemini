# Lucas Ferreira Simoes
# 2 de jul de 2025
# Arquivo ouvir TTS

import speech_recognition as sr

def ouvir_comando():
    """
    Ouve o microfone uma vez e retorna a frase transrita em minúsculas.
    """

    r = sr.Recognizer()


    # --- CONFIGURAÇÃO DO RECONHECEDOR ---

    # 1. Nível de Energia para Detecção
    # Este é o limiar de volume. Valores mais altos ignoram mais ruídos de fundo,
    # mas podem fazer com que falas mais baixas não sejam detectadas.
    # O padrão é 300. Um bom valor para começar a testar é entre 500 e 4000.
    # r.energy_threshold = 1000

    # 2. Sensibilidade à Pausa
    # Define quanto tempo de silêncio (em segundos) é necessário para considerar
    # que uma frase terminou. O padrão é 0.8. Se você faz pausas longas
    # enquanto fala, pode aumentar este valor para 1.5 ou 2.0.
    r.pause_threshold = 1.5

    # 3. Ajuste Dinâmico de Energia (Opcional)
    # Por padrão, é True. A função adjust_for_ambient_noise usa isso.
    # Se você quiser confiar APENAS no seu energy_threshold manual, pode definir como False.
    r.dynamic_energy_threshold = True

    # ----------------------------------------


    with sr.Microphone() as source:
        print("Ouvindo...")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=15)
            print("Processando...")
            frase = r.recognize_google(audio, language='pt-BR')
            print(f"Usuário: {frase}")
            return frase.lower()
        except sr.WaitTimeoutError:
            return "" # Retorna vazio se não ouvir nada
        except Exception:
            return "ERRO AO ESCUTAR O MICROFONE" # Retorna vazio em caso de outros erros
