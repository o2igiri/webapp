from django.contrib import admin
#modelsからBlogPostクラスをインポート
from .models import BlogPost
#django管理サイトにBlogPostを登録する
admin.site.register(BlogPost)
