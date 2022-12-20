from TensorS import *

class LinearRegression:


    def __init__(self, alpha=0.1, max_epoch=10):
        """
        batch_generator -- функция генератор, которой будем создавать батчи
        alpha - скорость спуска
        max_epoch - максимальное количество эпох
        """
        self.alpha = alpha
        self.max_epoch = max_epoch
        self.errors_log = {'iter': [], 'loss': []}


    def calc_loss(self, X_batch, y_batch):
        """
        Считаем функцию потерь по батчу
        X_batch - матрица объекты-признаки по батчу
        y_batch - вектор ответов по батчу
        """
        predict = X_batch.dot(self.w.T())
        loss = (y_batch - X_batch).squared().mean()
        return loss
    
    
    def calc_loss_grad(self, X_batch, y_batch):
        """
        Считаем  градиент функции потерь по батчу (то что Вы вывели в задании 1)
        X_batch - матрица объекты-признаки по батчу
        y_batch - вектор ответов по батчу
        Не забудте тип модели (линейная или логистическая регрессия)!
        """
        
        predict = X_batch.dot(self.w)
        loss = TensorList(calc_grad((predict - y_batch).item(), X_batch)) * self.alpha
        return loss
    def update_weights(self, new_grad):
        """
        Обновляем вектор весов
        new_grad - градиент по батчу
        """
        self.w = self.w -  new_grad



    def fit(self, X, y):
        self.w = TensorList([0.1, 0.1])
        for _ in range(self.max_epoch):
            for idx in range(len(X)):
                x_batch = TensorList(X[idx])
                y_batch = TensorList(y[idx])
                gradient = self.calc_loss_grad(x_batch, y_batch)
                self.update_weights(gradient)


    def predict(self, X):
        return X.dot(self.w)

if __name__ == "__main__":
    LinModel = LinearRegression(max_epoch=10)
    y = Tensor([[6], [12]])
    X = Tensor([[1, 2], [2,4]])
    LinModel.fit(X,y)
    print(LinModel.predict(TensorList([2,4])))