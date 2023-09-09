def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"Время: {hours:02}:{minutes:02}:{seconds:02}"
print(convert_seconds(323500))