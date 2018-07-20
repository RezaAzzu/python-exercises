tabby_cat    = "\tI'm tabbed in."
persian_cat  = "I'm split\non a line."
backslash_cat= "I'm \\ a \\ cat."

fat_cat = '''
"I'll do a list:"
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

test1 = "haha\'\'\""

#tes mbandingin nyetak biasa dengan format %r
print test1
print "%r" %test1

while True:
    for i in ["/", "-", "|", "\\", "|"]:
            print "%s\r" %i,
