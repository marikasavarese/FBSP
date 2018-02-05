import datetime
class DateService:
   
    def getCurrentDay(self):
        return datetime.datetime.now().day
   
    def getCurrentMonth(self):
        return datetime.datetime.now().month
   
    def getCurrentYear(self):
        return datetime.datetime.now().year
  
	
