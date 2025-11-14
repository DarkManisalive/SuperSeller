import random

def main():
    Name=""
    for i in range(16):
        Name += chr(random.randint(65, 90))  # Generate a random uppercase letter
        if i >= 5:
            Name += chr(random.randint(48, 57))  # Generate a random digit

if __name__ == '__main__':
    main()
