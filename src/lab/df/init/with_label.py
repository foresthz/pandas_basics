'''
Created on 2017-11-23

@author: jack
'''

import numpy as np
import pandas as pd

arr = np.random.randn(6,6)
dates = pd.date_range('2017-11-1', periods=6)
df = pd.DataFrame(arr, index=dates, columns=['A', 'B', 'C', 'D', 'E', 'F'])

print 'get two columns: '
print df[['A', 'D']]
