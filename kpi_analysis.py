import pandas as pd

def on_time_delivery_rate(shipments):
    return shipments["status"].eq("On Time").mean() * 100

def average_delivery_lead_time_hours(shipments):
    dispatch = pd.to_datetime(shipments["dispatch_time"], errors="coerce")
    delivery = pd.to_datetime(shipments["delivery_time"], errors="coerce")
    return (delivery - dispatch).dt.total_seconds().mean() / 3600

if __name__ == "__main__":
    shipments = pd.read_csv("data/shipments.csv")
    print("On-time delivery rate:", on_time_delivery_rate(shipments))
    print("Average lead time (hours):", average_delivery_lead_time_hours(shipments))
