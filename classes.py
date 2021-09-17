class myClass():
    def method1(self):
        print("my class")

    def method2(self, somestring):
        print("my method"+somestring)


def main():
    c = myClass()
    c.method1()
    c.method2("another")


if __name__ == "__main__":
    main()
