f = open("Tut 26 part1.py","r")  # Here we used open function to open tut 26 part 1 file
content = f.read()           # Sytax for open :- open("filename" ,"mode")
print(content)               # We must specify name of file and its extension ,
f.close()                      # Access mode where we can specify in which mode file has to be opened it could be read(r), write(w) or append(a)

"""In above example we stored file in variable which generally called as file pointer/file handler 
Hence code is snipped to open the file using fle handling in Python"""

""" We can use file pointer to further add more modification in file
Errors can occurs due to reasons like trying to access file that is already closed or trying to read a file open in write mode."""

"""We can read a whole file line by line using a for loop in combination with an iterator. 
    This will be a fast and efficient way of reading data."""

""" Python needs to know how to open file exactly. """

""" Two access modes are available reading (r), and reading in binary mode (rb)."""

""" They have to be specified during opening a file with the built-in open() method."""

"""read() , reads whole file by default but if we add numbers in read() we cam read exact lines"""

"""You can use the readline() method to read individual lines of a file.
    By calling readline() a second time, you will get the next line"""

"""readlines() method reads until the end the file ends and returns a list of lines of the entire file. 
    It does not read more than one line."""

# ALWAYS CLOSE YOUR FILE BY .close()