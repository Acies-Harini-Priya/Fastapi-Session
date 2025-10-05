import pandas as pd

def dataFrameToJson(dataframe: pd.DataFrame, orient='records') -> dict:
    """
    orient must be in `['tight', 'records']`
    Output:
    data: dict
    """

    data = dataframe.to_dict(orient=orient)
    return data