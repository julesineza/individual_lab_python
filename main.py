import time,string
from typing import Any


def readFiles(filename):
    with open(filename , mode="r", encoding="utf-8") as file1:
        essay=file1.read().lower()
        essay=essay.translate(str.maketrans('', '', string.punctuation))
        essay=essay.split()
    return essay

def get_all_words(filename):
    words_dict= {}
    all_words=readFiles(filename)

    for word in all_words:
        if  not word in words_dict:
            words_dict[word]=1

        else:
            words_dict[word]+=1


    return words_dict

def common_words():
    list1=get_all_words("essay-1.txt")
    list2=get_all_words("essay-2.txt")

    arr1=[]
    arr2=[]

    for word in list1:
        arr1.append(word)
    for word in list2:
        arr2.append(word)


    intersection2=set(arr1).intersection(set(arr2))
    for i in intersection2:
        time.sleep(0.1)
        if i in list1:
            print(f"-> {i} appears {list1[i]} {'time' if list1[i] == 1 else 'times'} in essay 1")
        if i in list2:
            print(f"-> {i} appears {list2[i]} {'time' if list1[i] == 1 else 'times'} in essay 2")

def search(word):
    # Normalize word (remove punctuation and lowercase it)
    word = word.lower().translate(str.maketrans('', '', string.punctuation))

    if not isinstance(word, str) or word == "":
        print(f"-> '{word}' is not a valid word. Please enter a valid word.")
        return

    list1 = get_all_words("essay-1.txt")
    list2 = get_all_words("essay-2.txt")

    found = False

    if word in list1:
        print(f"-> {word} appears in essay 1 : {list1[word]} {'time' if list1[word] == 1 else 'times'}")
        found = True
    else:
        print(f"-> {word} does not appear in essay 1")

    if word in list2:
        print(f"-> {word} appears in essay 2 : {list2[word]} {'time' if list2[word] == 1 else 'times'}")
        found = True
    else:
        print(f"-> {word} does not appear in essay 2")

    if not found:
        print(f"-> '{word}' was not found in either essay.")


def calculatePlagiarism():
    list1=get_all_words("essay-1.txt")
    list2=get_all_words("essay-2.txt")
    intersection=list(set(list1).intersection(set(list2)))
    union=list(set(list1).union(set(list2)))
    plagiarism_level=(len(intersection)/len(union))*100

    return plagiarism_level

def main():
    print("-----------------Welcome to Plagiarism Calculator--------------------------")
    time.sleep(1)
    print("we have found the following common words in the two essays you provided: ")
    print("---------------------------------------------------------------------------")
    time.sleep(1)

    common_words()
    print("---------------------------------------------------------------------------")

    word = input("Please enter a word to search: ")
    search(word)
    print("---------------------------------------------------------------------------")
    time.sleep(1)
    plagiarism_level = calculatePlagiarism()
    if plagiarism_level >=50:
        answer="There is plagiarism in these essays"
    else:
        answer="There is no plagiarism in these essays"
    print(f"The plagiarism score is {plagiarism_level} which means {answer}")
    print("-------------------------------------------------------------------------------------------")
    print("----------------Thank you for using Plagiarism Calculator ---------------------------------")

main()



