print("File __name__ = %s\n" % __name__)

if __name__ == "__main__":
    print("File1 script is being used directly")
else:
    print("File1 is being imported")


num = int(input())
print(num+1)
