# /management/commands/post_to_blog_command.py

from django.core.management.base import BaseCommand
import csv
from core.models import Phonenums  # importing Phonenums from models

class Command(BaseCommand):
    help = 'Export data to CSV'

    def handle(self, *args, **options):
        file_path = 'data_export.csv'  # Path to the CSV file

        # Fetch data from the database
        queryset = Phonenums.objects.all()

        # Write data to the CSV file
        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            #csv_writer.writerow(['Name', 'Phone', 'Email', 'Location'])  # Write header row
            for item in queryset:
                csv_writer.writerow([item.name, item.phone, item.email, item.location])  # Write data rows

       # writing to vcf
        input=list(csv.reader(open('data_export.csv','r'))) 
        output=open('contacts.vcf','a') 
        for row in input:
            output.write("BEGIN:VCARD\n") 
            output.write("VERSION:3.0\n")
            output.write("ADR:"+row[3]+""+"\n")
            output.write("EMAIL:"+row[2]+""+"\n")
            output.write("FN:"+row[0]+""+"\n") 
            output.write("N:"+row[0]+"\n") 
            output.write("TEL:"+row[1]+"\n") 
            output.write("END:VCARD\n") 
        output.close() 

        Phonenums.objects.all().delete() #Deletes the database after converting
        self.stdout.write(self.style.SUCCESS(f'Successfully exported data to {file_path}'))


# from django.core.management.base import BaseCommand
# from core.models import Post 
# import datetime

# class Command(BaseCommand):
#     help = 'Posts to the blog programmatically'

#     def handle(self, *args, **options):
#         # Your code to create a blog post programmatically
#         title = 'New Blog Post'
#         content = 'This is the content of the new blog post.'
#         pub_date = datetime.datetime.now()

#         # Create the blog post
#         blog_post = Post.objects.create(title=title, content=content, pub_date=pub_date)
#         blog_post.save()

#         self.stdout.write(self.style.SUCCESS('Successfully posted to the blog.'))