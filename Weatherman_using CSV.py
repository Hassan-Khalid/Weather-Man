# -*- coding: cp1252 -*-
# created by Hassan Khalid
# dated: 27-03-2017
import glob
import os
import csv

years_to_processed = ['1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011']
files = []
maximum_temperature = []
dates = []
monthly_max_temp = {}
yearly_max_temp = {}

def file_processing(file_name):
    
    minimum_temperature = []
    maximum_humidity = []
    minimum_humidity = []

    dates[:] = []
    maximum_temperature[:]=[]

    max_temp = 0
    min_temp = 0
    max_humidity = 0
    min_humidity = 0
 

    with open(file_name, 'r') as f:
        reader = csv.reader(f,delimiter=',')
        for line in f:
            if line != "\n" and line.find('<') < 0:
                tokenise_line = line.split(',')
                try:
                    maximum_temperature.append(int(tokenise_line[1]))
                    minimum_temperature.append(int(tokenise_line[3]))
                    maximum_humidity.append(int(tokenise_line[7]))
                    minimum_humidity.append(int(tokenise_line[9]))
                    dates.append(tokenise_line[0])                              
                except:
                    pass
    try:
        max_temp = max(maximum_temperature)
        min_temp = min(minimum_temperature)
        max_humidity = max(maximum_humidity)
        min_humidity = min(minimum_humidity)
            
    except:
        pass
    return max_temp, min_temp, max_humidity, min_humidity


def file_directory():
    os.chdir('D:/WeatherData/weatherdata')
    for filename in glob.glob('*.txt'):
        files.append(filename)

def processing(option=None):
    yearly_minimum_temperature = []
    yearly_maximum_temperature = []
    yearly_minimum_humidity = []
    yearly_maximum_humidity = []
        
    for year in years_to_processed:
        yearly_minimum_temperature[:]=[]
        yearly_maximum_temperature[:]=[]
        yearly_minimum_humidity[:]=[]
        yearly_maximum_humidity[:]=[]
        for f in files:
            if year in f:
                max_temp, min_temp, max_humidity, min_humidity = file_processing(f)
                yearly_minimum_temperature.append(min_temp)
                yearly_maximum_temperature.append(max_temp)
                yearly_minimum_humidity.append(min_humidity)
                yearly_maximum_humidity.append(max_humidity)

                try:
                    max_temp_index = maximum_temperature.index(max_temp)
                    monthly_max_temp[dates[max_temp_index]] = max_temp
                except:
                    pass
        yearly_max_temp_key=max(monthly_max_temp, key=monthly_max_temp.get)
        yearly_max_temp[yearly_max_temp_key]=monthly_max_temp[yearly_max_temp_key]
        if option is None:
            display( year, max(yearly_maximum_temperature), max(yearly_maximum_humidity),
                    min(yearly_minimum_humidity), min(yearly_minimum_temperature))
        monthly_max_temp.clear()

def display(year, max_temp, max_humidity, min_humidity, min_temp):
    print year,"\t\t", max_temp,"\t\t",min_temp,"\t\t",max_humidity,"\t\t",min_humidity,"\t\t"

def display_hottest_day():
    for date , Temp_C in yearly_max_temp.iteritems():
        year = date.split('-')
        print year[0] ,"\t", date, "\t", Temp_C,"\n"
    
def annual_report(option=None):
    file_directory()
    processing(option)
    
def hottest_day():
    print ("Year        Date          Temp")
    print ("------------------------------")   
    display_hottest_day()

def main():
    print("\t\bWellcome TO Weather Data System\b")
    print("Please Enter\n 1 For Annual Report \n 2 For Hottest Day of Year")
    index=int(input("Please enter the Index :"))
    if index==1:
       print("Year        MAX Temp        MIN Temp        MAX Humidity        MIN Humidity")
       print("----------------------------------------------------------------------------")
       annual_report()
    if index==2:
       annual_report(1)
       hottest_day()
       
    if(index!=1 and index != 2):
      print("\t\tWeatherMan Report Application")
      print("[Report]\n")
      print("1 : Annual Max/Min Tempeture\n2 : Hottest Day OF Each Year ")
     
if __name__=='__main__':
    main()
