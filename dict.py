#Dictionary - used to store values in key:value pairs 
# myDictionary = {
    # "name" : "Srikaran",
    # "age" : 18
# }
# print(myDictionary)
#Dictionary are ordered
#Dictionary mutable or changable
# it doesn't allow duplicate values
#print(myDictionary.get("age")) #through get we can get that element we want
#print(myDictionary.keys or .values) #we can get all the keys in the dictionary
#items = myDictionary.items()
# myDictionary["roll number"] = 11
# myDictionary["age"] = 33
# myDictionary.update({"age":33})
# print(myDictionary)

# dict1={"one":1 , "two":2 , "three":3}
# dict2={"four":4 , "five":5 , "six":6}
# dict1.update(dict2)
# print(dict1)

dict1 = {
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }    
    }    
}
print(dict1.get("class").get("student").get("marks").get("web"))

