# Functions to parse stream input (return either 4 or 8).
def parse_stream(stream_text):
  if "na" in stream_text.lower():
    return "Stream 8"
  elif "8" in stream_text:
    return "Stream 8"
  elif "4" in stream_text:
    return "Stream 4"
  else:
    # If no proper input is given, continue to ask until it is
    return parse_stream(input("Please input either 4 or 8. "))

# Function for parsing inputted program.
def parse_program(program):
  if "mechanical" in program.lower():
    return "Mechanical Engineering"
  elif "tron" in program.lower():
    return "Mechatronics Engineering"
  elif "nano" in program.lower():
    return "Nanotechnology Engineering"
  elif "systems design" in program.lower():
    return "Systems Design Engineering"
  elif "electrical" in program.lower():
    return "Electrical Engineering"
  elif "computer engineering" in program.lower():
    return "Computer Engineering"
  elif "software" in program.lower():
    return "Software Engineering"
  elif "bio" in program.lower():
    return "Biomedical Engineering"
  elif "chemical" in program.lower():
    return "Chemcial Engineering"
  elif "civil" in program.lower():
    return "Civil Engineering"
  elif "environment" in program.lower():
    return "Environmental Engineering"
  elif "management" in program.lower():
    return "Management Engineering"
  elif "cs" in program.lower() or "computer science" in program.lower():
    return "Computer Science"
  elif "architectural" in program.lower():
    return "Architectural Engineering"
  elif "math" in program.lower():
    return "Math"
  elif "aviation" in program.lower():
    return "Science and Aviation"
  elif "kinesiology" in program.lower():
    return "Kinesiology"
  else: 
    return parse_program(input("Please input a valid Waterloo program! "))

# Function to check if a proper residence was added.
def parse_top_choice(top_choice):
  # List of accepted residences.
  residences = ("CMH", "MKV", "UWP", "REV", "V1", "St. Paul's")
  for i in range(len(residences)):
    if residences[i].lower() in top_choice.lower():
      return residences[i]
  # If there was no properly inputted residence, continue to ask until there is.
  return parse_top_choice(input("Please correctly enter a residence! The choices are: \nCMH, MKV, UWP, REV, V1 and St. Paul's. "))

# Function to control gender added.
def parse_gender(user_gender):
  if "female" in user_gender.lower():
    return "Female"
  elif "male" in user_gender.lower():
    return "Male"
  else:
    return "Other"

def bool_answer(response):
  if "y" in response.lower():
    return True
  elif "n" in response.lower():
    return False
  else:
    return bool_answer(input("Please input either 'Y' or 'N'. "))
    