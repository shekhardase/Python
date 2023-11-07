var = "harry is a good boy"
var1 = "harrry123"
var2 = "harryisgoodboy"
print(var.endswith("boy"))
print(var.count("o"))
print(var.capitalize())
print(var.lower())
print(var.upper())
print(var.replace("good","bad"))

print(var1.isalnum())             #isalnum : should contain numbers and alphabates without space    as space is counted it is neither alphabate nor number
print(var.isalnum())
print(var1.isalpha())             #isalpha : should contain only alphabates without space
print(var2.isalnum())
print(var2.isalpha())
