#MadLib.py
#Name: Jack Burke
#Date: 09/01/2024
#Assignment: Madlib.py

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input(" Give me a noun 1:")
  noun2 = input(" Give me a noun 2:")
  verb1 = input(" Give me a verb 1:")
  verb2 = input(" Give me a verb 2:")
  adjective1 = input(" Give me adjective 1:")
  adjective2 = input(" Give me adjective 2:")
  #Print the story with the user supplied words.
  print( noun1 + "met up with" + noun2 + "a" + adjective1 + "person" + "." + noun1 + verb1 + "apple pie" + "and" + noun2 + verb2 + "crawfish" + "." + noun2 + "felt" + adjective2 + ".")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
