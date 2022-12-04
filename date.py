

def getDate(year, month, day):
    import datetime
    date = datetime.date(year, month, day)
    return date.strftime("%A")

def main():
    print(getDate(2022, 12, 5))

main()