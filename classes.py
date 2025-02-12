class Point():
  def __init__(self, input_x, input_y): # a method that automaically be called every time that create a new point.
    self.x = input_x
    self.y = input_y

p = Point(2,8)
print(p.x)
print(p.y)

class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []

  def add_passenger(self, name):
    if not self.open_seats():
      return False
    self.passengers.append(name)
    return True

  def open_seats(self):
    return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Haarry", "Ron", "Hermione","Ginny"]
for person in people:
  success = flight.add_passenger(person)
  if success:
    print(f"Added {person} to flight succesfully")
  else:
    print(f"No available seats for {person}")
