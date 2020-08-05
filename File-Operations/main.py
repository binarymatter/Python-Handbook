 
 # Reference : https://www.w3schools.com/python/python_file_handling.asp

 # Modes
'''
By default "mode=r"
Both read & write: mode=r+
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images) (Like mode = wb)

'''

f = open('test.txt')
print(f.read())
''' Output : Hey There 
		     Its me
'''

'''Remember that read() reads the entire thing present in the file. So if you want 
to re read the file from the beginning make sure to f.seek(0) to place the cursor back to the 
starting'''

f = open('test.txt')
print(f.readline())  # Reads the contents of the file line by line
# Output : Hey There

f = open('test.txt')
print(f.readlines())	#Returns a lists which contains all the lines
# Output : ['Hey there \n', 'Its me']

# Standard Way To Open A File

with open('test.txt') as f :
	print(f.readlines())

# Always close the file once opened
f.close()

#Another Example
with open('test.txt',mode='r+') as f:
	text = f.write('hellooooo')
'''Output : hellooooo
            Its me
'''

# Its better to perform file operations within try and except block