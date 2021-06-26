# -------------------------------------------------------
# Roommate Matcher Discord Bot
# 
# By Irekanmi, Fayiz, Mike and Charlie
# June 26th, 2021
# For EngHack 2021
#
# Discord bot to bring together compatible roommates.
# -------------------------------------------------------

import csv
import Class_feature
import os
import discord
from Parse_Files.parse_files import parse_gender, parse_program, parse_stream, parse_res_choice, bool_answer

# Function to check if user already exists in database
def contains_user(user_name, contact, gender, program, stream, first_choice, second_choice, third_choice):
  with open("Responses.csv") as responses:
        reader = csv.reader(responses)
        next(reader)
        for row in reader:
          # Checking is user is already in CVS
          if row[1] == user_name:
            return
  
  with open("Responses.csv", 'a') as Responses:
      writer = csv.writer(Responses)
      row = ["",user_name,"",contact,gender,program,stream,"",first_choice,"",second_choice,"",third_choice,"","",""]
      writer.writerow(row)
  return

def main(name, check_program, contact, gender, program, stream, first_choice, second_choice, third_choice):

  contains_user(name, contact, gender, program, stream, first_choice, second_choice, third_choice)

  list_of_third_matches = []
  list_of_second_matches = []
  list_of_first_matches = []
  with open("Responses.csv") as responses:
    reader = csv.reader(responses)
    #skip headings
    next(reader)   
    for row in reader:
        # In case self is located.
        if row[1] != name:
          # Check all responses for matching gender, stream and top choice.
          if(parse_gender(gender) == parse_gender(row[4]) and parse_stream(stream) == parse_stream(row[6]) and parse_res_choice(first_choice) == parse_res_choice(row[8])):
            # Only does this if user is looking for people in same program.
            if check_program.lower == "n":
              if program == parse_program(row[5]):
                current_match = Class_feature.Response(row[1], row[3], row[4], row[5], row[6], row[8], row[10], row[12])
                if second_choice == parse_res_choice(row[10]):
                  if third_choice == parse_res_choice(row[12]):
                    list_of_third_matches.append(current_match)
                  else:
                    list_of_second_matches.append(current_match)
                else:
                  list_of_first_matches.append(current_match)
            # Checks for matches in gender, stream and top choice, regardless of program.
            else:
              current_match = Class_feature.Response(row[1], row[3], row[4], row[5], row[6], row[8], row[10], row[12])
              if second_choice == parse_res_choice(row[10]):
                if third_choice == parse_res_choice(row[12]):
                  list_of_third_matches.append(current_match)
                else:
                  list_of_second_matches.append(current_match)
              else:
                list_of_first_matches.append(current_match)
  
  # Change below to printing to chat!
  
  discord_output = ""

  if len(list_of_third_matches) > 0:
    discord_output = discord_output + ("\n***All three top residences match(es):*** ")
    for match in list_of_third_matches:
      discord_output = discord_output + (f"\n\tName: {match.name}\n\tContact info: {match.contact}\n\tProgram: {match.program}\n")
  else:
    discord_output = discord_output + ("\n***No matches with top 3 residences.***\n ")

  if len(list_of_second_matches) > 0:
    discord_output = discord_output + ("\n***Only 2 top residences match(es):*** ")
    for match in list_of_second_matches:
      discord_output = discord_output + (f"\n\tName: {match.name}\n\tContact info: {match.contact}\n\tProgram: {match.program}\n")
  else:
    discord_output = discord_output + ("\n***No matches with top 2 residences***\n")
    
  if len(list_of_first_matches) > 0:
    discord_output = discord_output + ("\n***Only 1 top residence match(es):*** ")
    for match in list_of_first_matches:
      discord_output = discord_output + (f"\n\tName: {match.name}\n\tContact info: {match.contact}\n\tProgram: {match.program}\n")
  else:
    discord_output = discord_output + ("\n***No matches with just top residence.***\n")

  return discord_output

def startup():
  client = discord.Client()
  @client.event
  async def on_ready():
    print('I am {0.user}'.format(client))


  @client.event
  async def on_message(message):
    if message.content.startswith("!findroommate"):
      try:
        msg = message.content.split(" ",10)
        #for i in range(len(msg)):
        #  msg[i] = msg[i].strip()
        name = msg[1]
        msg[2] = bool_answer(msg[2])
        if msg[2] != "False":
          checking_program = msg[2]
          contact = msg[3]
          msg[4] = parse_gender(msg[4])
          if msg[4] != "False":
            gender = msg[4]
            msg[5] = parse_program(msg[5])
            if msg[5] != "False":
              program = msg[5]
              msg[6] = parse_stream(msg[6])
              if msg[6] != "False":
                stream = msg[6]
                first_res_choice = parse_res_choice(msg[7])
                second_res_choice = parse_res_choice(msg[8])
                third_res_choice = parse_res_choice(msg[9])
                if first_res_choice != "False" and second_res_choice != "False" and third_res_choice != "False":
                  output = main(name, checking_program, contact, gender, program, stream, first_res_choice, second_res_choice, third_res_choice)
                  embedVar = discord.Embed(title = "Matches found: ", description = output)
                  await message.channel.send(embed = embedVar)
                else:
                  embedVar = discord.Embed(title = "Error", description = "Incorrect input. Please make sure you input a valid residence choice.")
                  await message.channel.send(embed = embedVar)
                  """
              else:
                embedVar = discord.Embed(title = "Error", description = "Incorrect input. Please enter stream 4 or stream 8.")
                await message.channel.send(embed = embedVar)
            else:
              embedVar = discord.Embed(title = "Error", description = "Incorrect input. Please enter a valid waterloo program.")
              await message.channel.send(embed = embedVar)
          else:
            embedVar = discord.Embed(title = "Error", description = "Incorrect input. Please enter male, female or other.")
            await message.channel.send(embed = embedVar)
        else:
          embedVar = discord.Embed(title = "Error", description = "Incorrect input. Please enter Y or N. ")
          await message.channel.send(embed = embedVar)
      except IndexError as e:
        print(e)
        embedVar = discord.Embed(title = "Error", description = "Please enter only the correct amount of parameters (name, y/n to compare programs, contact info, gender, program, stream, top res choice, second res choice, third res choice.")
        await message.channel.send(embed = embedVar)
        

  #at end
  #keep_alive()
  client.run(os.getenv('Token'))

if __name__ == "__main__":
  #print(main("charlie", "n", "c", "male", "mechanical", "8", "CMH", "UWP", "MKV"))
  startup()

# how it going