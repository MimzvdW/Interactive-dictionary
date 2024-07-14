import json

data = json.load(open("DictionaryIndex.json")) # Load the dictionary data from a JSON file
word = str(input("Enter the word you want to search: ")) # Prompt the user to enter the word they want to search

# Check if the entered word is a digit, which is invalid
if word.isdigit():
    print("Wrong search!! Please try again")
    word = str(input("Enter the word you want to search: "))

# Check if the entered word exists in the dictionary data
if word in data:
    print(data[word]) # Print the definition of the word if it exists
else:
    print("Wrong search!! Please try again")
    # Ask the user if they want to find a close match
    match = str(input("Do you want to find a close match? Enter Y for Yes and N for No: ")).lower()

    if match == "y":
        from difflib import get_close_matches
         # Find the closest matching word in the dictionary data
        close_matches = get_close_matches(word, data.keys())[0]
        print(close_matches)
        # Check if the closest match exists in the dictionary data
        if close_matches in data:
            print(data[close_matches]) # Print the definition of the closest matching word
        else:
            # Inform the user that the word doesn't exist
            print("The word doesn't exist. Please double check it")

    elif match == "n":
        # Thank the user for using the dictionary and exit
        print("Thank you for using my Dictionary ;) ")
        exit()

    else:
        # Inform the user that the word doesn't exist and prompt for a new word
        print("The word doesn't exist. Please double check it")
        str(input("Enter the word you want to search: "))
