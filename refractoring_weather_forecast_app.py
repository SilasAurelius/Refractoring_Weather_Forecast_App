# Task 1: Identifying and Creating Classes Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

from user_interface import UserInterface

def main():
    user_interface = UserInterface()
    user_interface.run()

if __name__ == "__main__":
    main()
    
    
# I put the code across four modules to keep things neat and efficent. The modules are properly imported, encapsulated in classes, and the program is easy to use.