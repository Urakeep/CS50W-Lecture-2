people = [
  {"name":"Harry","house":"Gryffindor"},
  {"name":"Cho","house":"Ravenclaw"},
  {"name":"Draco", "house":"Slytherin"}
]

def f(person):
  return(person["name"])

people.sort(key=f) # sort person with their name alphabetically
people.srot(key=lambda person: person["name"]) # using lambada gives the same result within one line of code

print(people)