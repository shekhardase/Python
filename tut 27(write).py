# Handle open and append:-
f = open("Tut 27 autoform.py","a")
f.write("harry bhai is dope\n")
f.close()

# Handle open and write:-                           # Here codes are mixed to run it properly run only one use '#'
f = open("Tut 27 autoform.py","w")
f.write("harry bhai is dope\n")
f.close()

#Handle read and write both:-
f =  open("Tut 27 autoform.py","r+")
print(f.read())
f.write("Thank you\n")


"""
# SOME NOTES :-
(1) F is object for file. It is not a method or special character. You ca you use chacracter or word of your own.


(2) "w" Mode :-
      Here "w" stands for write. After opening or creating a file , a function, f.write() is used to insert text into a file. 
     The text is written inside closed parenthesis (" ") surrounded by double quatations. 
    There is a certain limitation to write mode of opening file that is overrides the existing data into file.
  for newely created file it does no harm , but in case of already existing file , the previous data is lost as f.write() overrides it.


(3) "a" Mode :-
         a stands for append means adding something at end of already written document and same is function the mode performs here.
       It adds more content at end of existing content.
      Same function f.write() is used to add text to file inappend mode.
     It is worth nothing that append mode will also create a new file if that file with same name does not exist and can also can be used to write in an empty file.


(4) "r+" Mode:-
        r+ mode is more of a combination of reading and append then read and the write.
       By opening a file in this mode,we can print the existing content on to the screen by printing f.read() function and adding or appending text to it using f.write() function.
 
 
 """