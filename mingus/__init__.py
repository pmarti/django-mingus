from django.db.models import signals
from django_proxy.signals import proxy_save, proxy_delete
from basic.blog.models import Post
from basic.bookmarks.models import Bookmark
import code_directive

signals.post_save.connect(proxy_save, Post, True)
signals.post_delete.connect(proxy_delete, Post)

signals.post_save.connect(proxy_save, Bookmark, True)
signals.post_delete.connect(proxy_delete, Bookmark)
