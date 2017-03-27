import glob
for name in glob.glob('C:/Users/IT solution/Desktop/*txt'):
    file=open(name,'r+')
     
def report1(): 
    f=open(name,'r+')
    print("Year           MAX Temp         MIN Temp        MAX Humidity           MIN Humidity")
    print("------------------------------------------------------------------------------------")
    for line,data in enumerate(f):
        data=data.strip().upper()
        x=data.split(',')
        if((data.find('\n') and len(data)==0)):
            print(' ')
        else:
            if (line!=1):
                if(line!=33):
                    print x[0],"\t",x[1],"\t\t",x[3],"\t\t\t",x[7],"\t\t\t",x[9]
            
                
    f.close()


def report2(name):
    f=open(name,'r+')
    
    print("Year        Date          Temp")
    print("------------------------------")
    for line,data in enumerate(f):
        data=data.strip().upper()
        d=data.split(',')
        if((data.find('\n') and len(data)==0)):
            print(' ')
        print(d[0])
        year=d[0].split('-')
        print year[0]#,"\t\t".d[3],"\t\t",max (d[1])
    f.close()


def weatherman(a):
    
    if (a==1):
        report1(name)
    elif(a==2):
        report2(name)
    else:
        print("[-] Usage: weatherman [report#] [data_dir]\n[Report #]\n 1 for Annual Max/Min Temperatur\n 2 for Hottest day of each year\n[data_dir]\n Directory containing weather data files")


def main():
    print("\t\t welcome to weatherman :")
    print("[!] press 1 for annual report or 2 for hottest day")
    print("[!] enter file name")
    
    e=int(input("enter the num:"))
    s=input("Enter the file name:")
    weatherman(e,name)


if __name__== "__main__": main()
