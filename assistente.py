# Lucas Ferreira Simoes
# 2 de jul de 2025
# Arquivo MAIN no projeto jarvis

# Importa as funções dos nossos módulos
import os
from ouvir import ouvir_comando
from falar import executar_fala
from ia import configurar, fazer_pergunta
from gerenciador_logs import registrar_log
from time import sleep
import webbrowser
from gerenciador_logs import abrir_log

#Processa o comando ouvido e decide qual ação tomar.
def processar_comando(cliente_ia, comando):
    
    conteudo_dos_logs = abrir_log() #para memória episódica
    
    if not comando:
        return True # Continua o laço se não ouviu nada
    

    pesquisa = comando
    if "pesquise" in comando or "pesquisa" in comando:

        if "pesquise por" in comando:
            pesquisa = comando.replace("pesquise por", "")

        elif "pesquisar por" in comando:
            pesquisa = comando.replace("pesquisar por", "")

        elif "pesquise pelo" in comando:
            pesquisa = comando.replace("pesquise pelo", "o")

        elif "pesquise pela" in comando:
            pesquisa = comando.replace("pesquise pela", "a")
        
        elif "faça uma pesquisa sobre" in comando:
            pesquisa = comando.replace("faça uma pesquisa sobre", "")

        elif "pesquise sobre" in comando:
            pesquisa = comando.replace("pesquise sobre", "")

        elif "pesquisa sobre" in comando:
            pesquisa = comando.replace("pesquisa sobre", "")            

        webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://www.google.com/search?q="+pesquisa, new=2)
        registrar_log("Sistema", str(f"Pesquisa no google por:{pesquisa}."))
    del pesquisa #isso exclui a variável do código, funcionando

    if "abra o " in comando or "abre o " in comando or "abrir o " in comando:
        site = fazer_pergunta(cliente_ia, comando + f". Sua resposta deve conter apenas o link direto do site (e.g., https://www.google.com/). Verifique se o link abre. Ele deve ser abrível e remeter ao conceito ou empresa associado a ele. E.g., o prompt 'abra o site do madero' deve retornar o site da empresa do madero, que é restaurantemadero.com.br/pt, e do detranMG que é https://transito.mg.gov.br/. Verifique em sua memória ({conteudo_dos_logs}) se não há informações sobre websites especificados.")
        webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(site, new=2)

    if "comando do sistema" in comando or "comando de sistema" in comando:
        
        if "desligar o computador" in comando:
            registrar_log("Usuario", "Desligando em 15 segundos")
            registrar_log("Sistema", "COMPUTADOR DESLIGANDO")
            executar_fala("O computador será desligado em 15 segundos!")
            os.system("shutdown /s /t 15")
            
            return True #volta o laço normalmente

        # Comando para encerrar o assistente
        if "encerrar" in comando:
            registrar_log("Usuario", "Encerrar assistente")
            registrar_log("Sistema", "ASSISTENTE ENCERRADO")
            executar_fala("Encerrando. Até logo!")
            sleep(1.2)
            return False # Sinaliza para sair do laço
        

    # Comando para interagir com a IA
    # Você pode definir uma palavra-chave para ativar o Gemini
    palavra_chave_ia = "gemini"
    if palavra_chave_ia in comando:
        prompt = comando.replace(palavra_chave_ia, "").strip()
        if prompt:
            registrar_log("Solicitação do Usuário", str(f"Gemini, {prompt}."))
            print("Processando a pergunta...")
            resposta = fazer_pergunta(cliente_ia, prompt)
            registrar_log("LLM Gemini", resposta)
            executar_fala(resposta)
        else:
            executar_fala("Por favor, diga o que quer perguntar ao Gemini.")
        
    #else:
        # Se não for um comando conhecido, avisa o usuário
        #executar_fala("Comando não reconhecido. Você pode pedir para 'encerrar assistente' ou chamar o 'gemini'.")
        #registrar_log("Usuário", comando)
        #registrar_log("Assistente", "Comando não reconhecido")
        
    
    return True # Continua o laço



# ---------------- execução ------------------

if __name__ == "__main__":

    # Configura a API do Gemini uma única vez no início
    cliente_gemini = configurar()
    
    if cliente_gemini:
        registrar_log("Sistema", "ASSISTENTE INICIADO\n")
        executar_fala("Assistente iniciado e conectado à IA.")
        
        continuar = True
        while continuar:
            comando_do_usuario = ouvir_comando()
            continuar = processar_comando(cliente_gemini, comando_do_usuario)
    else:
        print("Falha ao iniciar o assistente devido a erro na configuração da API.")