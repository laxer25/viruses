#Created by Jonny Chen, Nate Chen, Matthew Shao, and Tyler Hadziyianis
#This project is a questionnaire project that will diagnose participants with common illnesses based on their symptoms.

import time
print("This program will diagnose your illness with various symptoms of possible illnesses")
print("This however should not be the only source used and it is recommended to go see a doctor as well")
time.sleep(1)

virus = ["Covid 19", "Influenza","Common Cold","Strep Throat", "Sinus Infection"]

#This is the determination of what illness is to be diagnosed
q1 = input("Do you have a sore throat? ")
if q1.lower() == "yes":
  virus = ["Covid 19", "Influenza","Common Cold", "Strep Throat"]
  q2 = input("Are you coughing? ")
  if q2.lower() == "yes":
    virus = ["Covid 19", "Influenza","Common Cold"]
    q3 = input("Were the symptoms appearing gradually? ")
    if q3.lower() == "yes":
      virus = ["Covid 19","Common Cold"]
      q4 = input("Are you aching? ")
      if q4.lower() == "yes":
        virus = ["Covid 19"]
        print (virus)
      elif q4.lower() == "no":
        virus = ["Common Cold"]
        print (virus)
    elif q3.lower() =="no":
      virus = ["Influenza"]
      print (virus)
  elif q2.lower() =="no":
    virus = ["Strep Throat"]
    print (virus)
elif q1.lower() == "no":
  virus = ["Sinus Infection"]
  print (virus)

#This will give a list of the symptoms after the diagnosis to help either steer the participant from a false diagnosis or help determine if the diagnosis is accurate
if virus == ["Covid 19"]:
  print ("Common Symptoms: \n Fever \n Dry Cough \n Tiredness \nLess Common Symptoms: \n Aches and pains \n Sore throat \n Diarrhea \n Conjunctivitis \n Headache \n Loss of taste or smell \n A rash on skin \nSevere Symptoms: \n Difficulty breathing \n Chest pain/pressure \n Loss of speech or movement")
elif virus == ["Common Cold"]:
  print ("Symptoms: \n Nose stuffiness \n Runny nose \n Sore throat \n Cough \n Congestion \n Mild headache \n Sneezing \n Malaise \n Fever")
elif virus == ["Influenza"]:
  print("Symptoms: \n Fever\n Malaise \n Headache \n Runny nose \n Postnasal drip \n Sneezing \n Reduced sense of smell \n Metallic taste in mouth \n Chills \n Cough \n Body pain or muscle pain \n Sore throat")
elif virus == ["Strep Throat"]:
  print("Symptoms: \n Sudden fever \n Red throat \n Headache \n Chills \n Loss of appetite \n Swollen lymph nodes \n Trouble swallowing")
elif virus == ["Sinus Infection"]:
  print("Symptoms: \n Headaches \n Postnasal drip \n Congestion \n Coughing \n Fever \n Brightly covered mucus \n Fatigue \n Bad breath \n Tooth pain")
