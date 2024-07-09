import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    
    ret = pd.DataFrame(student_data)
    ret.columns = ["student_id", "age"]
    
    return ret