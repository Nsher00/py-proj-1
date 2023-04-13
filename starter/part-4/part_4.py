### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def new_book():
#     new_title = input('What is the name of the book you want to add?')
#     new_author = input('What is the name of the author of the book?')
#     new_year = input('What year was the book published?')
#     new_rating = input('What is the rating of this book?')
#     new_pages = input('How many pages are in the book?')

#     book_dictionary = {
#         'title': new_title,
#         'author': new_author,
#         'year': new_year,
#         'rating': new_rating,
#         'pages': new_pages
#     }

#     return book_dictionary



### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def new_book():
#     new_title = input('What is the name of the book you want to add?')
#     new_author = input('What is the name of the author of the book?')
#     new_year = int(input('What year was the book published?'))
#     new_rating = float(input('What is the rating of this book?'))
#     new_pages = int(input('How many pages are in the book?'))

#     book_dictionary = {
#         'title': new_title,
#         'author': new_author,
#         'year': new_year,
#         'rating': new_rating,
#         'pages': new_pages
#     }

#     return book_dictionary

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def new_book():
    new_title = input('What is the name of the book you want to add?')
    new_author = input('What is the name of the author of the book?')
    try:
        new_year = int(input('What year was the book published?'))
    except:
        new_year = int(input('Please enter a number for the year?'))
    try:
        new_rating = float(input('What is the rating of this book?'))
    except:
        new_rating = float(input('Please enter a number out of five for the rating'))
    try:
        new_pages = int(input('How many pages are in the book?'))
    except:
        new_pages = int(input('Enter a number for the amount of pages in the book.'))

    book_dictionary = {
        'title': new_title,
        'author': new_author,
        'year': new_year,
        'rating': new_rating,
        'pages': new_pages
    }

    return book_dictionary

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

def main_menu():
    print('Menu:\n 1: Create a new entry\n 2: Delete a book\n 3: View all books\n')
    try:
        navigation = input('What would you like to do?')
    except:
        navigation = input('Please enter a number for what you would like to do.')
    if navigation == 1:
        new_book()


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
is_idle = True
while is_idle == True:
    is_idle = False
    main_menu()