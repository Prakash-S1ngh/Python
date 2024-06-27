# f= open('myfile.txt','w')
# f.write("hello Prakash Kumar Singh , Long time no see ")
# f.write("looking Handsome were you really this looking will you fuck my ass ")
# # f.close()

# f=open('myfile.txt','r')
# print(f.read())
# f.close()

# Readline(),writeline()

# Writing to the file
f = open('myfile.txt', 'w')
f.write("Looking Handsome, were you really this good looking last year\n")
f.write("God it's hot in here, maybe I should get naked, but will you fuck my ass, please\n")
f.close()

# Reading from the file
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line.strip())  # Print the line without the newline character
f.close()


with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.")

