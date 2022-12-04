from datetime import datetime

from lib.Log import Log

def getDate(year, month, day):
    import datetime
    date = datetime.date(year, month, day)
    return date.strftime("%A")


class Offer:

    def __init__(self, offerResponseObject: object) -> None:
        self.id = offerResponseObject.get("offerId")
        self.expirationDate = datetime.fromtimestamp(offerResponseObject.get("expirationDate"))
        print("Received date:" ,str(offerResponseObject.get("expirationDate")))
        self.location = offerResponseObject.get('serviceAreaId')
        self.blockRate = float(offerResponseObject.get('rateInfo').get('priceAmount'))
        self.endTime = datetime.fromtimestamp(offerResponseObject.get('endTime'))
        self.startHour = self.expirationDate.hour
        self.endHour = self.endTime.hour


    
    def toString(self) -> str:
        blockDuration = (self.endTime - self.expirationDate).seconds / 3600
        self.day = str(getDate(self.expirationDate.year, self.expirationDate.month, self.expirationDate.day))

        body = 'Location: ' + self.location + '\n'
        body += 'Date: ' + str(self.expirationDate.month) + '/' + str(self.expirationDate.day) + '\n'
        body += 'Pay: ' + str(self.blockRate) + '\n'
        body += 'Block Duration: ' + str(blockDuration) + f'{"hour" if blockDuration == 1 else "hours"}\n'
        body += "Day of Week: " + self.day + "\n"
        body += "Offer ID: " + str(self.id) + "\n"
       

        if not self.expirationDate.minute:
            body += 'Start time: ' + str(self.startHour) + ':00\n'
        elif self.expirationDate.minute < 10:
            body += 'Start time: ' + str(self.startHour) + ':0' + str(self.expirationDate.minute) + '\n'
        else:
            body += 'Start time: ' + str(self.startHour) + ":" + str(self.expirationDate.minute) + '\n'

        if not self.endTime.minute:
            body += 'End time: ' + str(self.endHour) + ':00\n'
        elif self.endTime.minute < 10:
            body += 'End time: ' + str(self.endHour) + ':0' + str(self.endTime.minute) + '\n'
        else:
            body += 'End time: ' + str(self.endHour) + ":" + str(self.endTime.minute) + '\n'

        return body

    # function that turn a date into a weekday







    # def getDayOfWeek(self) -> str:
    #     return self.expirationDate.strftime("%A")

    #function that intakes month,day and year and returns the day of the week
