import json
import os
import random
import string

import hashlib

MASTER = "data/master.json"

def criar_master():
    senha = input("Crie sua senha mestra: ").strip()
    confirmacao = input("Confirme a senha mestra: ").strip()
    if senha != confirmacao:
        print("As senhas nao coincidem!")
        return criar_master()
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    with open(MASTER, "w") as f:
        json.dump({"hash": hash_senha}, f)
    print("Senha mestra criada com sucesso!")

def verificar_master():
    with open(MASTER) as f:
        salvo = json.load(f)["hash"]
    for tentativa in range(3):
        senha = input("Digite sua senha mestra: ").strip()
        if hashlib.sha256(senha.encode()).hexdigest() == salvo:
            return True
        print(f"Senha incorreta! {2 - tentativa} tentativa(s) restante(s).")
    return False

ARQUIVO = "data/vault.json"

def carregar_senhas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_senhas(senhas):
    with open(ARQUIVO, "w") as f:
        json.dump(senhas, f, indent=2, ensure_ascii=False)

def gerar_senha(tamanho=16):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    return "".join(random.choice(caracteres) for _ in range(tamanho))

def menu():
    while True:
        print("╔══════════════════════════════╗")
        print("║  🔐 VAULT - Gerenciador      ║")
        print("╚══════════════════════════════╝")
        print()
        print("[1] Cadastrar nova senha")
        print("[2] Listar senhas salvas")
        print("[3] Buscar senha")
        print("[4] Gerar senha forte")
        print("[5] Excluir senha")
        print("[0] Sair")
        print()

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            servico = input("Servico (ex: Gmail): ").strip()
            usuario = input("Usuario ou email: ").strip()
            senha   = input("Senha (Enter para gerar automaticamente): ").strip()
            if not senha:
                senha = gerar_senha()
                print(f"Senha gerada: {senha}")
            senhas = carregar_senhas()
            senhas.append({
                "servico": servico,
                "usuario": usuario,
                "senha":   senha
            })
            salvar_senhas(senhas)
            print("Senha salva com sucesso!")

        elif opcao == "2":
            senhas = carregar_senhas()
            if not senhas:
                print("Nenhuma senha cadastrada ainda.")
            else:
                print()
                for i, entrada in enumerate(senhas, 1):
                    print(f"[{i}] {entrada['servico']} | {entrada['usuario']}")

        elif opcao == "3":
            termo = input("Nome do servico: ").strip().lower()
            senhas = carregar_senhas()
            encontrados = [s for s in senhas if termo in s["servico"].lower()]
            if not encontrados:
                print("Nenhum resultado encontrado.")
            else:
                for entrada in encontrados:
                    print()
                    print(f"Servico : {entrada['servico']}")
                    print(f"Usuario : {entrada['usuario']}")
                    print(f"Senha   : {entrada['senha']}")

        elif opcao == "4":
            tamanho = input("Tamanho da senha (Enter para 16): ").strip()
            tamanho = int(tamanho) if tamanho.isdigit() else 16
            for i in range(5):
                print(f"[{i+1}] {gerar_senha(tamanho)}")

        elif opcao == "5":
            termo = input("Nome do servico a excluir: ").strip().lower()
            senhas = carregar_senhas()
            encontrados = [s for s in senhas if termo in s["servico"].lower()]
            if not encontrados:
                print("Nenhum resultado encontrado.")
            else:
                for i, entrada in enumerate(encontrados, 1):
                    print(f"[{i}] {entrada['servico']} | {entrada['usuario']}")
                escolha = input("Qual deseja excluir? (numero): ").strip()
                if escolha.isdigit() and 1 <= int(escolha) <= len(encontrados):
                    senhas.remove(encontrados[int(escolha) - 1])
                    salvar_senhas(senhas)
                    print("Registro excluido!")
                else:
                    print("Opcao invalida.")

        elif opcao == "0":
            print("Ate logo!")
            break
        else:
            print("Opcao invalida!")

        input("\nPressione Enter para continuar...")

if not os.path.exists(MASTER):
    criar_master()

if verificar_master():
    print("Acesso concedido!")
    menu()
else:
    print("Acesso negado. Encerrando.")