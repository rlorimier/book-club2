from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    """ A view to show a list with all blog posts """

    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """
    A view to show the posts in detail
    It also saves the user comments on each post
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    """ A view to add likes at the posts """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def new_post(request):
    """ A view to save new posts """

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_on = timezone.now()
            post.save()
            return redirect('index')
        else:
            messages.error(request, 'Failed to add new post.')

    else:
        form = PostForm()

    return render(request, 'new_post.html', {'form': form})


@login_required
def edit_post(request, slug):
    """ A view to edit existing posts """

    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_on = timezone.now()
            post.save()
            return redirect('post_detail', slug=slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})


@login_required
def delete_post(request, slug):
    """ Delete a post """

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect(reverse('index'))


def about(request):
    """ A view to show the about us page """

    aboutus = ""
    return render(request, 'about.html', {'aboutus': aboutus})
