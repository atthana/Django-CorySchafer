from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # UserPassesTestMixin จะช่วยจัดการ permission ให้แก้ไขได้เฉพาะโพสต์ของ user ตัวเองเท่านั้น

# posts = [
#     {
#         'author': 'Atthana',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 8, 2020'
#     },
#     {
#         'author': 'Pawan',
#         'title': 'Blog Post 2',
#         'content': 'First post content',
#         'date_posted': 'August 1, 2020'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()  # ค่าในหน้า home มาจาก query all ตรงนี้ล่ะนะ
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):  # แบบนี้คือเราใช้ class inherit ListView  แทนที่ของ Function view ก่อนหน้านะ
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # เป็นวิธีการ sort จากล่าสุดไปหาอดีตนะ

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    # เราใช้ LoginRequiredMixin เพื่อให้เวลาจะเข้ามา /post/new/ แต่ให้ redirect มาที่ login ก่อนในกรณีที่ logout ไปแล้ว
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # Method นี้สร้างเพื่อให้สามารถสร้าง Post ใหม่ได้ ถ้าไม่มีพอกดปุ่ม Post เข้าไปก้อพังเลย
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # เป็นการจัดการ update view นะ
        post = self.get_object()
        if self.request.user == post.author:  # ต้องให้ user เป็น author เท่านั้นค่อย return True เพื่อให้แก้ไขได้
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # ถ้า delete แล้วก้อให้กลับไป Homepage

    def test_func(self):  # เป็นการจัดการ delete view นะ
        post = self.get_object()
        if self.request.user == post.author:  # ต้องให้ user เป็น author เท่านั้นค่อย return True เพื่อให้แก้ไขได้
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})




