# Accept the filename from the user and print the extension
filename = input("Enter the filename:")
extlist = filename.split('.')
print('The extension of the file is: ' + repr(extlist[-1]))