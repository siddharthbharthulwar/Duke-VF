import pandas as pd

class Measurement:

    def __init__(self, x, y, threshold, total_deviation):

        self.x = x
        self.y = y 
        self.threshold = threshold
        self.total_deviation = total_deviation

class VisualFieldReader:

    def __init__(self):
        
        self.fieldpointspath = r"D:\Documents\School\2020-21\GlaucomaNet\RotterdamVisualFields\LongGlaucVF_20150216\VFPoints.csv"
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


class VisualField:

    def __init__(self, fieldid):

        self.fieldid = fieldid
        self.measurements = []

    def add_measurement(self, measurement):

        self.measurements.append(measurement)


a = VisualFieldReader()