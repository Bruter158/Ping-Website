import os
import platform

def ping_website(url):
    if platform.system().lower() == "windows":
        ping_cmd = f"ping -n 1 {url}"
    else:
        ping_cmd = f"ping -c 1 {url}"
    response = os.system(ping_cmd)
    if response == 0:
        print(f"{url} is UP!")
    else:
        print(f"{url} is DOWN!")

def display_menu():
    print("  ##############################")
    print("  #                            #")
    print("  #  Ali's Tool  #")
    print("  #                            #")
    print("  ##############################")
    print("  +---------------------------------------+")
    print("  |                Menu                  |")
    print("  +---------------------------------------+")
    print("  |  1. Ping Website                     |")
    print("  |  2. Exit                            |")
    print("  +---------------------------------------+")

def main():
    while True:
        display_menu()
        choice = input("  Enter your choice: ")
        if choice == "1":
            url = input("  Enter the website URL: ")
            ping_website(url)
        elif choice == "2":
            print("  Goodbye!")
            break
        else:
            print("  Invalid choice. Please try again.")

if __name__ == "__main__":
    main()