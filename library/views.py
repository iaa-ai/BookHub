from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from .forms import *
class HomeView(LoginRequiredMixin,ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'home'
    paginate_by = 10
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class BookListView(LoginRequiredMixin,ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'
    paginate_by = 10
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(title__icontains=q)
        return queryset

class UserInfoListView(LoginRequiredMixin,ListView):
    model = Member
    template_name = 'user_info.html'  
    context_object_name = 'authors'
    paginate_by = 10
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class AuthorListView(LoginRequiredMixin,ListView):
    model = Author
    template_name = 'authors.html'  
    context_object_name = 'authors'
    paginate_by = 10
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(name__icontains=q)
        return queryset

class MemberListView(LoginRequiredMixin,ListView):
    model = Member
    template_name = 'members.html'  
    context_object_name = 'members'
    paginate_by = 10
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class BookInstanceListView(LoginRequiredMixin,ListView):
    model = BookInstance
    template_name = 'bookinstances.html'
    context_object_name = 'bookinstances'
    paginate_by = 10
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(book__title__icontains=q)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class UserListView(LoginRequiredMixin,ListView):
    model = Profile
    template_name = 'users.html'  
    context_object_name = 'users'
    paginate_by = 10
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class AuthorAdd(LoginRequiredMixin,CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_add.html'
    success_url = reverse_lazy('authors_view')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class AuthorUpdate(LoginRequiredMixin,UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_edit.html'
    success_url = reverse_lazy('authors_view')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class AuthorDelete(LoginRequiredMixin,DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('authors_view')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('books_view')
    else:
        form = BookForm()
    return render(request, 'book_add.html', {'form': form})

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():

            form.save()
            return redirect('books_view')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_edit.html', {'form': form})

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('books_view')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class MemberCreate(LoginRequiredMixin, CreateView):
    model = Member
    form_class = MemberForm
    template_name = 'member_add.html'
    success_url = reverse_lazy('members_view')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class MemberUpdate(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'member_edit.html'
    success_url = reverse_lazy('members_view')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class MemberDelete(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = 'member_delete.html'
    success_url = reverse_lazy('members_view')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class BookInstanceCreate(LoginRequiredMixin, CreateView):
    model = BookInstance
    form_class = BookInstanceForm
    template_name = 'bookinstance_add.html'
    success_url = reverse_lazy('bookinstances_view')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q')
        books = Book.objects.all()
        if q:
            books = books.filter(title__icontains=q)
        books = books.distinct()
        context['books'] = books
        return context

class BookInstanceUpdate(LoginRequiredMixin, UpdateView):
    model = BookInstance
    form_class = BookInstanceForm
    template_name = 'bookinstance_edit.html'
    success_url = reverse_lazy('bookinstances_view')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

class BookInstanceDelete(LoginRequiredMixin, DeleteView):
    model = BookInstance
    template_name = 'bookinstance_delete.html'
    success_url = reverse_lazy('bookinstances_view')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

# Additional views
class TopPicksView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        top_picks = BookInstance.objects.order_by('-access_count')[:10]
        return render(request, 'top_picker.html', {'top_picks': top_picks})
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_view')  # Redirect to home after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You're successfully logged out, see you again")
    return redirect('login')

def register_view(request):
    from django.contrib.auth.forms import UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) 

def register_admin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False  # Ensure the user is not a staff member
            user.save()
            return redirect('users_view')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def edit_user_info(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('uinfo_view')
    else:
        form = UserInfoForm(instance=request.user.profile)
    return render(request, 'user_info_edit.html', {'form': form})