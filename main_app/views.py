from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models as my_models
from . import forms as my_forms



def Category(request, catg_name):
    category_posts = my_models.Post.objects.filter(category=catg_name.replace('-', ' '))
    return render(request, 'category.html',
                  {'catg_name': catg_name.title().replace('-', ' '), 'category_posts': category_posts})


def CategoryList(request):
    category_menu_list = my_models.Category.objects.all()
    return render(request, 'category_list.html', {'category_menu_list': category_menu_list})


def Like(request, pk):
    post = get_object_or_404(my_models.Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class Home(ListView):
    model = my_models.Post
    template_name = 'home.html'
    ordering = ['-publication_date']

    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        catg_menu = my_models.Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['catg_menu'] = catg_menu
        return context


class ArticleDetail(DetailView):
    model = my_models.Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        catg_menu = my_models.Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(my_models.Post, id=self.kwargs['pk'])
        liked_peoples = stuff.likes.all()
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['catg_menu'] = catg_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        context['liked_peoples'] = liked_peoples
        return context


class AddPost(CreateView):
    model = my_models.Post
    form_class = my_forms.PostForm
    template_name = 'add_post.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(AddPost, self).dispatch(request, *args, **kwargs)
        else:
            return render(request, 'add_post.html')


class AddCategory(CreateView):
    model = my_models.Category
    template_name = 'add_category.html'
    fields = '__all__'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(AddCategory, self).dispatch(request, *args, **kwargs)
        else:
            return render(request, 'add_category.html')


class UpdatePost(UpdateView):
    model = my_models.Post
    form_class = my_forms.EditForm
    template_name = 'update_post.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            post_id = my_models.Post.author
            return super(UpdatePost, self).dispatch(request, *args, **kwargs)
            #user_id = request.user.id
            #post_id = ''
            #if post_id == user_id:
            #    pass
        else:
            return render(request, 'update_post.html')


class DeletePost(DeleteView):
    model = my_models.Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(DeletePost, self).dispatch(request, *args, **kwargs)
        else:
            return render(request, 'delete_post.html')


class AddComment(CreateView):
    model = my_models.Comment
    form_class = my_forms.CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)