from django.conf.urls import url, include
from .views import *

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^books$', book_list, name='books'),
    url(r'^book/form$', book_form, name='book_form'),
    url(r'^books/(?P<book_id>[0-9]+)/$', book_details, name="book"),
    url(r'^librarians$', list_librarians, name='librarians'),
    url(r'^libraries$', library_list, name='libraries'),
    url(r'^library/form$', library_form, name='library_form'),
    url(r'^libraries/(?P<library_id>[0-9]+)/$', library_details, name="library"),
    url(r'^logout/$', logout_user, name='logout'),
]