# #print 1 to 10
#
# """
# l = range(1,100)
# #y = [el**2 for el in l]
# y=[el for el in l if el%2]
# print (y)
#
#
#     fruits = ["apple", "banana", "kiwi", "orange"]
#     formatted_fruits = ["Apple", "Banana", "Kiwi", "Orange"]
# """
#
#
fruits = ["kiwi" ,"wwwww" , "banana", "orange" , "apple"]
#
# formatted_fruits = [k.capitalize() for k in fruits]
# formatted_fruits2 = [j.upper() for j in fruits]
# print(formatted_fruits)
# print(formatted_fruits2)
#
#
#
#fruits2 = [len(x) for x in fruits]
#print(fruits2)
#print(max(fruits2))
#
#
# print(len(fruits2))
# print(len(fruits))
#print(sorted( reversed(fruits) ))
#
#
# """
#   strings
#   numbers
#   booleans
#   lists
#   tuples
#   sets
#   dictionaries
#   loops
# """
#
#
a = ["a", "b", "c", "b", "c", "b", "c","d"]
# #     1    3    3                       1
#
count_el = {}
#
#for el in a:
#    if el not in count_el:
#         count_el[el] = 1
#    else :
#         count_el[el] += 1
#
#
#print(count_el)
#
#

t = [
         ["Name", "Age", "Company"],
         ["J", 21, "3PG"],
         ["G", 33, "3PG"],
         ["F", 44, "3PG"]
 ]

for row in t:
    print(row)
for col in row:
    print(col)

# """
# for (var i = 0; i<t.length; i++) {
#   var thisRow = t[i];
#   for (var j = 0; j<thisRow.length; j++) {
#     var thisCol = thisRow[j];
#     console.log(thisCol);
#   }
# }
# """

d = {"Adelin": 2, "Madalina": 1}

# Cheia Adelin are valoarea 2
# Cheia Madalina are valoarea 1

for key in d:
    print("cheia " + key + " are valoarea " + str(d[key]))


#selenium


