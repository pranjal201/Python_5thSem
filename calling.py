# TabNine::sem
import devices
from tabulate import tabulate
print(__name__)
if __name__ == "__main__":
    num = int(input())
    lappy = devices.create_laptops(num)
    print(tabulate(lappy, headers="keys"))
