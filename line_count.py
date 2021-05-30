import sys

if len(sys.argv) == 2:
    line_count = int(sys.argv[1])
else:
    line_count = 100

file_name = f"line_count_{line_count}.txt"

file_out = open(file_name, "w")

for i in range(line_count):
    message = "line " + str(i+1)
    print(message)
    file_out.write(message + "\n")

file_out.close()


