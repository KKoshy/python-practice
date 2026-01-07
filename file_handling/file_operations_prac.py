"""
This file holds the practice on file operations
"""
with open("second.txt", "w+") as f:
    fin = f.write("The second file\n")
    f.writelines(["Curiosity\n", "kills\n", "the\n", "Cat\n"])

print(f"write output: {fin}")

# file first.txt exists
with open("first.txt", "r") as f:
    print(f"printing the file object: {__file__} of type {type(__file__)}")
    content = f.readline()    
    content_lines = f.readlines()

# handling 2 files at once
with open("first.txt", "r") as reader, open("third.txt", "w") as writer:
    text = reader.readlines()
    text.reverse()
    if text:
        writer.writelines(text)
    else:
        writer.write("Notextfound")


print(content_lines)
print(content)
