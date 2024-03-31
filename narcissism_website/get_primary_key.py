# Import necessary modules
from django.db import models
from content_management.models import Content

# Replace 'myapp' with the name of your Django app

# Get the primary key field for the Source model
primary_key_field = Content._meta.get_field(Content._meta.pk.name)

# Print the name of the primary key field
print(primary_key_field.name)
