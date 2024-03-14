#Write a function translate() that will translate a text into "rövarspråket"
# (Swedish for "robber's language"). That is, double every consonant and place an
# occurrence of "o" in between. For example, translate("this is fun") should return
# the string "tothohisos isos fofunon".

def translate():
    str1 = "this is fun"
    for i in str1:
        if i == ' ':
            print(i,end=" ")
        else:
            print(f"{i}o{i}",end="")

translate()