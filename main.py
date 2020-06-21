import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def normalize_data(data):

    return (data - np.min(data)) / (np.max(data) - np.min(data))

class Measurement:

    def __init__(self, x, y, threshold, total_deviation):

        self.x = x
        self.y = y 
        self.threshold = threshold
        self.total_deviation = total_deviation

class VisualFieldReader:

    def __init__(self):
        
        self.fieldpointspath = r"LongGlaucVF_20150216\VFPoints.csv"
        self.fieldpoints = pd.read_csv(self.fieldpointspath)
        self.parsecsv()

    def parsecsv(self):

        a = self.fieldpoints.groupby('FIELD_ID')[['X', 'Y', 'THRESHOLD', 'TOTAL_DEVIATION']].apply(lambda g: g.values.tolist()).to_dict()

        self.fields = []

        for key in a:

            vf = VisualField(key)

            for item in a[key]:

                m = Measurement(item[0], item[1], item[2], item[3])
                vf.add_measurement(m)

            self.fields.append(vf)

        for field in self.fields:

            field.plot()


class VisualField:

    def __init__(self, fieldid):

        self.fieldid = fieldid
        self.measurements = []
        #self.matrix = np.zeros(21, 21)

    def add_measurement(self, measurement):

        self.measurements.append(measurement)

    def plot(self):

        xValues = []
        yValues = []
        thresholds = []

        for measurement in self.measurements:

            xValues.append(measurement.x)
            yValues.append(measurement.y)
            thresholds.append(measurement.threshold)

        thresholds = normalize_data(thresholds)

        plt.scatter(xValues, yValues, c = thresholds, cmap = "Blues")
        

        plt.title(self.fieldid)
        plt.show()

a = VisualFieldReader()