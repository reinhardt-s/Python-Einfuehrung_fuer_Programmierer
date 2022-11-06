my_name = "Hermoine Granger"

def who_am_i_this_time():
    print(my_name)


def who_am_i(my_name):
    print(my_name)

def who_is_this():
    my_name = "Cho Chang"
    print(my_name)

def i_am_ron():
    my_name = "Ron Weasly"
    print(my_name)


def who_am_i_now():
    global my_name
    print(my_name)
    my_name = "Draco Malfoy"


def names():
    name_1 = "Bill Weasly"
    name_2 = "Charlie Weasly"
    name_3 = "Percy Weasly"

#print(my_name)
# who_am_i_this_time()
# who_am_i("Neville Longbottom")

# who_is_this()
# print(my_name)

# i_am_ron()
# print(my_name)

# who_am_i_now()
# print(my_name)

# print(name_2)


# no block scopes
if 3 > 2:
    print("Mister Potter!")
    fear = 3
print(fear)

SCHULLEITER = "Dumbledore"

print(SCHULLEITER)
SCHULLEITER = "Umbridge"
print(SCHULLEITER)

