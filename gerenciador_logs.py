# Lucas Ferreira Simoes
# 2 de jul de 2025
# Arquivo de criar logs do projeto jarvis

import datetime
 
LOG_FILE = "logs.txt"

def registrar_log(identificador, mensagem):
    """
    Registra uma mensagem formatada no arquivo de log.
    Ex: registrar_log("SolicitacaoDoUsuario", "que horas são?")
    """
    # Gera o timestamp no formato especificado nos args
    
    
    # Remove quebras de linha da mensagem para um log limpo
    mensagem_limpa = mensagem.strip()
    
    try:
        # Abre o arquivo em modo 'append' (a), para adicionar ao final
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            #timestamp = datetime.datetime.now().strftime("data [%d %m %y] time [%H %M %S]")
            #f.write(f"{timestamp} | {identificador}: {mensagem_limpa}\n") - para caso queira colocar a data e hora da interação
            f.write(f"{identificador}: {mensagem_limpa}\n")
    except Exception as e:
        print(f"ERRO ao escrever no log: {e}")

def abrir_log():
    """
    Abre o arquivo de log e retorna seu conteúdo.
    """
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Arquivo de log não encontrado."
    except Exception as e:
        return f"Erro ao abrir o log: {e}"
