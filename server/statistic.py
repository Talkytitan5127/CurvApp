from datetime import datetime

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_monday(today):
    monday = today.day - today.weekday()
    month = today.month
    if monday < 1:
        monday += months[(month-1)-1]
        month -= 1
    return datetime(
        year=today.year,
        month=month,
        day=monday
    )


def get_sunday(today):
    sunday = today.day + (7 - today.isoweekday())
    month = today.month
    if sunday > months[month - 1]:
        sunday -= months[(month + 1) % 12]
        month += 1
    return datetime(
        year=today.year,
        month=month,
        day=sunday
    )


def get_week_period(today):
    if not today:
        today = datetime.now()


