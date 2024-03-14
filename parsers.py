import base64
import io
import numpy as np
import pandas as pd

'''
Parsers should return a list of dicts, each of format:
    {'df': <dataframe>, 'height': <height>}
'''
def generic_csv_parser(content):
    content_type, content_string = content.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    return [{'df': df, 'height': 1}]

def ohlc_parser(content):
    content_type, content_string = content.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    #set datetime as index
    df['dtime'] = pd.to_datetime(df['dtime'])
    df.set_index('dtime', inplace=True)
    
    df1 = df[['open', 'high', 'low', 'close']]
    df2 = df[['volume']]
    return [{'df': df1, 'height': 3}, {'df': df2, 'height': 1}]