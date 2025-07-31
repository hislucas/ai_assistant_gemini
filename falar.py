# Lucas Ferreira Simoes
# 2 de jul de 2025
# Arquivo falar com microfone

import os
from gtts import gTTS
from playsound import playsound
import multiprocessing


def executar_fala(texto):
    """
    Recebe um texto, gera um áudio com gTTS e o reproduz com mpg123.
    """
    if not texto:
        return
    try:
        tts = gTTS(text=texto, lang='pt-br')
        arquivo_audio = "resposta_assistente.mp3"
        tts.save(arquivo_audio)
        print(f"Assistente: {texto}")
        playsound(arquivo_audio, block=False)
        os.remove(arquivo_audio)
    except Exception as e:
        print(f"Ocorreu um erro na função de fala: {e}")
