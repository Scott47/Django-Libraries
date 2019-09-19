import sqlite3
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from libraryapp.models import Book
from libraryapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:

            conn.row_factory = model_factory(Book)

            db_cursor = conn.cursor()
            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)

            all_books = db_cursor.fetchall()

        template = 'books/list.html'
        context = {
            'all_books': all_books
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_book
            (
                title, author, isbn,
                year_published, location_id, librarian_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (form_data['title'], form_data['author'],
                form_data['isbn'], form_data['year_published'],
                request.user.librarian.id, form_data["location"]))

        return redirect(reverse('libraryapp:books'))


#creates list of book. Request is a single parameter to this view. This code only runs if someone makes a GET request.
# def book_list(request):
#     if request.method == 'GET':
#         with sqlite3.connect(Connection.db_path) as conn:
#             conn.row_factory = sqlite3.Row
#             db_cursor = conn.cursor()

#queries all of the columns from book table.
            # db_cursor.execute("""
            # select
            #     b.id,
            #     b.title,
            #     b.isbn,
            #     b.author,
            #     b.year_published,
            #     b.librarian_id,
            #     b.location_id
            # from libraryapp_book b
            # """)

            # all_books = []
            # dataset = db_cursor.fetchall()

#iterating over list of tuples in book model, creates an instance of book based upon the columns that match the properties on the book.
#.row is a method that
            # for row in dataset:
            #     book = Book()
            #     book.id = row['id']
            #     book.title = row['title']
            #     book.isbn = row['isbn']
            #     book.author = row['author']
            #     book.year_published = row['year_published']
            #     book.librarian_id = row['librarian_id']
            #     book.location_id = row['location_id']

#adds books to the empty list created above.
                # all_books.append(book)

#When a view wants to generate some HTML representations of data, it needs to specify a template to use. Above, the template variable is holding the path and filename of the template you just created.

        # template = 'books/list.html'
        # context = {
        #     'all_books': all_books
        # }

# Then the render() method is invoked. That method takes the HTTP request as the first argument, the template to be used as the second argument, and then a dictionary containing the data to be used in the template.
        # return render(request, template, context)