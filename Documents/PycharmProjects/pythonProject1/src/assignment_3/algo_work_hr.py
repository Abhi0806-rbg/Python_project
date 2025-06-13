#Write an algorithm to find the work hours of the given day.
def get_work_hours(day):
    timetable = {
        "Mon": [3, 2, 2],
        "Tue": [3, 2, 2],
        "Wed": [3, 2, 2],
        "Thu": [3, 2, 1],
        "Fri": [3, 2, 1],
        "Sat": [3, 1, 0],
        "Sun": [0, 0, 0]
    }

    return timetable.get(day, [])


if __name__ == "__main__":
    day = input("Enter the day: ")
    work_hours = get_work_hours(day)
    print(f"Work hours on {day}: {work_hours}")