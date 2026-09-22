# 🌌 Aurora ChatBot

> Um projeto de chatbot desenvolvido em Python, criado com foco em arquitetura, organização de código e evolução gradual para um assistente inteligente.

## 📌 Sobre o projeto

**Aurora** é um chatbot desenvolvido em Python que está sendo construído de forma incremental.

Nesta primeira versão, o projeto concentra-se na criação do núcleo do assistente, responsável por receber perguntas, gerar respostas básicas e manter um histórico das interações realizadas.

A ideia é utilizar essa estrutura como base para futuras implementações de inteligência artificial, incluindo processamento de linguagem natural e **embeddings**.

## ⚙️ Atualmente

A versão atual conta com:

* 🧠 Classe principal `Aurora`
* 💬 Sistema básico de perguntas e respostas
* 📝 Registro do histórico de conversas
* 🕒 Data e hora de cada interação
* 🏗️ Estrutura preparada para futuras expansões
* 🧪 Estrutura inicial para testes automatizados

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

## 📂 Estrutura do projeto

```text
Aurora_chatBot/
│
├── aurora/
│   ├── __init__.py
│   └── nucleo.py
│
├── testes/
│   └── test_nucleo.py
│
├── .gitignore
├── requeriments.txt
└── README.MD
```

## 🚀 Como executar

Clone o repositório:

```bash
git clone https://github.com/samellop3s/Aurora_chatBot.git
```

Entre na pasta:

```bash
cd Aurora_chatBot
```

Execute o núcleo da Aurora:

```bash
python -m aurora.nucleo
```

## 💡 Exemplo

Atualmente, a Aurora consegue registrar uma interação e armazená-la em seu histórico:

```python
from aurora.nucleo import Aurora

aurora = Aurora()

resposta = aurora.responder("Quem é você?")

print(resposta)
print(len(aurora.historico))
```

## 🧠 Próximos passos

O projeto está sendo desenvolvido com uma abordagem incremental.

### Roadmap

* [x] Estrutura inicial do projeto
* [x] Criar núcleo da Aurora
* [x] Sistema de interação
* [x] Histórico de conversas
* [ ] Implementar testes automatizados
* [ ] Implementar embeddings
* [ ] Adicionar processamento de linguagem natural
* [ ] Criar sistema de contexto
* [ ] Implementar memória persistente
* [ ] Integrar modelo de IA
* [ ] Criar interface para interação com o usuário
* [ ] Containerização com Docker

## 🎯 Objetivo

O objetivo do projeto é construir uma arquitetura de chatbot evolutiva, começando pela implementação do núcleo e adicionando novas capacidades de inteligência artificial conforme o desenvolvimento avança.

O projeto também serve como laboratório prático para estudar **Python, arquitetura de software, testes, processamento de linguagem natural, embeddings e integração com modelos de IA**.

## 👨‍💻 Autor

Desenvolvido por **Samuel Ferreira Lopes**.

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/samellop3s)
