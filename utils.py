"""
scripts for handling time
"""

def to_seconds(time_str: str) -> int:
    # A:BB:CC,DDD -> A*3600+BB*60+CC.DDD
    if time_str.count(":") == 2:
        hour_str, minute_str, second_str = time_str.split(":")
    elif time_str.count(":") == 1:
        minute_str, second_str = time_str.split(":")
        hour_str = "0"

    if "," in second_str:
        second_str = second_str.replace(",", ".")
    return int(hour_str) * 3600 + int(minute_str) * 60 + int(float(second_str)+0.5)


def to_time_str(time_value: int) -> str:
    hour = int(time_value // 3600)
    minute = int(time_value % 3600 // 60)
    second = time_value % 60
    return f"{hour}:{minute:02}:{second:02}"