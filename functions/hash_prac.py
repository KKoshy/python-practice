"""
This file holds the practice on using hash function
"""

def create_file(name, content):
    with open(name, "w+") as f:
        f.write(content)


# hash function returns an integer hash value for a given object
# hash value of an object acts as a digital fingerprint for the object.
def compare_files(file_01, file_02):
    with open(file_01, "r") as f1, open(file_02, "r") as f2:
        if hash(f1.read()) == hash(f2.read()):
            print("Files have the same content")
        else:
            print("Files have different content")


if __name__=="__main__":
    content = "1.Alex\n2.Bob\n3.Cassandra"
    print(f"Creating file-01 with the content: {content}")
    create_file("file-01.txt", content)
    print(f"Creating file-02 with the content: {content}")
    create_file("file-02.txt", content)
    print("Comparing file content with hash function")
    compare_files("file-01.txt", "file-02.txt")
