import pandas as pd

def load_orders(path="data/orders.csv"):
    orders = pd.read_csv(path)
    orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce")
    return orders

def quality_report(df):
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": int(df.isna().sum().sum()),
    }

if __name__ == "__main__":
    orders = load_orders()
    print(quality_report(orders))
