import pandas as pd
import os

def test_case_save(title: str, url: str, content: str, filename: str = "request_cases.csv", folder: str = "../collected_cases") -> bool:
    try:
        os.makedirs(folder, exist_ok=True)
        path_to_save = os.path.join(folder, filename)
        print(path_to_save)
        df = pd.DataFrame([[title, url, content]], columns=['title', 'url', 'content'])
        
        if os.path.exists(path_to_save):
            df.to_csv(path_to_save, mode='a', header=False, index=False, encoding='utf-8-sig')
        else:
            df.to_csv(path_to_save, mode='w', index=False, encoding='utf-8-sig')
        
        return True
    except Exception:
        return False
