import numpy as np


class N_network(object):
    def __init__(self):
        self.input_layer_size=2
        self.hidden_layer_size=4
        self.output_layer=1


        #weight

        self.w1=np.random.randn(self.input_layer_size,self.hidden_layer_size)
        self.w2=np.random.randn(self.hidden_layer_size,self.output_layer)

        #forward propagation

    def forward(self, X):
        self.z2 =np.dot(X,self.w1)
        self.a2 =self.sigmoid(self.z2)
        self.z3 =np.dot(self.a2,self.w2)
        y = self.sigmoid(self.z3)
        return y

        #activation function
    def sigmoid(self, z):
        return 1/(1+np.exp(-z))

r=N_network()
y=r.forward(X)
print(y)
