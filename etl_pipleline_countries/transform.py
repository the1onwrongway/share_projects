import logging

def transform(data):
    clean = []
    for d in data:
        try:
            row = [d["name"]["official"], d["region"], d["population"]]
            clean.append(row)
        except Exception as e:
            logging.error(f"Transform failed: {e}")
    return clean