"""
Examples to show how sting formatting works in python
"""
city = "chennai"
event = "show"

print("welcome to " + city +" and enjoy the " + event)

print("welcome to %s and enjoy the %s" % (city, event))

company = "Ivy Mobility"
designation = "Senior Test Engineer"
years = "4 years"
print("I am working at %s as a %s for %s" %(company, designation, years))
print("I am working at " + company +" as a " + designation + " for " + years +"")