from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from core.models import Phonenums
from .models import Post
# Free package page index

def index(request):
    
    if request.method == "POST":
        data=request.POST
        name=data['name']
        phone=data['phone']

        Phonenums.objects.create(
            name=name,
            phone=phone
        )

        print(name)
        print(phone)

        print('Successfully submitted your contact')
        
        if request.method == "POST":

            messages.success(request, 'messages.html')

        # with open('test.vcf', 'a', newline='') as f: 
        #     f.write(data.serialize())
            return HttpResponseRedirect('/contacts/', {'data': data})


    return render(request, 'index.html')


# Premium package page

def premium(request):
    if request.method == "POST":
        data=request.POST
        name=data['name']
        phone=data['phone']
        email=data['email']
        state=data['state']
        
        Phonenums.objects.create(
            name=name,
            phone=phone,
            email=email,
            location=state
        )

        print(name)
        print(phone)
        print(email)
        print(state)

        if request.method == "POST":
            messages.success(request, 'messages.html')

        # with open('test.vcf', 'a', newline='') as f: 
        #     f.write(data.serialize())
            return HttpResponseRedirect('/contacts/', {'data': data })


    return render(request, 'premium.html')


#  Archive page

def archive(request):
    posts = Post.published.all()
    return render(request, 'archive.html', {'posts' : posts})

# Downloads page

def downloads(request, slug, id):
    blog_post = Post.objects.get(id=id)

    if blog_post.is_locked:
        if request.method == 'POST':
            entered_password = request.POST.get('passwords')
            if entered_password == blog_post.password:
                blog_post.is_locked = False
                blog_post.save()
        
    id = get_object_or_404(Post,id=id,status='published')
    return render(request, 'downloads.html',{'post': blog_post})

# Contacts page

def contacts(request):
    # contact = get_object_or_404(Post,success=contact,status='published')

    return render(request, 'contacts.html')