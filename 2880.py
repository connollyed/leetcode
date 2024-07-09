import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    
    ret = students.loc[students["student_id"] == 101, ["name","age"]]
    return ret