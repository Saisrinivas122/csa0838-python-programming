month = input("enter the month(e.g. january,february etc.):")
day = int(input("enter the day:"))
if month in ('january','february','march'):
    season = 'winter'
elif month in ('april','may','june'):
    season = 'summer'
elif month in ('july','august','september'):
    season = 'summer'
else:
    season = 'autumn'
if (month == 'march')and (day>19 ):
    season = 'spring'
elif (month == 'june') and (day> 20):
    season  = 'summer'
elif (month == 'september') and(day> 21):
    season = 'autumn'
elif (month == 'december') and (day> 20):
    season = 'winter'
print("season is",season)