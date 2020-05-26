from random import choice, sample
from datetime import timedelta, date
cooking = []
washing = []

print("#+title: Rota")
print("#+options:  h:2 num:nil toc:t") 
print("\n")
def create_rota(d):
    for i in range(0, 7):
        avail_cook = ["Noam", "Laura", "Louis", "David", "Nat", "Störm"]

        if(i==0):
            cook_day=sample(avail_cook, 2)
        # no cooks two days in a row
        if(i>0):
            # remove already cooking
            for c in cooking[i-1]:
                if c in avail_cook:
                    avail_cook.remove(c)
            cook_day=sample(avail_cook, 2)
        # store cooks for the day
        cooking.append(cook_day)

    for i in range(0, 7):
        
        avail_wash = ["Noam", "Laura", "Louis", "David", "Nat", "Soko", "Sonny", "Störm"]
        cook_day=cooking[i]
        # no washers who are cooking
        for c in cook_day:
            if c in avail_wash:
                avail_wash.remove(c)
        print("* ", d.strftime("%d %b %Y %A"))
        print("- Cooking: ", cook_day[0], "and ", cook_day[1])
        cooking.append(cook_day)

        wash_day = sample(avail_wash, 3)

        print("- Washing: ", wash_day[0], ", ", wash_day[1]," and ", wash_day[2])
        washing.append(wash_day)
        d+=timedelta(days=1)
        
d1 = date.today()
for i in range (0, 100):
#     print("Week ", i, ". Starting on ", d1.strftime("%a %d %b %Y"))
#     print("----------\n")
    create_rota(d1)
    d1+=timedelta(days=7)
#     print("\n")
