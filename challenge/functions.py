def cell_null(data):
    return data.isnull().sum()/data.shape[0] * 100