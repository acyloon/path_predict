# coding:UTF-8
import chainer
import chainer.functions as F
import chainer.links as L

class Model(chainer.Chain):
    def __init__(self, i_size, h_size, o_size, train):
        self.train = train
        super(Model, self).__init__(
            i_h=L.Linear(i_size, h_size),
            h_h=L.LSTM(h_size, h_size),
            h_o=L.Linear(h_size, o_size),
        )

    def forward(self, x, t=None, train=False):
        h = self.i_h(x)
        v = self.h_h(h)
        y = self.h_o(v)

        if self.train == True:
            loss = F.mean_squared_error(y, t)
            return loss
        elif self.train == False:
            return y

    def reset_state(self):
        self.h_h.reset_state()