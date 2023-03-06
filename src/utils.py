import pandas as pd
import numpy as np


def preprocess(data):
    data = data.dict()
    data = pd.DataFrame([data])
    data = data.apply(lambda row: row.fillna(np.nan),axis=1)
    return data

def postprocess(data):
    response_dict = {0: "Likely to stay in company", 1: "Likely to leave the company"}
    return response_dict[data[0]]
