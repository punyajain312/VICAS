from _ai import nlp
import datetime
import re


def date_obj(day, month, year):
    day = int(re.findall(r"\d\d|\d", day)[0])
    year = int(year)
    
    month = month.lower()  
    if 'jan' in month:
        m = 1
    elif 'feb' in month:
        m = 2
    elif 'mar' in month:
        m = 3
    elif 'apr' in month:
        m = 4
    elif 'may' in month:
        m = 5
    elif 'jun' in month:
        m = 6
    elif 'jul' in month:
        m = 7
    elif 'aug' in month:
        m = 8
    elif 'sep' in month:
        m = 9
    elif 'oct' in month:
        m = 10
    elif 'nov' in month:
        m = 11
    elif 'dec' in month:
        m = 12
    else:
        return 'invalid month'
    
    try:
        return datetime.date(year, m, day)
    except ValueError:
        return datetime.date.today()

def date(doc):
    dates = []
    for ent in doc.ents:
        if ent.label_ == "DATE":
            date_parts = ent.text.split()
            if len(date_parts) == 3:
                day, month, year = date_parts
                date_obj_val = date_obj(day, month, year)
                dates.append(date_obj_val)
    if not dates:
        dates.append(datetime.date.today())      
    
    return dates



def time(doc):
    times = []
    for ent in doc.ents:
       if ent.label_ == "TIME":
           times.append(ent.text)
    return times

   
def dateTime(text):
    dateTime_info = []
    doc = nlp(text)
    dateTime_info.append(date(doc))
    dateTime_info.append(time(doc))

    return dateTime_info