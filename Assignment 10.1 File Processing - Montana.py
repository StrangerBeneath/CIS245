# Assignment 10.1 - File Processing
# CIS 245 - Michael Montana
# 20 February 2022
# =================================================================================================================================================================================
# This week we will create a program that performs file processing activities.
# Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.
# Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.
# The program should then prompt the user for their name, address, and phone number.
# Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user.
# Once the data has been written your program should read the file you just wrote to the file system and display the file contents to the user for validation purposes.
# Submit a link to your Github repository.
# ================================================================================================================================================================================
import os
yeslist = ['y', 'ye', 'yes', '']


def openWrite(fileComp, userName, address, phoneNum):  # open and write file
    with open(fileComp, 'w')as fileHandle:
        fileHandle.write('{}, {}, {}'.format(userName, address, phoneNum))
    print('You\'ve written following text to the file:\n')


def openRead(fileComp):  # open and read file
    with open(fileComp, 'r') as fileHandle:
        fileRead = fileHandle.read()
    print(fileRead)


# open and append on the next line of a file
def openAppend(fileComp, userName, address, phoneNum):
    with open(fileComp, 'a')as fileHandle:
        fileHandle.write('\n{}, {}, {}'.format(userName, address, phoneNum))
    print('You\'ve appended the following text to the file:\n')


def fileUpdate(fileComp, userName, address, phoneNum, oaChoice):
    if oaChoice == '1':
        openWrite(fileComp, userName, address, phoneNum)
        openRead(fileComp)
    else:
        openAppend(fileComp, userName, address, phoneNum)
        openRead(fileComp)


def fileInfo():
    filePath = input(
        '\nPlease provide the directory you would like the file stored: ')
    # if dir does not exist loop for another input
    if os.path.isdir(filePath) is False:
        while os.path.isdir(filePath) is False:
            filePath = input(
                'The provided directory does not exist.  Please provide a valid directory: ')
    else:
        print('\nYour Directory was found.')
    fileName = '\\' + input('\nPlease provide a file name:')+'.txt'
    fileComp = filePath + fileName
    return fileComp


def user():
    userName = input('Please enter your name: ')
    address = input('Please enter your address: ')
    phoneNum = input('Please enter your phone number: ')
    return userName, address, phoneNum


def main():
    moreFiles = 'yes'
    while moreFiles in yeslist:
        print(str('This program stores/appends user information to a text file').center(100, '_') + ('\n'))
        print('\nPlease provide the following:\n')
        userName, address, phoneNum = user()
        fileComp = fileInfo()
        if os.path.exists(fileComp):
            print('\nThe file already exists, and contains the following:')
            openRead(fileComp)
            oaChoice = input(
                '\nSelect one of the following options:\n[1] Overwrite File\n[2]Append to File\n')
            while oaChoice != '1' and oaChoice != '2':
                oaChoice = input(
                    '\nChoose 1 to Overwrite File; or 2 to Append to File:')
            fileUpdate(fileComp, userName, address, phoneNum, oaChoice)
        else:
            oaChoice = 1
            print('\nYou are creating a new file.\n')
            fileUpdate(fileComp, userName, address, phoneNum, oaChoice)
        moreFiles = input(
            '\nWould you like to add user information to additional files (yes/no)?\n')


if __name__ == "__main__":
    main()
