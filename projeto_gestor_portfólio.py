import json           
import os                                               
import json
from pyfiglet import figlet_format
import os
from colorama import Fore, Style, init

init(autoreset=True)
ARQUIVO_DADOS = 'fotografias.json'  

def carregar_fotografias():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, FileNotFoundError):
        print(Fore.RED + "Erro ao carregar os dados. O arquivo pode estar corrompido ou ausente.")
    return []
def salvar_fotografias(fotografias):
    try:
        with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
          json.dump(fotografias, arquivo, ensure_ascii=False, indent=4)
        print (Fore.GREEN + "Dados salvos com sucesso!")  
    except Exception as e:
        print (Fore.RED + f"Erro ao salvar os dados: {e}")  
        
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def buscar_foto(lista, nome):
    for foto in lista:
        if foto["nome"].lower() == nome.lower():
            return foto
    return None

def adicionar_fotos(lista):
    limpar_tela()

    try:
        quantidade = int(input("Quantas fotografias deseja adicionar: "))
        if quantidade <= 0:
            print(Fore.YELLOW + "Digite um número positivo.")
            input("ENTER para continuar...")
            return
    except ValueError:
        print(Fore.RED + "Digite um número inteiro válido.")
        input("ENTER para continuar...")
        return

    for i in range(quantidade):
        nome = input("\nNome da foto: ")

        while True:
            resp = input("Salvar como concluída? (S/N): ").strip().upper()

            if resp == "S":
                concluido = True
                break
            elif resp == "N":
                print(Fore.YELLOW + "Foto NÃO adicionada.")
                break
            else:
                print(Fore.YELLOW + "Digite apenas S ou N.")

        if resp == "N":
            continue

        foto = {
            "nome": nome,
            "concluido": True,
            "historico": []
        }

        lista.append(foto)
        print(Fore.GREEN + f"'{nome}' adicionada com sucesso!")

    salvar_fotografias(lista)
    input("\nENTER para continuar...")
    
def listar_fotos(lista):
    if not lista:
        print(Fore.YELLOW + "Lista vazia.")
    else:
        print(Fore.MAGENTA + "- - - LISTA DE FOTOGRAFIAS - - -")

        for foto in lista:
            status = "✅" if foto["concluido"] else "⏳"

            print(f"\n[{status}] Nome: {foto['nome']}")
            print(f"Concluído: {foto['concluido']}")

            if foto["historico"]:
                print("    Histórico de Alterações:", [h['nome'] for h in foto["historico"]])

    input("\nPressione ENTER para voltar ao menu...")
    limpar_tela()

def atualizar_foto(lista):
    if not lista:
        print("Lista vazia, adicione algo")
    else:
        nome = input("Digite o nome da foto que deseja atualizar: ")
        foto = buscar_foto(lista, nome)

        if foto is None:
            nome = input("Digite o nome da foto que deseja atualizar: ")
    foto = buscar_foto(lista, nome)
    if foto:
        versao_antiga = {"nome": foto["nome"], "concluido": foto["concluido"]}
        foto["historico"].append(versao_antiga)
        
        foto["nome"] = input("Novo nome: ")
        foto["concluido"] = input("Concluída? (S/N): ").upper()
        print(Fore.GREEN + "Atualizado!")
        salvar_fotografias(lista)
    else:
        print(Fore.RED + "Não encontrada.")
    input("\nPressione ENTER...")
input("\nPressione ENTER para voltar ao menu...")
os.system("cls" if os.name == "nt" else "clear")
    
def deletar_foto(lista):
   nome = input("Nome para deletar: ")
   foto = buscar_foto(lista, nome)
   if foto:
        lista.remove(foto)
        print(Fore.GREEN + "Removido!")
        salvar_fotografias(lista)
   else:
        print(Fore.RED + "Não encontrada.")
   input("\nPressione ENTER...")

def buscar_por_fotografias(lista):
    termo = input("Digite o termo de busca: ").lower()
    resultados = [f for f in lista if termo in f['nome'].lower()]
    
    limpar_tela()
    print(f"--- Resultados para '{termo}' ---")
    if not resultados:
        print("Nenhum projeto encontrado.")
    for r in resultados:
        print(f"- {r['nome']} (Status: {r['concluido']})")
    input("\nPressione ENTER...")

def resumir_portfolio(lista):
    total = len(lista)
    concluidos = sum(1 for f in lista if f['concluido'] == 'S')
    andamento = total - concluidos
    
    limpar_tela()
    print(Fore.CYAN + "=== RESUMO DO PORTFÓLIO ===")
    print(f"Total de Projetos: {total}")
    print(f"Concluídos: {concluidos}")
    print(f"Em andamento: {andamento}")
    if total > 0:
        print(f"Taxa de conclusão: {(concluidos/total)*100:.1f}%")
    input("\nPressione ENTER...")

def sobre():
    os.system("cls" if os.name == "nt" else "clear")

    BORDA    = Fore.MAGENTA + Style.BRIGHT
    TITULO   = Fore.MAGENTA + Style.BRIGHT
    DESTAQUE = Fore.CYAN    + Style.BRIGHT
    TEXTO    = Fore.WHITE
    SETA     = Fore.MAGENTA + Style.BRIGHT
    BRILHO   = Fore.YELLOW  + Style.BRIGHT
    
    titulo_pixel: str = figlet_format("JHEIMILY", font="small")

    print()
    print(BORDA + "  ════════════════════════════════════════════════════════════════")
    print()
    print(TITULO +    titulo_pixel + "📸   JHEIMILY  PHOTOGRAPHY  —  PORTFOLIO   📸")  
    print()
    print(BORDA + "  ════════════════════════════════════════════════════════════════")
    print()
    print(TEXTO + "    Por trás de cada clique, uma história. Por trás de cada")
    print(TEXTO + "    história, a " + DESTAQUE + "Jheimily" + TEXTO + " — fotógrafa apaixonada por eternizar")
    print(TEXTO + "    momentos que merecem ser lembrados para sempre.")
    print()
    print(TEXTO + "    Seu olhar é guiado pelas cores quentes, pelo aconchego e")
    print(TEXTO + "    pela emoção que pulsa em cada imagem. Da luz dourada do")
    print(TEXTO + "    fim de tarde ao brilho discreto de um sorriso espontaneo,")
    print(TEXTO + "    cada foto carrega um pedacinho de alma.")
    print()
    print(TEXTO + "    Com sensibilidade aos detalhes e uma abordagem criativa,")
    print(TEXTO + "    ela transforma cada sessao em uma experiencia unica.")
    print()
    print(BORDA + "  ────────────────────────────────────────────────────────────────")
    print()
    print(TEXTO + "    Este programa nasceu para acompanhar essa jornada —")
    print(TEXTO + "    ajudando a organizar, registrar e revisitar cada projeto")
    print(TEXTO + "    fotografico, do primeiro clique a entrega final.")
    print()
    print(SETA + "       ➤  " + TEXTO + "Adicionar novos projetos ao portfolio")
    print(SETA + "       ➤  " + TEXTO + "Listar todas as fotografias com seu historico")
    print(SETA + "       ➤  " + TEXTO + "Atualizar nomes e status sem perder versoes antigas")
    print(SETA + "       ➤  " + TEXTO + "Excluir registros que nao fazem mais sentido")
    print()
    print(BORDA + "  ════════════════════════════════════════════════════════════════")
    print(BRILHO + "             ✨   " + TITULO + "Criado por Jheimily" + BRILHO + "   •   2026   ✨")
    print(BORDA + "  ════════════════════════════════════════════════════════════════")
    print()
    input("Pressione ENTER para voltar ao menu...")
    os.system("cls" if os.name == "nt" else "clear")


print("Bem Vindo ao Gestor de Portfolio")

lista = []

while True:
    print("\n===== MENU =====")
    print("1 - ABOUT")
    print("2 - ADD")
    print("3 - LIST")
    print("4 - UPDATE")
    print("5 - DELETE")
    print("6 - SEARCH")
    print("7 - STATS")
    print("8 - QUIT")
    print("================")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        sobre()

    elif opcao == "2":
        adicionar_fotos(lista)

    elif opcao == "3":
        listar_fotos(lista)

    elif opcao == "4":
        atualizar_foto(lista)

    elif opcao == "5":
        deletar_foto(lista)
        
    elif opcao == "6":
        buscar_por_fotografias(lista)

    elif opcao == "7":
        resumir_portfolio(lista)

    elif opcao == "8":
        print("Encerrando o programa...")
        break

    else:
        print("Opcao invalida")

    ARQUIVO_DADOS = 'fotografias.json'

    def recuperar_fotografias():
     if not os.path.exists(ARQUIVO_DADOS):
        return []
     with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

    def salvar_fotografias(fotografias):
     with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(fotografias, arquivo, ensure_ascii=False, indent=4)

    def incluir_fotografia(fotografia):
     fotografias = recuperar_fotografias()
     fotografias.append(fotografia)
     salvar_fotografias(fotografias)
    print("Fotografia cadastrada com sucesso!")

    def listar_fotografias():
     fotografias = recuperar_fotografias()
     if not fotografias:
        print("Nenhuma fotografia cadastrada.")
     else:
        print("- - - LISTA DE FOTOGRAFIAS - - -")
        for foto in fotografias:
            print(f"\nNome: {foto['nome']}")
            print(f"Concluido: {foto['concluido']}")
            if foto["historico"]:
                print("Historico de Alteracoes:")
                for i, versao in enumerate(foto["historico"]):
                    print(f"  VERSAO {i + 1}:")
                    print(f"      Nome: {versao['nome']}")
                    print(f"      Concluido: {versao['concluido']}")
            else:
                print("Historico: (sem alteracoes)")
        input("\nPressione ENTER para voltar ao menu...")

    def excluir_fotografia(nome):
     fotografias = recuperar_fotografias()
     fotografia_encontrada = False
     for foto in fotografias:
        if foto["nome"].lower() == nome.lower():
            fotografias.remove(foto)
            salvar_fotografias(fotografias)
            print(f"Fotografia '{nome}' removida com sucesso")
            fotografia_encontrada = True
            break
     if not fotografia_encontrada:
        print(f"Fotografia '{nome}' nao encontrada")