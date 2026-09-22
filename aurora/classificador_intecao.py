from sklearn.feature_extraction.text import CountVectorizer;
from sklearn.neural_network import MLPClassifier
from falas import frases, rotulos

#estamos indicando ao sistema a criação de uma "caixa" inteligente que vai receber as frases
class ClassificadorIntecao:
    def __init__(self):
        self.vetorizador = CountVectorizer()
        self.modelo = MLPClassifier(
            hidden_layer_sizes=(16,),
            max_iter=3000, 
            random_state=42,
        )

        #aqui estamos criando um metodo de treino, ele vai treinar a caixa inteligente com as frases e rotulos
    def treinar(self):
        X = self.vetorizador.fit_transform(frases)
        self.modelo.fit(X, rotulos)
    
        #aqui estamos criando um metodo de previsão, ele vai prever a intenção do usuário
    def prever(self, frase):
        X_nova = self.vetorizador.transform([frase])
        return self.modelo.predict(X_nova)[0]

        