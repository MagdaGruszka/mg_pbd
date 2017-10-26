name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)



data = [-14.82381293, -0.29423447, -13.56067979, -1.6288903, -0.31632439,
          0.53459687, -1.34069996, -1.61042692, -4.03220519, -0.24332097]

x_bar = sum(data) / len(data)
print "x_bar=", x_bar

varRes = sum([(xi - x_bar)**2 for xi in data]) / len(data)

print varRes

def standard_deviation(varRes):
    return varRes(varRes)**0.5??????
 
 #