from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you do'nt want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#target.truncate() //gak perlu di-truncate sebenarnyah 

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#isi = line1 + "\n" + line2 + "\n" + line3 + "\n"
isi = "%s\n%s\n%s\n" %(line1,line2,line3)
target.write(isi)

print "And finally, we close it."
target.close()
