# Object to hold information about match.
class Response:
  def __init__(self,name,contact, gender, program, stream, first_choice, second_choice, third_choice):
    self.name = name
    self.contact = contact
    self.gender = gender
    self.program = program
    self.stream = stream
    self.first_choice = first_choice
    self.second_choice = second_choice
    self.third_choice = third_choice
