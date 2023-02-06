from django.urls import path
from . import views
#URLパターンを逆引きできるように名前をつける
app_name = 'blog'
#URLパターンを登録するための変数
#リクエストされたURLのページへのフルパス部分が''にマッチ(全て)した場合
#viewsモジュールのIndexViewクラスをインスタンス化する
urlpatterns = [
    path('',views.IndexView.as_view(),name='indexboot'),
    #リクエストされたURLが「blog-detai/レコードのid/」の場合はBlogDetailを実行
    path(
        #詳細ページのURLはblog-detail/レコードのid/
        'blog-detail/<int:pk>/',
        #viewsモジュールのBlogDetailを実行
        views.BlogDetail.as_view(),
        #URLパターンの名前を'blog_detail'にする
        name='blog_detail'
    ),
    path(
    'science-list/',
    views.ScienceView.as_view(),
    name='science_list'
    ),
    path(
    'dailylife-list/',
    views.DailylifeView.as_view(),
    name='dailylife_list'
    ),
    path(
    'music-list/',
    views.MusicView.as_view(),
    name='music_list'
    ),
    path(
    'contact/',
    views.ContactView.as_view(),
    name='contact'
    ),
]
