from django.urls import path
from .import views
from .views import StreamCreateView
from rest_framework.authtoken.views import obtain_auth_token #step8

urlpatterns = [

##############################################################################################################
#Step8: # for getting the token : 
# http://127.0.0.1:8000/api/api-token-auth/
    path('api-token-auth/', obtain_auth_token),
##########################################################################################################
    
#####################################################################################################################################
# End User Authentication
    # http://127.0.0.1:8000/api/end-user-auth/
    path('end-user-auth/', views.EndUser_Authentication.as_view()),
############################################################################################################################################

#####################################################################################################################################
# Admin User Authentication
    # http://127.0.0.1:8000/api/admin-user-auth/
    path('admin-user-auth/', views.AdminUser_Authentication.as_view()),
############################################################################################################################################

###############################################################################################################################################
# For adding a user to manager group
    # Pattern: http://127.0.0.1:8000/api/groups/manager/users/
    path('groups/manager/users/', views.managers),
############################################################################################################################################

# Stream Model:
###########################################################################################################    
# Url pattern to get the id
    # http://127.0.0.1:8000/api/streams/getid/
    path('streams/getid/', views.get_stream_id),

# URL pattern for creating a new stream
    # http://127.0.0.1:8000/api/streams/create/
   path('streams/create/', StreamCreateView.as_view(), name='stream-create'),

# URL pattern for retrieving streams
    # http://127.0.0.1:8000/api/streams/retrieve/
    path('streams/retrieve/', views.StreamRetrieveView.as_view()),

# URL pattern for updating a stream
    # http://127.0.0.1:8000/api/streams/1/update/
    path('streams/<int:pk>/update/', views.StreamUpdateView.as_view()),

# URL pattern for deleting a stream
    # http://127.0.0.1:8000/api/streams/1/delete/
    path('streams/<int:pk>/delete/', views.StreamDeleteView.as_view()),
###########################################################################################################

# Book Model
###########################################################################################################
    # URL pattern for inserting a book
    # http://127.0.0.1:8000/api/create/book/
    path('create/book/', views.BookCreateView.as_view()),

    # URL pattern for retrieving books
    # http://127.0.0.1:8000/api/retrieve/books/
    path('retrieve/books/', views.BookRetrieveView.as_view()),

    # URL pattern for updating a book by id
    # http://127.0.0.1:8000/api/book/1/update
    path('book/<int:pk>/update/', views.BookUpdateView.as_view()),

    # URL pattern for deleting a book by id
    # http://127.0.0.1:8000/api/book/3/delete
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view()),
#################################################################################################################

# Availability Model
####################################################################################################
    # URL pattern for inserting a book availability
    # http://127.0.0.1:8000/api/create/book/availability/
    path('create/book/availability/', views.AvailabilityCreateView.as_view()),

    # URL pattern for reading a book availability
    # http://127.0.0.1:8000/api/retrieve/book/availability/
    path('retrieve/book/availability/', views.AvailabilityRetriveView.as_view()),

    # URL pattern for updating a book availability by id
    # http://127.0.0.1:8000/api/book/1/availability/update
    path('book/<int:pk>/availability/update/', views.AvailabilityUpdateView.as_view()),

    # URL pattern for deleting a book availability by id
    # http://127.0.0.1:8000/api/book/2/availability/delete
    path('book/<int:pk>/availability/delete/', views.AvailabilityDeleteView.as_view()),
##############################################################################################

############################################################################################################
    # Pattern for fetching library books
    # http://127.0.0.1:8000/api/mycustomview/
    path('mycustomview/', views.MyCustomView.as_view()),
############################################################################################################
]

