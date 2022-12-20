from django.db import migrations

from users.initial_user_data import gen_user
from books.initial_book_data import gen_book

class Migration(migrations.Migration):
    initial = True
    dependencies = [
    
    ]
    operations = [
        migrations.RunPython(gen_user),
        migrations.RunPython(gen_book),
    ]