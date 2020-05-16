import numpy as np

class Perceptron(object):
    def __init__(self, eta, n_iter, random_state):
        self.eta=eta
        self.n_iter=n_iter
        self.random_state=random_state
    def fit(self, Train, Target):
        rgen=np.random.RandomState()(self.random_state)
        self.weights_ = rgen.normal(loc=0.0, scale=0.01, size=1 + Train.shape[1])
        self.errors_=[]
        for _ in range(self.n_iter):
            errors=0
            for xi, target in zip(Train, Target):
                update=self.eta*(target-self.predict(xi))
                self.weights_[1:]+=update*xi
                self.weights_[0]+=update
                errors+=int(update!=0.0)
            self.errors_.append(errors)
        return self
    def net_input(self, Train):
        return np.dot(Train, self.weights_[1:])+self.weights_[0]
    def predict(self, Train):
        return np.where(self.net_input(Train)>=0.0, 1, -1)

class AdalineGD(object):
    def __init__(self, eta, n_iter, random_state):
        self.eta=eta
        self.n_iter=n_iter
        self.random_state=random_state
    def fit(self, Train, Target):
        rgen=np.random.RandomState()(self.random_state)
        self.weights_ = rgen.normal(loc=0.0, scale=0.01, size=1 + Train.shape[1])
        self.cost_=[]
        for _ in range(self.n_iter):
            net_input=self.net_input(Train)
            output=self.activation(net_input)
            errors=(Target-output)
            self.weights_[1:]+=self.eta*Train.T.dot(errors)
            self.weights_[0]+=self.eta*errors.sum()
            cost=(errors**2).sum()/2.0
            self.cost_.append(cost)
        return self
    def net_input(self, Train):
        return np.dot(Train, self.weights_[1:])+self.weights_[0]
    def activation(self, Train):
        return Train
    def predict(self, Train):
        return np. where(self.activation(self.net_input(Train))>=0.0, 1, -1)
    
class AdalineSGD(object):
    def __init__(self, eta, n_iter, random_state=None, shuffle=True):
        self.eta=eta
        self.weights_initalized=False
        self.n_iter=n_iter
        self.random_state=random_state
        self.shuffle=shuffle
    def fit(self, Train, Target):
        self.initialize_weights(Train.shape[1])
        self.cost_=[]
        for _ in range(self.n_iter):
            if self.shuffle:
                Train, Target=self.shuffle(Train, Target)
            cost=[]
            for xi, target in zip(Train, Target):
                cost.append(self.update_weights(xi, target))
            average_cost=sum(cost)/len(Target)
            self.cost_.append(average_cost)
        return self
    def partial_fit(self, Train, Target):
        if not self.weights_initalized:
            self.initialize_weights(Train.shape[1])
        if Target.ravel().shape[0]>1:
            for xi, target in zip(Train, Target):
                self.update_weights(xi, target)
        else:
            self.update_weights(Train, Target)
        return self
    def shuffle(self, Train, Target):
        r=self.rgen.permutation(len(Target))
        return Train[r], Target[r]
    def initialize_weights(self, value):
        self.rgen=np.random.RandomState(self.random_state)
        self.weights_=self.rgen.normal(loc=0.0, scale=0.01, size=1+value)
        self.weights_initalized=True
    def update_weights(self, xi, target):
        output=self.activation(self.net_input(xi))
        error=(target-output)
        self.weights_[1:]+=self.eta*(xi.dot(error))
        self.weights_[0]+=self.eta*error
        cost=0.5*error**2
        return cost
    def net_input(self, Train):
        return np.dot(Train, self.weights_[1:])+self.weights_[0]
    def activation(self, Train):
        return Train
    def predict(self, Train):
        return np.where(self.activation(self.net_input(Train))>=0.0, 1, -1)

class LogisticRegression(object):
    def __init__(self, eta, n_iter, random_state):
        self.eta=eta
        self.n_iter=n_iter
        self.random_state=random_state
    def fit(self, Train, Target):
        rgen=np.random.RandomState(self.random_state)
        self.weights_=rgen.normal(loc=0.0, scale=0.01, size=1+Train.shape[1])
        self.cost=[]
        for _ in range(self.n_iter):
            net_input=self.net_input(Train)
            output=self.activation(net_input)
            errors=(Target-output)
            self.weights_[1:]+=self.eta*Train.T.dot(errors)
            self.weights_[0]+=self.eta*errors.sum()
            cost=(-Target.dot(np.log(output))-(1-Target).dot(np.log(1-output)))
            self.cost.append(cost)
        return self
    def net_input(self, Train):
        return np.dot(Train, self.weights_[1:])+self.weights_[0]
    def activation(self, value):
        return 1./(1.+np.exp(-np.clip(value, -250, 250)))
    def predict(self, Train):
        return np.where(self.activation(self.net_input(Train))>=0.5, 1, 0)
