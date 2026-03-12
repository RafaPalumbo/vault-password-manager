# 🔐 VAULT — Gerenciador de Senhas

> *Gerencie suas senhas com segurança, direto pelo terminal.*

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-SHA--256-red?style=for-the-badge&logo=shield&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-JSON-yellow?style=for-the-badge&logo=json&logoColor=black)
![License](https://img.shields.io/badge/LICENSE-MIT-brightgreen?style=for-the-badge)

---

## ✨ Funcionalidades

- 🔑 **Senha mestra** — acesso protegido com hash SHA-256
- ➕ **Cadastrar senhas** — salva serviço, usuário e senha
- 📋 **Listar serviços** — visualize tudo que está salvo
- 🔍 **Buscar credenciais** — encontre qualquer serviço pelo nome
- ⚡ **Gerar senha forte** — letras, números e símbolos aleatórios
- 🗑️ **Excluir registro** — remove entradas com confirmação
- 💾 **Armazenamento local em JSON** — seus dados ficam no seu computador

---

## 🚀 Como usar

### Pré-requisitos

- Python 3.8 ou superior

### Instalação

```bash
# Clone o repositório
git clone https://github.com/RafaPalumbo/vault-password-manager.git

# Entre na pasta
cd vault-password-manager

# Execute o programa
python3 manager.py
```

### Primeira execução

Na primeira vez, o VAULT pede para criar uma **senha mestra**. Essa senha protege todo o cofre — guarde bem!

---

## 🎮 Menu do programa

```
╔══════════════════════════════╗
║  🔐 VAULT - Gerenciador      ║
╚══════════════════════════════╝

[1] Cadastrar nova senha
[2] Listar senhas salvas
[3] Buscar senha
[4] Gerar senha forte
[5] Excluir senha
[0] Sair
```

---

## 🛠️ Tecnologias

| Recurso | Uso |
|--------|-----|
| `hashlib` | Hash SHA-256 da senha mestra |
| `random` + `string` | Geração de senhas fortes |
| `json` | Armazenamento local dos dados |
| `os` | Manipulação de arquivos e pastas |

Feito com **Python puro** — zero dependências externas.

---

## 📁 Estrutura do Projeto

```
vault-password-manager/
├── manager.py        # Código principal
├── .gitignore        # Ignora a pasta data/
└── data/             # Criada automaticamente (não vai ao GitHub)
    ├── vault.json    # Senhas salvas
    └── master.json   # Hash da senha mestra
```

> ⚠️ A pasta `data/` é criada automaticamente e está no `.gitignore` — suas senhas **nunca** vão para o GitHub.

---

## 🔒 Segurança

- Senha mestra armazenada como **hash SHA-256** — nunca em texto puro
- Dados salvos **100% localmente** no seu computador
- Limite de **3 tentativas** para digitar a senha mestra

---

## 🗺️ Próximas melhorias

- [ ] Migrar de JSON para SQLite
- [ ] Criptografar o vault.json com Fernet
- [ ] Interface gráfica com Tkinter
- [ ] Exportar senhas para CSV

---

## 👨‍💻 Autor

Feito por **Rafael Palumbo**

[![GitHub](https://img.shields.io/badge/GitHub-RafaPalumbo-181717?style=flat&logo=github)](https://github.com/RafaPalumbo)
[![Instagram](https://img.shields.io/badge/Instagram-rafapalumbo-E4405F?style=flat&logo=instagram)](https://www.instagram.com/rafapalumbo)
