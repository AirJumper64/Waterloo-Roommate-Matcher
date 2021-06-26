import csv
import Class_feature
from Parse_Files.parse_files import parse_gender, parse_program, parse_stream, parse_top_choice, bool_answer

# Function to check if user already exists in 
def contains_user(user_name):
  with open("Responses.csv") as responses:
        reader = csv.reader(responses)
        next(reader)
        #next(reader)
        for row in reader:
          # Checking is user is already in CVS
          if row[1] == user_name:
            return (row[3], row[4], row[5], row[6], row[8])
  contact = input("Please enter your email. ")
  gender = parse_gender(input("What is your gender? "))
  program = parse_program(input("What is your program? "))
  stream = parse_stream(input("Please enter your stream. "))
  first_choice = parse_top_choice(input("Please enter your first choice residence.\nThe choices are CMH, MKV, UWP, REV, V1 and St. Paul's. "))
  with open("Responses.csv", 'a') as Responses:
      writer = csv.writer(Responses)
      row = ["",user_name,"",contact,gender,program,stream,"",first_choice,"","","","","","",""]
      writer.writerow(row)
  return(contact, gender, program, stream, first_choice)

def main():
  run_program = True
  while run_program:
    # User variables
    responseName = input("What is your full name? ")
    check_program = False
    check_program = bool_answer(input("Do you want to match with your program? Y/N. "))
    # Matches found
    list_of_matches = []
    # Look for user in CSV.
    name_check = contains_user(responseName)
    
    # Save informtation we need.
    contact = name_check[0]
    gender = name_check[1]
    program = name_check[2]
    stream = name_check[3]
    first_choice = name_check[4]
    
    print(f"""\nContact (email/instagram): {contact}\nGender: {gender}\nProgram: {program}\nStream: {stream}\nResidence Choice: {first_choice}\n""")

    with open("Responses.csv") as responses:
      reader = csv.reader(responses)
      #skip headings
      next(reader)   
      for row in reader:
          # In case self is located.
          if row[1] != responseName:
            # Check all responses for matching gender, stream and top choice.
            if(gender == parse_gender(row[4]) and stream == parse_stream(row[6]) and first_choice == parse_top_choice(row[8])):
              # Only does this if user is looking for people in same program.
              if check_program:
                if program == parse_program(row[5]):
                  current_match = Class_feature.Response(row[1], row[3], row[4], row[5], row[6], row[8])
                  list_of_matches.append(current_match)
              # Checks for matches in gender, stream and top choice, regardless of program.
              else:
                current_match = Class_feature.Response(row[1], row[3], row[4], row[5], row[6], row[8])
                list_of_matches.append(current_match)
    for match in list_of_matches:
      print(f"Match: \n\tName: {match.name}\n\tContact info: {match.contact}\n\tProgram: {match.program}")

    
    run_program = bool_answer(input("Would you like to run again? Y/N "))

if __name__ == "__main__":
  main()

