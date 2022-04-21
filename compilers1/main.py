#def user_in(sentinel = ''):
#    for inp in iter(input, sentinel):
#        yield inp.split()

"""
Assumptions
-- whitespace = UNICODE whitespace characters which include [ \t\n\r\f\v]
-- Assignment operator will be ":=" (no whitespace between).
-- Assign op does not need spaces before or after to be recognized.
-- Semicolon does not need whitespace before or after. (expressions can be concat in a single line).
-- Input can be multiline, and this is ignored as well as multiple spaces.
-- ID consists of one letter at least, then letter or number or _ or - only.
-- Comments in TINY language not accounted for.
"""

import re
from pprint import pprint
from nltk.tokenize import regexp_tokenize

#example input
"""
if @mxf$ 0 then
y := 5 ;
else x := 5;
end;
ok1 := 50;
ok_2 := 3102.25;
ok_3:= -4.0 ;;
not_ok :=-4?
count-1;ok_4 := -2;
"""


def user_in():  #function to get multiline input from user, return a list (element = 1 line)
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    return contents


def prep_str(lis): #function to prepare string for tokenization
    my_string = ' '.join(lis) #join lines with spaces
    my_string = my_string.replace(";", " ; ") #any semicolon will have space before and after
    my_string = my_string.replace(":=", " := ") #any semicolon will have space before and after
    return my_string


def tokenize(my_string): #function to return token stream
    my_pattern = re.compile(r"\S+") #matching any sequence of non-whitespaces
    matches = my_pattern.findall(my_string)
    #for match in matches:
    #    print(match)

    #my_pattern = r"([a-zA-Z]+[a-zA-Z0-9_-]*|:=|;|[0-9.0-9]+|[0-9]+)"
    #my_pattern = (r"\S+")
    #lis = regexp_tokenize(my_string, my_pattern)
    #print("INPUT STRING: ")
    #print(lis)

    token_type_list = []
    for attr in matches:
        #match each attribute to its token type and output the token in angled brackets
        if attr.lower() == "if":
            print("<" + attr + ", "+ "IF>")
            token_type_list.append("IF")
            continue
        elif attr.lower() == "then":
            print("<" + attr + ", " + "THEN>")
            token_type_list.append("THEN")
            continue
        elif attr.lower() == "end":
            print("<" + attr + ", " + "END>")
            token_type_list.append("END")
            continue
        elif attr.lower() == "else":
            print("<" + attr + ", " + "ELSE>")
            token_type_list.append("ELSE")
            continue
        elif attr == ":=":
            print("<" + attr + ", " + "ASSIGN>")
            token_type_list.append("ASSIGN")
            continue
        elif attr == ";":
            print("<" + attr + ", " + "SEMICOLON>")
            token_type_list.append("SEMICOLON")
            continue
        elif re.fullmatch(r"-?[0-9]+|-?[0-9]+.[0-9]+", attr):
            print("<" + attr + ", " + "NUM>")
            token_type_list.append("NUM")
            continue
        elif re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_-]*", attr):
            print("<" + attr + ", " + "ID>")
            token_type_list.append("ID")
        else: #unidentifiable token
            print("<"+ attr + ", " + "UNIDENTIFIABLE>")
            token_type_list.append("UNIDENTIFIABLE")
    #print("\n--done tokenization--")
    #print("\nTOKEN_LIST: ")
    #print(token_type_list)
    return token_type_list


#main
#step 1: TINY language input
print("To terminate input, press Enter then Ctrl + D")
lis = user_in()

#step 2: input to charstream
my_string = prep_str(lis)
#print("INPUT STRING: " + my_string)

#step 3: tokenize charstream
token_type_list = tokenize(my_string) #function to output token stream

#now, we have the sequence of token types. we will trace the types in dfa