# cities=["london","bristol","sydney","leeds"]
#
# with open("cities.txt",'w')as city_files:
#     for city in cities:
#         print(city,file=city_files)
#
# cities=[]
# with open("cities.txt",'r')as city_files:
#     for city in city_files:
#         cities.append(city.strip('\n'))
# print(cities)
# for city in cities:
#     print(city)
#
imelda="more mayhem","imelda may","2011",(
    (1,"pulling th ring"),(2,"psycho"),(3,"mayhem"),(4,"kentish town waltz"))

# with open("imelda3.txt",'w')as imelda_files:
#     print(imelda,file=imelda_files)
# with open("imelda3.txt",'r')as imelda_files:
#     print(imelda,file=imelda_files)

with open("imelda3.txt",'r')as imelda_files:
    contents=imelda_files.readline()
imelda=eval(contents)

print(imelda)
title,artist,year,track=imelda
print(title)
print(artist)
print(year)