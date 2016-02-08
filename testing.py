#NAME:      Kristian
#DATE:      11/2015
#PURPOSE:   Program that saves unit details and tests
#           the user on their knowledge.

#   Testing source control feature in VS 2015

import json
import random
import os
import shutil 

#Function to create a directory if it does not exist 
def CheckDir(dr):
    fDir = os.path.dirname(__file__)
    relPath = "Units/" + dr
    absPath = os.path.join(fDir,relPath)
    
    if not os.path.exists(absPath):
        os.makedirs(absPath)

#Same function but returns directory 
def ReturnDir(dr):
    fDir = os.path.dirname(__file__)
    relPath = "Units/" + dr
    absPath = os.path.join(fDir,relPath)
    
    if not os.path.exists(absPath):
        os.makedirs(absPath)
    return absPath

#Function to add a unit
def AddUnit(units):
    try:
        unitTitle = input("Enter the unit title: ")
        units.append(unitTitle)

        #Create a directory for the new unit and a file of the unit's name. 
        
        absPath = ReturnDir(unitTitle) + "/" + unitTitle + ".txt"        
        f = open(absPath,"w")
        f.close()

        #Add unit to units file

        units = SaveUnits(units)
    except Exception as e:
        print(e.strerror)
    finally:
        return units

#Function to add unit content
def AddContent(unit, contentList):
    try:
        contentTitle = input("Enter the unit content title: ")
        contentList.append(contentTitle)

        #Create unit content file
        absPath = ReturnDir(unit) + "/" + contentTitle + ".txt"
        f = open(absPath,"w")
        f.close()
        
    except Exception as e:
        print(e.strerror)
    finally:
        return SaveContentList(unit, contentList)

        
        

#Function to delete a unit
def DeleteUnit(units):
    try:
        print("Enter the unit number you wish to delete, between 1 and ",len(units))
        delInt = input("")
        try:
            delInt = int(delInt)
            absPath = ReturnDir(units[delInt-1])
            shutil.rmtree(absPath)
            del units[delInt-1]
        except Exception:
            print("Invalid input")
    except Exception as e:
        print(e.strerror)
    finally:
        return SaveUnits(units)

#Function to delete unit content
def DeleteContent(unit, contentList): 
    try:
        print("Enter the unit content number you wish to delete, between 1 and ", len(contentList))
        delInt = input("")
        try:
            delInt = int(delInt)
            absPath = ReturnDir(unit) + "/" + contentList[delInt-1] + ".txt"
            os.remove(absPath)
            del contentList[delInt-1]            
        except Exception:
            print("Invalid input")
    except Exception as e:
        print(e.strerror)
    finally:
        return SaveContentList(unit,contentList)
        

#Function to save units to file
def SaveUnits(units):
    fDir = os.path.dirname(__file__)
    relPath = "units.txt"
    absPath = os.path.join(fDir,relPath)
    f = open(absPath,"w")
    json.dump(units,f,indent=4)
    f.close()
    return units

#Function to save unit contents to unit file
def SaveContentList(unit, contentList):
    absPath = ReturnDir(unit) + "/" + unit + ".txt"
    f = open(absPath,"w")
    json.dump(contentList,f,indent=4)
    f.close()
    return contentList

#Function to save content list
def SaveContent(unit, contentList, contentName):
    absPath = ReturnDir(unit) + "/" + contentName + ".txt"
    f = open(absPath,"w")
    json.dump(contentList,f,indent=4)
    f.close()
    return contentList

def AddQuestion(unit, contentList, contentName):
    try:
        lstQuestion = []
        qNum = len(contentList) + 1
        lstQuestion.append(input("\nEnter question " + str(qNum) + ": "))
        lstQuestion.append(input("\nEnter answer: "))

        while True:
            keyword = input ("Enter key words for the right answer (enter \'e\' to exit): ")

            if keyword == "e":
                break

            lstQuestion.append(keyword)

        contentList.append(lstQuestion)
    except Exception:
        print("An error occured, please check your data.")
    finally:
        return SaveContent(unit, contentList, contentName)

def DeleteQuestion():
   pass

def ListQuestions(contentList):
    for i,q in enumerate(contentList,start=1):
        print(i,".",q[0],"\n")

def TestQuestions(contentList):
    print('Testing must needs doing.')

#Function to load contents of unit
def LoadUnitContent(unit):
    try:
        absPath = ReturnDir(unit) + "/" + unit + ".txt"
        f = open(absPath,"r")
        contentList = json.load(f)
        f.close()
    except Exception:
        print("No unit content found")
        print("Please add some content")
        contentList = []

    while True:
        if len(contentList) > 0:
            print("Please select a unit content, or add content.")
            contentList.sort()
            for i in range(0, len(contentList)):
                print(i+1, ". ", contentList[i])

        print("\na .  Add content")
        print("d .  Delete content")
        print("e .  Exit to units")

        conSel = input("")
        try:
            conSel = int(conSel)
            try:
                LoadQuestions(unit,contentList[conSel-1])
            except IndexError:
                print("Index out of range")
        except Exception:
            conSel = conSel.lower()
            if conSel == "a":
                contentList = AddContent(unit,contentList)
            elif conSel == "d":
                contentList = DeleteContent(unit,contentList)
            elif conSel == "e":
                print("Good luck")
                break
            else:
                print("Invalid input") 
            
#Function to load questions about the unit content
def LoadQuestions(unit,content):
    try:
        absPath = ReturnDir(unit) + "/" + content + ".txt"
        f = open(absPath,"r")
        contentList = json.load(f)
        f.close()
    except Exception:
        print("No questions found.")
        contentList = []

    while True:
        print("\n",unit," test")
        uInput = input("\nChoose [t]est, [a]dd question, [l]ist, [d]elete, [e]xit: ")
        uInput = uInput.strip().lower()

        if uInput == "t":
            print("todo")
        elif uInput == "a":
            contentList = AddQuestion(unit,contentList,content)
        elif uInput == "l":
            ListQuestions(contentList)
        elif uInput == "d":
            print("todo")
        elif uInput == "e":
            print("Good luck")
            break
        else:
            print("Invalid input") 


    

#Main function
def main():
    try:
        fDir = os.path.dirname(__file__)
        relPath = "units.txt"
        absPath = os.path.join(fDir,relPath)
        f = open(absPath,"r")
        units = json.load(f)
        f.close()
    except Exception:
        print("No units found")
        print("Please add units.")
        units = []

    while True:
        if len(units) > 0:
            print("Please select a unit, or add a unit.")
            units.sort()
            for i in range(0,len(units)):
                print(i+1, '. ', units[i])

        print("\na .  Add Unit")
        print("d .  Delete Unit")
        print("e .  Exit Program")

        unitSel = input("")
        try:
            unitSel = int(unitSel)
            try:
                LoadUnitContent(units[unitSel-1])
            except IndexError:
                print("index out of range")
        except Exception:
            unitSel = unitSel.lower()
            if unitSel == "a":
                units = AddUnit(units)
            elif unitSel == "d":
                units = DeleteUnit(units)
            elif unitSel == "e":
                print("Good Luck!")
                break
            else:
                print("Invalid input.") 

main()
        
        
