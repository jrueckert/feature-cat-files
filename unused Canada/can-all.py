import gspread
import getpass
import datetime
import sys
import codecs
import re

from collections import OrderedDict
from django.template import Template, Context
from django.conf import settings


def usernam(name):
    if name == "jr":
        user = "jrueckert@costco.com"
    elif name == "ci":
        user = "cicichen@costco.com"
    elif name == "jg":
        user = "jguzman@costco.com"
    elif name == "gj":
        user = "gjacobson@costco.com"
    return user




username = usernam(raw_input("What's your name? "))
password = getpass.getpass()

success = "MISSION: Accomplished."

def pick_country(country):
	if country == 1:
		print "You selected U.S. of A!"
		selected_us()

	elif country == 2:
		print "You selected Canada, eh?"
		selected_can()
	else:
		print "Try again." 

def selected_us():
	print "Which script would you like to execute (select a number):"
	print "1: Next Week"
	print "2: This Week" 
	print "3: Single Category on a Specific Day"
	print "-" * 62
	selected_script = (int(raw_input(prompt)))
	if selected_script == 1:
		next_week_us()
	elif selected_script == 2:
		this_week_us()
	elif selected_script == 3:
		single_category_us()

def selected_can():
	print "Which script would you like to execute (select a number):"
	print "1: Next Week"
	print "2: This Week" 
	print "3: Single Category on a Specific Day"
	print "-" * 62
	selected_script = (int(raw_input(prompt)))
	if selected_script == 1:
		next_week_can()
	elif selected_script == 2:
		this_week_can()
	elif selected_script == 3:
		single_category_can()


def single_category_us():
	pass

def next_week_us():
	pass

def this_week_us():
	pass

def single_category_can():

    spread_sheet = "FY14 CANADA Category Hero-Features"


    """This is the full list of category tabs on the google doc spreadsheet"""
    category_list = ["URL/Search Term Legend", "Appliances", "Auto", "Baby & Kids", "Computers", "Electronics", "Food", "Furniture", "Gift cards, tickets", "Hardware", "Health & Beauty", "Home & Decor", "Jewellery & Fashion", "Office Products", "Patio, Lawn and Garden", "Pet Supplies", "Sports & Fitness"]
    print ""
    print 'Which day of the week is this for? Please choose from the following: '
    print "-" * 60
    print "This week:" 
    print ' 0 : "Monday"'
    print ' 1 : "Tuesday"'
    print ' 2 : "Wednesday"'
    print ' 3 : "Thursday"'
    print ' 4 : "Friday"'
    print ' 5 : "Saturday"'
    print ' 6 : "Sunday"'
    print ""
    print "Next week:" 
    print ' 7 : "Monday"'
    print ' 8 : "Tuesday"'
    print ' 9 : "Wednesday"'
    print '10 : "Thursday"'
    print '11 : "Friday"'
    print '12 : "Saturday"'
    print '13 : "Sunday"'
    print "-" * 60
    print ""
    day_selection = int(raw_input("==> "))

    print ""
    print 'Which category needs updating? Please choose from the following: '
    print "-" * 60
    print ' 1 : "Appliances"'
    print ' 2 : "Auto"'
    print ' 3 : "Baby & Kids"'
    print ' 4 : "Computers"'
    print ' 5 : "Electronics"'
    print ' 6 : "Food"'
    print ' 7 : "Furniture"'
    print ' 8 : "Gift cards, tickets"'
    print ' 9 : "Hardware"'
    print '10 : "Health & Beauty"'
    print '11 : "Home & Decor"'
    print '12 : "Jewellery & Fashion"'
    print '13 : "Office Products"'
    print '14 : "Patio, Lawn and Garden"'
    print '15 : "Pet Supplies"'
    print '16 : "Sports & Fitness"'
    print "-" * 60
    print ""
    selection = int(raw_input("==> "))
    selected = category_list[selection]
    del category_list[selection]
    print "you have chosen", selected


    skipped_list = category_list
    prop_col = ("hero english text", "hero french text", "hero en link/search", "hero fr link/search", "en file name","fr file name", "feature 1 english text", "feature 1 french text","feature 1 en link/search", "feature 1 fr link/search", "feature 2 english text", "feature 2 french text", "feature 2 en link/search", "feature 2 fr link/search")
    template_name = 'tmp.html'


    days_ahead = 0 - datetime.date.today().weekday()
    if days_ahead <= 0:
        days_ahead += day_selection
    next_monday = datetime.date.today() + datetime.timedelta(days_ahead)
    date_row = next_monday.strftime("%-m/%-d/%Y")
    print "next monday is", date_row
    data = OrderedDict({})

    print "login as", username
    print "open spread sheet", spread_sheet
    for worksheet in gspread.login(username, password).open(spread_sheet).worksheets():
        title = worksheet.title
        title = title.lstrip()
        title = title.rstrip()
        if not title in skipped_list:
            print "reading worksheet", title, "..."

            read_col_list = []
            col = 1
            for value in worksheet.row_values(3):
                if not value is None:
                    value.lstrip()
                    value.rstrip()
                    if value.lower().startswith(prop_col):
                        read_col_list.append(col)
                col += 1
            if not len(read_col_list) == 18:
                print "invalid column data on worksheet", title
                sys.exit(1)

            read_row = -1
            row = 1
            for value in worksheet.col_values(1):
                if not value is None:
                    value.lstrip()
                    value.rstrip()
                    if value == date_row:
                        read_row = row
                        # print value
                row += 1
            if read_row == -1:
                print "invalid row data on worksheet", title
                sys.exit(1)

            line = []
            col = 1
            value_list = worksheet.row_values(read_row)
            for read_col in read_col_list:
                value = value_list[read_col-1]
                # print value
                if not value is None:
                    value.lstrip()
                    value.rstrip()
                else:
                    value = 'TBD'
                if col%3 == 0:
                    if re.match("^[0-9]+$", value):
                        value = "/.product.{0}.html".format(value)
                    elif re.match("^[a-zA-Z]+[0-9]+$", value) or re.match("^[a-zA-Z]+$", value):
                        value = "/CatalogSearch?langId=-1&storeId=10301&catalogId=10701&keyword={0}&sortBy=PriceMax%7C1".format(value)

                line.append(value)
                col += 1
            key = 'cat-'
            key += title.lower().replace(' ', '-').replace('&', '').replace(',', '-').replace('/', '-')
            key += '-hero-'
            key += next_monday.strftime("%y%m%d")
            data[key] = line

    output_name = '%s-%s.html' % (selected.lower(), next_monday.strftime("%y%m%d"))

    settings.configure()
    print "reading template from", template_name, "..."
    template_file = open(template_name, "r").read()
    output_file = codecs.open(output_name, mode="w", encoding='utf-8')
    print "filling data into", output_name, "..."
    template = Template(template_file)
    content = template.render(Context({'data': data}))
    output_file.write(content)
    print success 
    sys.exit(0)

def next_week_can():
	spread_sheet = "FY14 CANADA Category Hero-Features"
	skipped_list = ["URL/Search Term Legend"]
	prop_col = ("hero english text", "hero french text", "hero en link/search", "hero fr link/search", "en file name","fr file name", "feature 1 english text", "feature 1 french text","feature 1 en link/search", "feature 1 fr link/search", "feature 2 english text", "feature 2 french text", "feature 2 en link/search", "feature 2 fr link/search")
	template_name = 'tmp.html'
	

	days_ahead = 0 - datetime.date.today().weekday()
	if days_ahead <= 0:
	    days_ahead += 7
	next_monday = datetime.date.today() + datetime.timedelta(days_ahead)
	date_row = next_monday.strftime("%-m/%-d/%Y")
	print "next monday is", date_row
	data = OrderedDict({})

	print "login as", username
	print "open spread sheet", spread_sheet
	for worksheet in gspread.login(username, password).open(spread_sheet).worksheets():
	    title = worksheet.title
	    title = title.lstrip()
	    title = title.rstrip()
	    if not title in skipped_list:
	        print "reading worksheet", title, "..."

	        read_col_list = []
	        col = 1
	        for value in worksheet.row_values(3):
	            if not value is None:
	                value.lstrip()
	                value.rstrip()
	                if value.lower().startswith(prop_col):
	                    read_col_list.append(col)
	            col += 1
	            # print read_col_list
	        if not len(read_col_list) == 18:
	            print "invalid column data on worksheet", title
	            sys.exit(1)

	        read_row = -1
	        row = 1
	        for value in worksheet.col_values(1):
	            if not value is None:
	                value.lstrip()
	                value.rstrip()
	                if value == date_row:
	                    read_row = row
	            row += 1
	        if read_row == -1:
	            print "invalid row data on worksheet", title
	            sys.exit(1)

	        line = []
	        col = 1
	        value_list = worksheet.row_values(read_row)
	        for read_col in read_col_list:
	            value = value_list[read_col-1]
	            if not value is None:
	                value.lstrip()
	                value.rstrip()
	            else:
	                value = 'TBD'
	            if col%3 == 0:
	                if re.match("^[0-9]+$", value):
	                    value = "/.product.{0}.html".format(value)
	                elif re.match("^[a-zA-Z]+[0-9]+$", value) or re.match("^[a-zA-Z]+$", value):
	                    value = "/CatalogSearch?langId=-1&storeId=10301&catalogId=10701&keyword={0}&sortBy=PriceMax%7C1".format(value)

	            line.append(value)
	            col += 1
	        key = 'cat-'
	        key += title.lower().replace(' ', '-').replace('&', '').replace(',', '-').replace('/', '-')
	        key += '-hero-'
	        key += next_monday.strftime("%y%m%d")
	        data[key] = line

	output_name = 'can-%s.html' % next_monday.strftime("%y%m%d")
	settings.configure()
	print "reading template from", template_name, "..."
	template_file = open(template_name, "r").read()
	output_file = codecs.open(output_name, mode="w", encoding='utf-8')
	print "filling data into", output_name, "..."
	template = Template(template_file)
	content = template.render(Context({'data': data}))
	output_file.write(content)
	print success
	sys.exit(0)

def this_week_can():
    spread_sheet = "FY14 CANADA Category Hero-Features"
    skipped_list = ["URL/Search Term Legend"]
    prop_col = ("hero english text", "hero french text", "hero en link/search", "hero fr link/search", "en file name","fr file name", "feature 1 english text", "feature 1 french text","feature 1 en link/search", "feature 1 fr link/search", "feature 2 english text", "feature 2 french text", "feature 2 en link/search", "feature 2 fr link/search")
    template_name = 'tmp.html'
    output_name = 'main.html'

    days_ahead = 0 - datetime.date.today().weekday()
    if days_ahead <= 0:
        days_ahead += 0
    next_monday = datetime.date.today() + datetime.timedelta(days_ahead)
    date_row = next_monday.strftime("%-m/%-d/%Y")
    print "This week's Monday was", date_row
    data = OrderedDict({})

    print "login as", username
    print "open spread sheet", spread_sheet
    for worksheet in gspread.login(username, password).open(spread_sheet).worksheets():
        title = worksheet.title
        title = title.lstrip()
        title = title.rstrip()
        if not title in skipped_list:
            print "reading worksheet", title, "..."

            read_col_list = []
            col = 1
            for value in worksheet.row_values(3):
                if not value is None:
                    value.lstrip()
                    value.rstrip()
                    if value.lower().startswith(prop_col):
                        read_col_list.append(col)
                col += 1
                # print read_col_list
            if not len(read_col_list) == 18:
                print "invalid column data on worksheet", title
                sys.exit(1)

            read_row = -1
            row = 1
            for value in worksheet.col_values(1):
                if not value is None:
                    value.lstrip()
                    value.rstrip()
                    if value == date_row:
                        read_row = row
                row += 1
            if read_row == -1:
                print "invalid row data on worksheet", title
                sys.exit(1)

            line = []
            col = 1
            value_list = worksheet.row_values(read_row)
            for read_col in read_col_list:
                value = value_list[read_col-1]
                if not value is None:
                    value.lstrip()
                    value.rstrip()
                else:
                    value = 'TBD'
                if col%3 == 0:
                    if re.match("^[0-9]+$", value):
                        value = "/.product.{0}.html".format(value)
                    elif re.match("^[a-zA-Z]+[0-9]+$", value) or re.match("^[a-zA-Z]+$", value):
                        value = "/CatalogSearch?langId=-1&storeId=10301&catalogId=10701&keyword={0}&sortBy=PriceMax%7C1".format(value)

                line.append(value)
                col += 1
            key = 'cat-'
            key += title.lower().replace(' ', '-').replace('&', '').replace(',', '-').replace('/', '-')
            key += '-hero-'
            key += next_monday.strftime("%y%m%d")
            data[key] = line


    settings.configure()
    print "reading template from", template_name, "..."
    template_file = open(template_name, "r").read()
    output_file = codecs.open(output_name, mode="w", encoding='utf-8')
    print "filling data into", output_name, "..."
    template = Template(template_file)
    content = template.render(Context({'data': data}))
    output_file.write(content)
    print success
    sys.exit(0)

prompt = '==> '

print "-" * 62 
print "*********  Welcome to the Future of Automation  **************" 
print "Which country is this for? Please choose one of the following:"
print "       [ For the US, ENTER '1', for Canada, ENTER '2' ]"
print "-" * 62
pick_country(int(raw_input(prompt)))