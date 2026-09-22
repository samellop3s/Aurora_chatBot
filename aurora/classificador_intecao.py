from sklearn.feature_extraction.text import CountVectorizer;
from sklearn.neural_network import MLPClassifier

#estamos indicando ao sistema a criação de uma "caixa" inteligente que vai receber as frases
class ClassificadorIntecao:
    def __init__(self):
        self.vetorizador = CountVectorizer()
        self.modelo = MLPClassifier(
            hidden_layer_sizes=(16,),
            max_iter=3000, 
            random_state=42,
        )
        pass #estamos indicando que por enquanto nao existe informações para serem trabalhadas