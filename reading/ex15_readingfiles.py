from sys import argv

script, filename = argv


print "Here's your file %r:" %filename
txt = open(filename)

print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.next()
print txt_again.tell()
#print txt_again.readlines()

txt_again.close()

