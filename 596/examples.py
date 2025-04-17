import pandas as pd

courses =  pd.DataFrame({
    "student": list("ABCDEFGHI"),
    "class": ["English","English", "Math","Biology","Math","Computer","Math","Math","Math" ]
})
result =  pd.DataFrame({
    "class": ["Math"]
})


inputs = [
(courses)
]
outputs = [
result
]
