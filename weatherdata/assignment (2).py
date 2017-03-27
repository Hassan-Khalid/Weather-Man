import os
month_max_temp=dict()
year_max_temp=dict()
month_min_temp=dict()
year_min_temp=dict()
month_max_h=dict()
year_max_h=dict()
month_min_h=dict()
year_min_h=dict()
year=0

def temp_of_year1(month_max_temp):
    max1=0
    temp_y=dict()
    
    for i in month_max_temp:
        
        if(max1==0):
            max1=month_max_temp[i]
            temp_y={i:month_max_temp[i]}
        else:
            
            if(max1<=month_max_temp[i]):
                max1=month_max_temp[i]
                temp_y={i:month_max_temp[i]}
    
    year_max_temp.update(temp_y)
    month_max_temp.clear()

def temp_of_year(month_max_temp,month_min_temp,month_max_h,month_min_h):
    max1=0
    temp_y=dict()
    
    for i in month_max_temp:
        
        if(max1==0):
            max1=month_max_temp[i]
            temp_y={i:month_max_temp[i]}
        else:
            
            if(max1<=month_max_temp[i]):
                max1=month_max_temp[i]
                temp_y={i:month_max_temp[i]}
    
    year_max_temp.update(temp_y)
    month_max_temp.clear()
      
    '''
        /*********************************
          loop for min temp of  a year
        ********************************/
        '''
    max1=0
    temp_y.clear()
    for i in month_min_temp:
        
        if(max1==0):
            max1=month_min_temp[i]
            temp_y={i:month_min_temp[i]}
        else:
            
            if(max1>=month_min_temp[i]):
                max1=month_min_temp[i]
                temp_y={i:month_min_temp[i]}
    year_min_temp.update(temp_y)
    month_min_temp.clear()
    '''
        /*********************************
          loop for max humidity of  a year
        ********************************/
        '''
    max1=0
    temp_y.clear()
    for i in month_max_h:
        
        
        if(max1==0):
            
            max1=month_max_h[i]
            temp_y={i:month_max_h[i]}
        else:
            
            
            if(max1<=month_max_h[i]):
                max1=month_max_h[i]
                temp_y={i:month_max_h[i]}
    year_max_h.update(temp_y)
    month_max_h.clear()
    
    '''
        /*********************************
          loop for min humidity of  a year
        ********************************/
        '''
    max1=0
    temp_y.clear()
    for i in month_min_h:
        
        if(max1==0):
            max1=month_min_h[i]
            temp_y={i:month_min_h[i]}
        else:
            
            if(max1>=month_min_h[i]):
                max1=month_min_h[i]
                temp_y={i:month_min_h[i]}
    year_min_h.update(temp_y)
    month_min_h.clear()



                
def temp_of_month1(ma):

    '''to check max temp in whole month'''

    max1=0
    temp_m=dict()


    
    
    '''
        /****************************************************
           for finding max temp of month and send it to dict
        *****************************************************/
        '''
    for i in ma:
        if(max1==0):
            max1=(ma[i])
            temp_m={i:max1}
        elif(max1<=(ma[i])):
            max1=(ma[i])
            temp_m={i:max1}
    month_max_temp.update(temp_m)
    

def temp_of_month(ma,mi,mah,mih):

    '''to check max temp in whole month'''

    max1=0
    temp_m=dict()


    
    
    '''
        /****************************************************
           for finding max temp of month and send it to dict
        *****************************************************/
        '''
    for i in ma:
        if(max1==0):
            max1=(ma[i])
            temp_m={i:max1}
        elif(max1<=(ma[i])):
            max1=(ma[i])
            temp_m={i:max1}
    month_max_temp.update(temp_m)
    
    '''
        /****************************************************
           for finding max humidity of month and send it to dict
        *****************************************************/
        '''
    temp_m.clear()
    max1=0
    for i in mah:
         if(max1==0):
             max1=(mah[i])
             temp_m={i:max1}
         elif(max1<=(mah[i])):
             max1=(mah[i])
             temp_m={i:max1}
    month_max_h.update(temp_m)
    
     
    
    '''
        /****************************************************
           for finding min temp of month and send it to dict
        *****************************************************/
        '''
    temp_m.clear()
    max1=0
    for i in mi:
        if(max1==0):
            max1=(mi[i])
            temp_m={i:max1}
        elif(max1>=(mi[i])):
            max1=(mi[i])
            temp_m={i:max1}
    month_min_temp.update(temp_m)


    '''
        /****************************************************
           for finding min humidity of month and send it to dict
        *****************************************************/
        '''
    temp_m.clear()
    max1=0
    for i in mih:
        if(max1==0):
            max1=(mih[i])
            temp_m={i:max1}
        elif(max1>=(mih[i])):
            max1=(mih[i])
            temp_m={i:max1}
    month_min_h.update(temp_m)

'''
/********************
 for display output
 ********************/
 '''
def retrive(s):
    from itertools import izip
    
    y_max_t=sorted(year_max_temp)
    y_min_t= sorted(year_min_temp)
    y_max_h= sorted(year_max_h)
    y_min_h= sorted(year_min_h)
    

    if (s==1):
        print("Year           MAX Temp        MIN Temp       MAX Humidity         MIN Humidity")
        print("-------------------------------------------------------------------------------")

        for i,j,k,l in izip(y_max_t,y_min_t,y_max_h,y_min_h):
            o=i.split('-')
            print o[0],'\t\t', year_max_temp[i]," \t\t",year_min_temp[j],'   \t\t', year_max_h[k],' \t\t\t', year_min_h[l]

            
    elif(s==2):
            
        print("Year              Date                  Temp")
        print("--------------------------------------------")
        for i in y_max_t:
            o=i.split('-')
            print o[0],'\t\t',i,"\t\t",year_max_temp[i]



def report1(s):
    
    d=os.listdir(s)
    global year
    for i in d :
        
      
        
        y=int(i.split('_')[2])
        if( year==0):
            year=y
        elif( year!=y ):
            
            temp_of_year(month_max_temp,month_min_temp,month_max_h,month_min_h)
            year=y
        
        ma=dict()# dict for max_temp in month
        
        mi=dict()#dict for min_temp in month
        
        mah=dict()#dict for max_humanity in month
        
        mih=dict()#dict for min_humanity in month
        
        r=open(s+"\\"+i,'r+')
        f=r.readlines()
        for line,data in enumerate(f):
            
            data=data.strip().upper()

            x=data.split(',')

            if (not(data.find('\n') and len(data)==0)):

               

                if(line!=1):#blank line or space

                    if(x[0][0]!='<'):# to check the last line

                        if (x[1]=="" or x[3]=="" or x[7]=="" or x[9]==""):

                            ma.update({x[0]:0})#if temp is not in recorde 
                            mi.update({x[0]:0})
                            mah.update({x[0]:0})
                            mih.update({x[0]:0})
                        else:
                            ya=int(x[1])
                            ma.update({x[0]:ya})
                            y1=int(x[3])
                            mi.update({x[0]:y1})
                            y2=int(x[7])
                            mah.update({x[0]:y2})
                            y3=int(x[9])
                            mih.update({x[0]:y3})
                            
         
                        #print x[0],"\t",x[1],"\t\t",x[3],"\t\t\t",x[7],"\t\t\t",x[9]

        r.close()

        temp_of_month(ma,mi,mah,mih)

        if(i=="lahore_weather_2011_May.txt"):
            temp_of_year(month_max_temp,month_min_temp,month_max_h,month_min_h)
  
    retrive(1)

def report2(s):
    d=os.listdir(s)
    global year
    for i in d :
        
      
        
        y=int(i.split('_')[2])
        if( year==0):
            year=y
        elif( year!=y ):
            
            temp_of_year1(month_max_temp)
            year=y
        
        ma=dict()# dict for max_temp in month
        
       
        
        r=open(s+"\\"+i,'r+')
        f=r.readlines()
        for line,data in enumerate(f):
            
            data=data.strip().upper()

            x=data.split(',')

            if (not(data.find('\n') and len(data)==0)):

               

                if(line!=1):#blank line or space

                    if(x[0][0]!='<'):# to check the last line

                        if (x[1]==""):

                            ma.update({x[0]:0})#if temp is not in recorde 
                            
                        else:
                            ya=int(x[1])
                            ma.update({x[0]:ya})
                            
                            
         
                       
        r.close()

        temp_of_month1(ma)

        if(i=="lahore_weather_2011_May.txt"):
            temp_of_year1(month_max_temp)
    retrive(2)


def weatherman(a,s):
    if(a is not None and s is not None):
        
        
        if (a==1):
            report1(s)
            
        elif(a==2):
            
            report2(s)
        else:
            print '\n\n***please Enter a vaild number***'
    else:
        print("\n\n[-] Usage:\n\t weatherman [report#] [data_dir]\n\t[Report #]\n\t 1 for Annual Max/Min Temperatur\n\t 2 for Hottest day of each year\n\t[data_dir]\n\t Directory containing weather data files")


def main():
    


    print("\t\t welcome to weatherman :")
    print("[!] press 1/2 for report:")
    print("[!] enter dictory path:")
    try :
        
        e=input("enter the num:")
        s=input("Enter the dictory path:")
    except SyntaxError:
        e=None
        s=None
        
    
    
   
    
    weatherman(e,s)


if __name__== "__main__": main()
