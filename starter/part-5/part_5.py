### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

def new_book():
    new_title = input('What is the name of the book you want to add?')
    new_author = input('What is the name of the author of the book?')
    try:
        new_year = int(input('What year was the book published? '))
    except:
        new_year = int(input('Please enter a number for the year? '))
    try:
        new_rating = float(input('What is the rating of this book? '))
    except:
        new_rating = float(input('Please enter a number out of five for the rating '))
    try:
        new_pages = int(input('How many pages are in the book? '))
    except:
        new_pages = int(input('Enter a number for the amount of pages in the book. '))


    with open ("library.txt", 'a') as f:
        f.write(f'{new_title}, {new_author}, {new_year}, {new_rating}, {new_pages}\n')

def open_library():
    with open('library.txt', 'r') as f:
        file = f.readlines()

    for line in file:
        new_title, new_author, new_year, new_rating, new_pages = line.split(', ')

        book_dictionary = {
            'title': new_title,
            'author': new_author,
            'year': int(new_year),
            'rating': float(new_rating),
            'pages': int(new_pages)
        }
        print(book_dictionary)

def remove_book():
    with open('library.txt', 'r') as f:
        file = f.readlines()
        deleteLine = int(input("Enter the book number to be deleted: "))
        line_index = 1
        with open ("library.txt", 'w') as f:
            for line in file:
                if line_index != deleteLine:
                    f.write(line)
                line_index += 1
    print(f'Book was deleted.')

    



def main_menu():
    print('Menu:\n 1: Create a new entry\n 2: View all books\n 3: Delete book\n')
    try:
        navigation = input('What would you like to do?')
    except:
        navigation = input('Please enter a number for what you would like to do.')
    if navigation == '1':
        new_book()
    elif navigation == '2':
        open_library()
    elif navigation == '3':
        remove_book()




### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


if __name__ == "__main__":
    main_menu()