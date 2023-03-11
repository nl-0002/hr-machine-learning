import pandas as pd
import numpy as np


def preprocess(data):
    data = data.dict()
    enrollee_id = data['enrollee_id']
    data = pd.DataFrame([data]).drop(columns='enrollee_id')
    data = data.apply(lambda row: row.fillna(np.nan),axis=1)
    return enrollee_id, data

def postprocess(enrollee_id, data):
    response_dict = {0: "stay in", 1: "leave"}
    response = f'Enrollee Id: {enrollee_id} is likely to {response_dict[data[0]]} the company'
    return response
