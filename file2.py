import file1

print("File2 __name__ = %s" % __name__)

if __name__ == "__main__":
    print("File2 script is being executed")
else:
    print("File2 is being imported")
