

class LinearRegression:


 

   def __init__(self, batch_generator, C=1, alpha=0.01, max_epoch=10,
                 batch_size=100):
        """
        batch_generator -- функция генератор, которой будем создавать батчи
        C - коэф. регуляризации
        alpha - скорость спуска
        max_epoch - максимальное количество эпох
        """
 
    self.C = C
    self.alpha = alpha
    self.max_epoch = max_epoch
    self.batch_generator = batch_generator
    self.errors_log = {'iter': [], 'loss': []}
    self.batch_size = batch_size
 
   def calc_loss(self, X_batch, y_batch):
        """
        Считаем функцию потерь по батчу
        X_batch - матрица объекты-признаки по батчу
        y_batch - вектор ответов по батчу
        Не забудте тип модели (линейная или логистическая регрессия)!
        """
        m = X_batch.shape()[0]
        predict = X_batch.dot(self.weights)
        L2 = 1 / self.C * np.square(self.weights).sum()
        if self.model_type == "lin_reg":
            loss = np.square(np.subtract(y_batch, predict)).mean() + L2
        elif self.model_type == "log_reg":
            # L(w)=−1N[∑iyilogai+(1−yi)log(1−ai)]+1CR(w)
            loss = -(y_batch*np.log(sigmoid(predict)) + (1 - y_batch)
                     * np.log(1 - sigmoid(predict))).mean() + L2
        return loss
 
   def calc_loss_grad(self, X_batch, y_batch):
        """
        Считаем  градиент функции потерь по батчу (то что Вы вывели в задании 1)
        X_batch - матрица объекты-признаки по батчу
        y_batch - вектор ответов по батчу
        Не забудте тип модели (линейная или логистическая регрессия)!
        """
        m = X_batch.shape[0]
        predict = X_batch.dot(self.weights)
        L2 = 2 / self.C * (self.weights)
        if self.model_type == 'lin_reg':
            loss_grad = (2 * (predict - y_batch).dot(X_batch) / m) + L2
 
   elif self.model_type == 'log_reg':
        loss_grad = ((sigmoid(predict) - y_batch).dot(X_batch) / m) + L2
    return loss_grad
 
   def update_weights(self, new_grad):
        """
        Обновляем вектор весов
        new_grad - градиент по батчу
        """
 
   self.weights -= self.alpha * new_grad
 
   def fit(self, X, y):
        '''
        Обучение модели
        X - матрица объекты-признаки
        y - вектор ответов
        '''
        np.random.seed(2022)
        # Нужно инициализровать случайно весаw
        self.weights = np.random.normal(size= X.shape[1] + 1)
        for n in range(0, self.max_epoch):
            new_epoch_generator = self.batch_generator(X, y, batch_size= self.batch_size)
            for batch_num, new_batch in enumerate(new_epoch_generator):
                w0Vec = np.ones(new_batch[0].shape[0])[:, np.newaxis]
                X_batch = np.hstack((w0Vec, new_batch[0]))
                y_batch = new_batch[1]
                batch_grad = self.calc_loss_grad(X_batch, y_batch)
                self.update_weights(batch_grad)
                # Подумайте в каком месте стоит посчитать ошибку для отладки модели
                # До градиентного шага или после
                batch_loss = self.calc_loss(X_batch, y_batch)
                self.errors_log['iter'].append(batch_num)
                self.errors_log['loss'].append(batch_loss)
 
   return self
 
   def predict(self, X):
        '''
        Предсказание класса
        X - матрица объекты-признаки
        Не забудте тип модели (линейная или логистическая регрессия)!
        '''
 
   w0Vec = np.ones(X.shape[0])[:, np.newaxis]
    X = np.hstack((w0Vec, X))
 
   y_hat = X.dot(self.weights)
    if self.model_type == "log_reg":
        y_hat = sigmoid(y_hat)
    y_hat = np.round(y_hat)
    return y_hat
    # Желательно здесь использовать матричные операции между X и весами, например, numpy.dot
 
