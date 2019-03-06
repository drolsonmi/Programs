
# coding: utf-8

# In[11]:

# GetWxData.py
# October 24, 2015
# Select satellite images from a certain date range
# Create a .sh file to download



# In[2]:

##### FUNCTIONS #####
def JulianDate(year,month,day):
    LeapYear = 0
    if year%4 == 0:
        LeapYear = 1
    
    days_in_month = {1 : 0,
                     2 : 31,
                     3 : 31+28+LeapYear,
                     4 : 31+28+31+LeapYear,
                     5 : 31+28+31+30+LeapYear,
                     6 : 31+28+31+30+31+LeapYear,
                     7 : 31+28+31+30+31+30+LeapYear,
                     8 : 31+28+31+30+31+30+31+LeapYear,
                     9 : 31+28+31+30+31+30+31+31+LeapYear,
                     10 : 31+28+31+30+31+30+31+31+30+LeapYear,
                     11 : 31+28+31+30+31+30+31+31+30+31+LeapYear,
                     12 : 31+28+31+30+31+30+31+31+30+31+30+LeapYear,
                    }
    return(days_in_month[month]+day)


# In[3]:

##### INPUT DATA #####
correct = "n" 
while correct == "n":
    year = int(input("What year do you want data?\n>> "))
    month = int(input("What month do you want data?\n>> "))
    day0 = int(input("What is the first day for which you want to pull data?\n>> "))
    dayf = int(input("What is the last day for which you want to pull data?\n>> "))
    print("\nData starting: {0:02d}/{1:02d}/{2:04d}".format(month,day0,year))  
    print("Data finishing: {0:02d}/{1:02d}/{2:04d}".format(month,dayf,year)    )
    correct = input("Are these dates correct? (y/n)\n>> ")

shortyear = year - (100*round(year/100))
jday0 = JulianDate(year,month,day0)
jdayf = JulianDate(year,month,dayf)
print("\nDates accepted: Julian Dates = [{0:0d} - {1:0d}]".format(jday0,jdayf))


# In[4]:

##### SELECT TYPE OF DATA #####
print("Which Dataset?")
print("  1) Surface Plots (Continental US)")
print("  2) Surface Plots (North America)")
print("  3) US East Coast Satellite (GOES 16)")
print("  4) Atlantic Ocean Satellite (GOES 16)")
print("  5) US West Coast Satellite")
print("  6) East Pacific Coast Satellite")
print("  7) Gulf of Mexico and Carribean Satellite")
data_type = int(input(">> "))

if data_type > 2:
    print("Which Satellite?")
    print("  1) IR")
    print("  2) Visible")
    print("  3) Water Vapor")
    satellite = int(input(">> "))


# In[12]:

##### SELECTING THE SATELLITE #####
satellite_name = {3: "GOES16-CONUS",
                  4: "GOES16-Atlantic",
                  5 : "WC",
                  6 : "HP",
                  7 : "HU",
                 }
satellite_image = {1 : "IR",
                   2 : "VS",
                   3 : "WV",
                  }

filename = "GetWxImages-" + satellite_name[data_type] + "-" + satellite_image[satellite] + ".sh"
outfile = open(filename,'w')
outfile.write("#!/bin/bash\n")
# In[6]:

##### SURFACE PLOTS (Continental US) #####
if data_type == 1:
    for day in range(day0,dayf):
        for hr in range(8):
            outfile.write("wget http://www.wpc.ncep.noaa.gov/archives/sfc/{0:04d}/usfntsfc{0:04d}{1:02d}{2:02d}{3:02d}.gif\n".format(year,month,day,hr*3))


# In[7]:

##### SURFACE PLOTS (North America) #####
if data_type == 2:
    for day in range(day0,dayf):
        for hr in range(8):
            outfile.write("wget http://www.wpc.ncep.noaa.gov/archives/sfc/{0:04d}/namfntsfc{0:04d}{1:02d}{2:02d}{3:02d}.gif\n".format(year,month,day,hr*3))


##### CONUS East Coast Satellite (GOES 16) #####
if data_type == 3:
    for jday in range(jday0,jdayf):
        for hr in range(24):
            for minute in range(12):
                if satellite == 1:
                   outfile.write("wget https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/13/{0:04d}{1:03d}{2:02d}{3:02d}_GOES16-ABI-CONUS-13-1250x750.jpg\n".format(year,jday,hr,(minute*5)+2))
                if satellite == 2:
                   outfile.write("wget https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/{0:04d}{1:03d}{2:02d}{3:02d}_GOES16-ABI-CONUS-GEOCOLOR-1250x750.jpg\n".format(year,jday,hr,(minute*5)+2))
                if satellite == 3:
                   outfile.write("wget https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/09/{0:04d}{1:03d}{2:02d}{3:02d}_GOES16-ABI-CONUS-09-1250x750.jpg\n".format(year,jday,hr,(minute*5)+2))


##### CONUS Atlantic Satellite (GOES 16) #####
if data_type == 4:
    for jday in range(jday0,jdayf):
        for hr in range(24):
            for minute in range(12):
                if satellite == 1:
                   outfile.write("wget https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/taw/13/{0:04d}{1:03d}{2:02d}{3:02d}_GOES16-ABI-taw-13-1250x750.jpg\n".format(year,jday,hr,(minute*5)+2))
                if satellite == 2:
                   outfile.write("wget https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/taw/GEOCOLOR/{0:04d}{1:03d}{2:02d}{3:02d}_GOES16-ABI-taw-GEOCOLOR-1250x750.jpg\n".format(year,jday,hr,(minute*5)+2))
                if satellite == 3:
                   outfile.write("wget https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/taw/09/{0:04d}{1:03d}{2:02d}{3:02d}_GOES16-ABI-taw-09-1250x750.jpg\n".format(year,jday,hr,(minute*5)+2))


##### SATELLITE IMAGES #####
if data_type > 5:
    for jday in range(jday0,jdayf):
        for hr in range(24):
            outfile.write("wget http://www.goes-arch.noaa.gov/{3}{4}{0:02d}{1:03d}{2:02d}00.GIF\n".format(shortyear,jday,hr,satellite_name[data_type],satellite_image[satellite]))
            outfile.write("wget http://www.goes-arch.noaa.gov/{3}{4}{0:02d}{1:03d}{2:02d}15.GIF\n".format(shortyear,jday,hr,satellite_name[data_type],satellite_image[satellite]))
            outfile.write("wget http://www.goes-arch.noaa.gov/{3}{4}{0:02d}{1:03d}{2:02d}30.GIF\n".format(shortyear,jday,hr,satellite_name[data_type],satellite_image[satellite]))
            outfile.write("wget http://www.goes-arch.noaa.gov/{3}{4}{0:02d}{1:03d}{2:02d}45.GIF\n".format(shortyear,jday,hr,satellite_name[data_type],satellite_image[satellite]))


# In[14]:

outfile.close()


# In[4]:

print("--------------------------------\nFile Exported: GetWxImages.sh\n--------------------------------")
print("To complete the download:")
print(" - run \"chmod a+x GetWxImages.sh\"")
print(" - run \"./GetWxImages.sh\"")
print("\nTo convert the images to a .gif file, run the following command:")
print("   $ convert -delay 6 -loop 0 *IR* <Event Name>_IR.gif")


# In[ ]:



