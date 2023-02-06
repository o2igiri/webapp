from django.db import models

class BlogPost(models.Model):
    #カテゴリに設定する項目を入れ子のタプルとして定義
    #最初の要素はモデルが使用する値，2番目の要素は選択メニューに表示する文字列
    CATEGORY = (('science','科学について'),('dailylife','日常生活について'),('music','音楽について'))
    #タイトル用のフィールド
    title = models.CharField(
        verbose_name = 'タイトル',
        max_length = 200
    )
    content = models.TextField(
        verbose_name = '本文'
    )
    posted_at = models.DateTimeField(
        verbose_name = '投稿日時',
        auto_now_add = True
    )
    category = models.CharField(
        verbose_name = 'カテゴリ',
        max_length = 50,
        choices = CATEGORY
    )
    def __str__(self):
        #オブジェクトを文字列に変換して返す Returns(str):投稿記事のタイトル
        return self.title
