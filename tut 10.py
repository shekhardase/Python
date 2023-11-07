#dictionary is nothing but key value pairs
d1 = {}
print(type(d1))


d2 = { "harry":"fish",
       "rohan":"fish",
       "skillf":"roti" }
print(d2["harry"])


d3 = {"shubham": {"b":"maggie",
                  "c":"roti",
                  "d":"tatti"}}
print(d3["shubham"]["b"])
print(d3["shubham"]["d"])

d3["ankit"] = "junk food"
d3["jhangya"] = "guuu"
print(d3)
del d3["jhangya"]
print(d3)