from django.core.management.base import BaseCommand
from core.models import Post
import datetime

class Command(BaseCommand):
    help = 'Posts to the blog programmatically'

    def handle(self, *args, **options):

        #code to create a blog post programmatically
        title = 'Vcard for Sat Sep 16 2023'
        # slug = 
        # content = 'This is the content of the new blog post.'
        # pub_date = datetime.datetime.now()
        # is_locked = request.POST.get('is_locked') == 'on'
        
        # if is_locked:
        #     password = generate_random_password()
        # else:
        #     password = None
        author = 'Admin'


        # Create the blog post
        blog_post = Post.objects.create(title=title, author=author)
        blog_post.save()

        self.stdout.write(self.style.SUCCESS('Successfully posted to the blog.'))