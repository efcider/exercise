#subject={"math","biology","ict"}


#subject.add("physics")
#subject.update(["chemistry"])




#subject.remove("ict")
#print(subject)


#print(len(subject))



#mounthleap=[31,29,31,30,31,30,31,31,30,31,30,31]



mounth=[31,28,31,30,31,30,31,31,30,31,30,31]

days=0
funday=0
dayinweek=7 #in case number of days in week  change 
sundaymod=5 #mode of first sunday


for y in range(1901,2000+1):
    for x in mounth:
        days+=x
        if(y%4==0 and x==28):
            days+=1
            

        if (days%dayinweek==sundaymod):
            funday+=1
print(funday)

