Create:

> > > book = Book.objects.create( title="1984", author="George Orwell", publication_year=1949)
> > > book
> > > <Book: 1984 by George Orwell (1949)>

Retrieve:

> > > book = Book.objects.get(title="1984")

Update:

> > > book.title = "Nineteen Eighty-Four"

Delete:

> > > from bookshelf.models import Book
> > > book.delete
> > > <bound method Model.delete of <Book: 1984 by George Orwell (1949)>>
