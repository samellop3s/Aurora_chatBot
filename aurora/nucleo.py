#Núcleo do assistente Aurora - versão 0.1 (só a estrutura!!).
from classificador_intecao import ClassificadorIntecao
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
        self.classificador = ClassificadorIntecao()
        self.classificador.treinar()
    
    def responder(self, pergunta: str) -> str:
        intencao = self.classificador.prever(pergunta)
        respostas_padrao = {
            "saudacao": f"Olá! me chamo {self.nome}, Como posso ajudar você hoje?",
            "pergunta_tecnica": "Eu ainda não tenho capacidade de responder perguntas técnicas, mas estou aprendendo!",
            "despedida": "Até logo!"
        }
        reposta = respostas_padrao[intencao]
        self.historico.append(Interacao(pergunta=pergunta, resposta=reposta))
        return reposta
    
if __name__ == "__main__":
    aurora = Aurora()
    print(aurora.responder("Bom dia"))
    print(aurora.responder("O que é Deep Learning?"))
    print(aurora.responder("Tchau"))
    print(f"Total de interações registradas: {len(aurora.historico)}")