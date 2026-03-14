import json
import os


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


data_mobilecity = read_json("../data/raw/cellphones_data.json")
data_cellphones = read_json("../data/raw/mobilecity_data.json")

all_products = data_mobilecity + data_cellphones

print(f"Total products: {len(all_products)}")

os.makedirs("../data/raw", exist_ok=True)
with open("../data/raw/all_products.json", "w", encoding="utf-8") as f:
    json.dump(all_products, f, ensure_ascii=False, indent=4)
