import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')


class Support_vector_machine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.color = {1:'r', -1:'b'}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)

    def fit(self, data):
        self.data = data
        opt_dict = {}

        transform = [[1,1],
                     [-1,1],
                     [-1,-1],
                     [1,-1]]
        
        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)

        all_data = None

        step_sizes = [self.max_feature_value * 0.1,
                      self.max_feature_value * 0.01,
                      self.max_feature_value * 0.001]

        b_range_multiple = 5
        b_multiple = 5
        latest_optimum = self.max_feature_value * 10
    def predict(self,features):
        classification = np.sign(np.dot(np.array(features),self.w)+self.b)
        return classification