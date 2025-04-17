import pandas as pd
import numpy as np


employee =  pd.DataFrame({
    "id": [1,2,3,4],
    "name": ["Joe", "Henry", "Sam","Max"],
    "salary": [70_000,80_000,60_000,90_000],
    "managerId": [3, 4, "null", "null"]
 })
result =  pd.DataFrame({
    "class": ["Math"]
})


inputs = [
(employee)
]
outputs = [
result
]
