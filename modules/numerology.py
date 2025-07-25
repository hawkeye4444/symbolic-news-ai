
from datetime import datetime

def reduce_number(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def analyze_date(date: datetime):
    total = sum([date.day, date.month, date.year % 100, date.year // 100])
    return {
        "raw_sum": total,
        "reduced": reduce_number(total)
    }

def compare_intervals(date1, date2):
    delta = abs((date1 - date2).days)
    return {"days_apart": delta, "reduced": reduce_number(delta)}
