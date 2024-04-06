import os

def main():
    while True:
        x = int(input("Enter the width of the object: "))
        y = int(input("Enter the height of the object: "))

        if x != y:
            print("Error: Width and height must be equal. Please re-enter.")
            continue  # Restart the loop to re-enter dimensions

        if x < 10 and y < 10:
            os.system("python3 donut_code.py")
        elif x >= 100 or y >= 100:
            os.system("python3 loop_inside.py")
        elif 10 <= x < 50 and 10 <= y < 50:
            os.system("python3 donut.py")
        elif 50 <= x < 100 and 50 <= y < 100:
            os.system("python3 ring.py")
        else:
            print("Dimensions do not fall into any category.")

        break  # Exit the loop if dimensions are valid

if __name__ == "__main__":
    main()
