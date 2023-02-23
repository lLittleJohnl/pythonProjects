import numpy as np

"""
Classificador Perceptron -> class Perceptron:
 
Parâmetros:
eta: float        -Taxa de aprendizado (entre 0,0 e 1,0)
n_iter: int       -Passa o conjunto de dados de treinamento
random_state: int -Semente geradora de números aleatórios para peso aleatório inicialização
  
Atributos:
w_ : 1d-array     -Pesos após a montagem.
errors_ : list    -Número de erros de classificação (atualizações) em cada época.
"""
"""
Ajustar dados de treinamento -> def fit
 
Parâmetros:
X : {array-like}, shape = [n_samples, n_features] -Vetores de treinamento, onde n_samples é o número de amostras e n_features é o número de recursos
y : array-like, shape = [n_samples]               -Valores alvo

Retorno:
self : object
"""

class Perceptron:
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
        self.w_ = None
        self.errors_ = None

    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)