my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_info(book):
    for item in book:
        print(item+':', book[0])
    


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def grab_title(book):
    title = []
    for key, value in my_book.items():
        title.append(key+':'+value)
    return title[0]

def grab_authore(book):
    author = []
    for key, value in my_book.items():
        author.append(key+':'+value)
    return author[1]

def grab_year(book):
    year = []
    for key, value in my_book.items():
        year.append(key+':'+value)
    return year[2]

def grab_rating(book):
    rating = []
    for key, value in my_book.items():
        rating.append(key+':'+value)
    return rating[3]

def grab_pagese(book):
    pages = []
    for key, value in my_book.items():
        pages.append(key+':'+value)
    return pages[4]
    


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

# Gets all the books that start with a certain letter
    def search_alph(input,book):
        if book['title'][0].lower == input:
            return book['title']
        
# Gets books based on their length
    def search_length(input,book):
        if book['pages'] >= input:
            return (book['title'], book['pages'])

#this function returns all the books with a certain rating the user specifices

    def get_ratings(input,book):
        if book['rating'] >= input:
            return(book['title'], book['rating'])
