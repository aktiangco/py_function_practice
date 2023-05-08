# Activity: File Manipulation
# *! To check: python3 day4/error_check_handling.py

# acivity for errors
fileName = input("Please enter hte name of the file you would like to read: ")
myfile = open(fileName, 'r') # Open a file for reading.
contents = myfile.readlines() # Read in the content by line.clear
myfile.close() # Explicitly close the file
print(contents) #print the contents of the file

'''
# TODO 
# Your task for this activity is to complete the program by gracefully handling any errors that might come your way. There are many ways to do this, but for this activity you will be creating a class to manipulate files, called FileManipulator. To successfully create this class, complete the following steps:

# TODO - Create the FileManipulator class and implement the constructor. The constructor should accept the name of a file to read in and should continually prompt for input if the name given causes an error. Make sure that you give an informative message if an error is raised.

 # TODO - Implement the reverse() function. This function should accept the name of a file to write to and should write each line of the original file to this new file. However, in the new file, although the line order will be the same, the string that makes each line will be reversed. So "cheese" will become "eseehc". Be careful not to add an extra newline character at the beginning of the file. Make sure that errors are handled elegantly, and appropriate error messages are given.'
'''
# from the solution code
class FileManipulator:
    def __init__(self, file_name):
        self.file_name = self.get_valid_file_name(file_name)

    def get_valid_file_name(self, file_name):
        while True:
            try:
                # Attempt to open the file to check if it exists
                with open(file_name, 'r'):
                    return file_name
            except FileNotFoundError:
                print("File not found. Please enter a valid file name.")
                file_name = input("Enter the name of the file to read: ")

    def reverse(self, output_file_name):
        try:
            with open(self.file_name, 'r') as input_file:
                lines = input_file.readlines()

            with open(output_file_name, 'w') as output_file:
                for line in lines:
                    reversed_line = line.strip()[::-1]  # Reverse the line
                    output_file.write(reversed_line + '\n')

            print("Reversal complete!")
        except FileNotFoundError:
            print("Input file not found.")
        except PermissionError:
            print("Permission denied. Cannot write to the output file.")
        except Exception as e:
            print("An error occurred during the reversal process:", str(e))


# Example usage
file_name = input("Enter the name of the file to read: ")
file_manipulator = FileManipulator(file_name)
output_file_name = input("Enter the name of the output file: ")
file_manipulator.reverse(output_file_name)

        




'''
test code:

f = FileManipulator("tmp.txt")
print(f.contents)
f.reverse("tmp2.txt")
'''
