from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from hello.models import Item, ItemFeatures


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def item_view(request, item_id):
    if request.method == 'GET':
        item_info = Item.objects.get(pk=item_id)
        item_list = ItemFeatures.objects.get(fk=item_id)
        return render(request, 'item_pages/single_item.html', {'item': item_info, 'details': item_list})
