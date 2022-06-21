import tensorflow.compat.v1 as tf
import pandas as pd
import os
import sys
from icecream import ic
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import basedir

# year : 년, avg_temp : 평균, min_temp : 최소, max_temp : 최대, rain_fall : 강수량?, avgprice : 평균가격
class Solution:
    def __init__(self):
        self.model = os.path.join(basedir, 'model')

    def cabbage(self, avg_temp, min_temp, max_temp, rain_fall):
        ic(f'훅에 전달된 avg_temp : {avg_temp}, min_temp : {min_temp}, '
        f'max_temp : {max_temp}, rain_fall : {rain_fall}')

        return [avg_temp, min_temp, max_temp, rain_fall]
    def csv(self, file):
        return pd.read_csv(f'{file}.csv', encoding='UTF-8', thousands=',')

    def preprocessing(self):
        file = self.csv('./data/price_data')

    def create_model(self):
        sess = tf.Session()
        _ = tf.Variable(initial_value = 'fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.save(sess, os.path.join(self.model, 'cabbage', 'model'), global_step=1000)
    def fit(self):
        pass

    def eval(self):
        pass



if __name__=='__main__':
    tf.disable_v2_behavior()
    s = Solution()
    s.preprocessing()
    s.create_model()
