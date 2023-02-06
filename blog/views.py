from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blog:contact')
    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'送信されました')
        return super().form_valid(form)
class IndexView(ListView):
    """トップページのビュー
    投稿記事を一覧表示するのでListViewを継承する
    Attributes:
      template_name: レンダリングするテンプレート(html)
      context_object_name: object_listキーの別名を設定
      queryset: データベースのクエリ
    """
    #indexboot.htmlをレンダリング
    template_name = 'indexboot.html'
    #object_listキーの別名を設定
    context_object_name = 'orderby_records'
    #BlogPostのレコードを投稿日時の降順で並び替える
    queryset = BlogPost.objects.order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 4
class BlogDetail(DetailView):
    template_name = 'post.html'
    model = BlogPost
class ScienceView(ListView):
    template_name = 'science_list.html'
    model = BlogPost
    context_object_name = 'science_records'
    queryset = BlogPost.objects.filter(category='science').order_by('-posted_at')
    paginate_by = 2
class DailylifeView(ListView):
    template_name = 'dailylife_list.html'
    model = BlogPost
    context_object_name = 'dailylife_records'
    queryset = BlogPost.objects.filter(category='dailylife').order_by('-posted_at')
    paginate_by = 2
class MusicView(ListView):
    template_name = 'music_list.html'
    model = BlogPost
    context_object_name = 'music_records'
    queryset = BlogPost.objects.filter(category='music').order_by('-posted_at')
    paginate_by = 2
