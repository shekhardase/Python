# Seek(), Tell() and more on python files:-
"""
# TELL():
        f.tell() returns an integer giving the file pointer current position in file represented as a number of bytes.
       File pointer Handler like cursor which defines from where the data has to be read or written in file.

# SEEK():
       To change the file object position, use seek() function.
     If we want to read the file but skip the first 5 bytes , open the file, use function seek(5) to move
    to where you want to start reading, then continue reading the file.
"""

x = open("Tut 27 autoform.py","w")
print(x.write("78655654679879848465454654654646546546545"))
print(x.seek(245))
x.close()