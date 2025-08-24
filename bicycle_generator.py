import json
import os
from itertools import product
from typing import Dict, List
import pandas as pd

def generate_bicycle_json(file_path: str) -> str:
    
    abs_path = os.path.abspath(file_path)
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"File not found: {abs_path}")

    xls = pd.ExcelFile(abs_path)

    # ID sheet
    id_df = pd.read_excel(xls, 'ID', header=None)
    designators: List[str] = id_df.iloc[0].tolist()
    designator_values: Dict[str, List[str]] = {}
    for i, des in enumerate(designators):
        values = id_df.iloc[1:, i].dropna().astype(str).unique().tolist()
        if not values:
            raise ValueError(f"No values for designator '{des}'")
        designator_values[des] = sorted(values)  

    # GENERAL sheet
    general_df = pd.read_excel(xls, 'GENERAL', header=None)
    general_fields: Dict[str, str] = dict(zip(general_df.iloc[0], general_df.iloc[1].astype(str)))

    # lookup sheets ('1' to '6')
    lookups: Dict[str, Dict[str, Dict[str, str]]] = {}
    for i in range(1, len(designators)):
        sheet = str(i)
        if sheet not in xls.sheet_names:
            raise ValueError(f"Missing lookup sheet '{sheet}'")
        df = pd.read_excel(xls, sheet, header=None)
        key_col = df.iloc[0, 0]
        lookups[sheet] = {}
        for _, row in df.iloc[1:].iterrows():
            key = str(row[0])
            fields = dict(zip(df.iloc[0, 1:], row[1:].astype(str)))
            lookups[sheet][key] = fields

    # Generate combinations 
    value_lists = [designator_values[des] for des in designators]
    bicycles: List[Dict[str, str]] = []
    for comb in product(*value_lists):  
        bike_id = ''.join(comb)
        bike: Dict[str, str] = {"ID": bike_id}
        bike.update(general_fields)

        for j, des in enumerate(designators[1:], 1):
            sheet = str(j)
            key = comb[j]
            if key in lookups[sheet]:
                fields = lookups[sheet][key]
                for k, v in fields.items():
                    lower_v = v.lower()
                    if lower_v in {'true', '1', 'yes'}:
                        bike[k] = 'TRUE'
                    elif lower_v in {'false', '0', 'no'}:
                        bike[k] = 'FALSE'
                    else:
                        bike[k] = v
            else:
                print(f"Warning: No lookup for {des}='{key}' in sheet {sheet}")

        bicycles.append(bike)

    
    bicycles.sort(key=lambda b: b['ID'])

    
    return json.dumps(bicycles, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    try:
        file_path = r"C:\Nidhieee\projects\BicycleGenerator\Bicycle.xlsx"  
        json_str = generate_bicycle_json(file_path)
        with open('bicycles.json', 'w', encoding='utf-8') as f:
            f.write(json_str)
        print("Generated bicycles.json (5508 entries)")
    except Exception as e:
        print(f"Error: {e}")