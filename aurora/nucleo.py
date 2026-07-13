#Núcleo do assistente Aurora - versão 0.1 (só a estrutura!!).

from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Interacao:
    """Representa uma troca única entre usuário e Aurora"""
    pergunta: str
    resposta: str
    quando: datetime = field(default_factory=datetime.now)

class Aurora: 
    """Classe principal do assistente. Ira apenas ecoar a pergunta"""
    def __init__(self, nome: str = "Aurora"):
        self.nome = nome
        self.historico: list[Interacao] = []
    
    def responder(self, pergunta: str) -> str:
        #Como é a primeira versão ainda não tera IA. com a implementação do embeddings vai ter essa alteração
        resposta = f"Você peruntou: '{pergunta}'. Ainda não consigo te responder com total certeza, me faça essa pergunta novamente mais tarde!."
        self.historico.append(Interacao(pergunta=pergunta, resposta=resposta))
        return resposta
    
if __name__ == "__main__":
    aurora = Aurora()
    print(aurora.responder("Quem é você? "))
    print(f"Total de interações registradas: {len(aurora.historico)}")