import json

data = json.load(open("DictionaryIndex.json"))
word = str(input("Enter the word you want to search: "))

if word.isdigit():
    print("Wrong search!! Please try again")
    word = str(input("Enter the word you want to search: "))

if word in data:
    print(data[word])

else:
    print("Wrong search!! Please try again")

    match = str(input("Do you want to find a close match? Enter Y for Yes and N for No: ")).lower()

    if match == "y":
        from difflib import get_close_matches
        close_matches = get_close_matches(word, data.keys())[0]
        print(close_matches)
        if close_matches in data:
            print(data[close_matches])
        else:
            print("The word doesn't exist. Please double check it")

    elif match == "n":
        print("Thank you for using my Dictionary ;) ")
        exit()

    else:
        print("The word doesn't exist. Please double check it")
        str(input("Enter the word you want to search: "))