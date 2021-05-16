
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# For Loops
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

# Question
counties_tuple = ("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuple)):
      print(counties_tuple[i])
for county in counties_tuple:
      print(county)



# Iterate Through a Dictionary
coutnies_dict = {"Arapahoe": 422829 , "Denver": 463353,"Jefferson":432438}
for county in coutnies_dict:
    print(county)

for county in coutnies_dict.keys():
    print(county)



# SKILL DRILL
coutnies_dict = {"Arapahoe": 422829 , "Denver": 463353,"Jefferson":432438}
counties = coutnies_dict.keys()
print(counties)

for county in counties:
     print (county)

# Get the Values of a Dictionary
#1 
for voters in coutnies_dict.values():
     print(voters)
#2
for county in coutnies_dict:
    print(coutnies_dict[county])
#3
for county in coutnies_dict:
    print(coutnies_dict.get(county))

# Get the Key-Value Pairs of a Dictionary
for county, voters in coutnies_dict.items():
    print(county, voters)

    #SKILL DRILL
# Print each county and registered voter form the counties dictionary so that the output will have registered voters  ,county and voters
for county,voterrs in coutnies_dict.items():
    print(county,"county has", str(voters),"registered voters")


# Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
              {"county":"Denver", "registered_voters": 463353},
              {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:  
  print(county_dict)


# Get the Values from a List of Dictionaries
for county_dict in voting_data:
  for value in county_dict.values():
    print(value)
# Question 
for county_dict in voting_data:

 print(county_dict['registered_voters'])
       
       
for county_dict in voting_data:
 print(county_dict['county'])

# F-strings: Formatted String Literals
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
     
# F string
print(f"I received {my_votes/total_votes *100} % of the total votes")


#Using F-Strings with Dictionaries
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

# Using F-Strings with Dictionaries
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters ")


# Multiline F-Strings (f'{value"{width}.{precision}}')
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes "
    f"The total number of votes in the election was {total_votes}."
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print (message_to_candidate)

# Format Floating-Point Decimals
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes "
    f"The total number of votes in the election was {total_votes:,} "
    f"You received {candidate_votes / total_votes *100:.2f}% of the total votes")
print (message_to_candidate)

#SKILL DRILL
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
for county, voters in counties_dict.items():
 print(f"{county} county has {voters,:} registered voters.)")

