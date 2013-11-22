category_list = ["URL/Search Term Legend", "Appliances", "Auto", "Baby & Kids", "Computers", "Electronics", "Food", "Furniture", "Gift cards, tickets", "Hardware", "Health & Beauty", "Home & Decor", "Jewellery & Fashion", "Office Products", "Patio, Lawn and Garden", "Pet Supplies", "Sports & Fitness"]
print ""
print 'Which category needs updating? Please choose from the following: '
print "-" * 60
print '1 : "Appliances"'
print '2 : "Auto"'
print '3 : "Baby & Kids"'
print '4 : "Computers"'
print '5 : "Electronics"'
print '6 : "Food"'
print '7 : "Furniture"'
print '8 : "Gift cards, tickets"'
print '9: "Hardware"'
print '10 : "Health & Beauty"'
print '11 : "Home & Decor"'
print '12 : "Jewellery & Fashion"'
print '13 : "Office Products"'
print '14 : "Patio, Lawn and Garden"'
print '15 : "Pet Supplies"'
print '16 : "Sports & Fitness"'
print "-" * 60
print ""
selection = int(raw_input("Which cat do you want? > "))
selected = category_list[selection]
del category_list[selection]
print "you have chosen", selected
print category_list