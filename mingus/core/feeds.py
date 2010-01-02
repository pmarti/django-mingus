from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _
from django.contrib.syndication.feeds import Feed, FeedDoesNotExist

from basic.blog.models import Settings, Post
from django_proxy.models import Proxy
from tagging.models import Tag, TaggedItem


class AllEntries(Feed):
    _settings = None

    @property
    def settings(self):
        if self._settings is None:
            self._settings = Settings.get_current()
        return self._settings

    def title(self):
        return self.settings.site_name

    def description(self):
        return _('All entries published and updated on %s') % self.settings.site_name

    def author_name(self):
        return self.settings.author_name

    def copyright(self):
        return self.settings.copyright

    def link(self):
        return 'http://%s' % self._settings.site.domain

    def items(self):
        return Proxy.objects.published().order_by('-pub_date')[:10]

    def item_link(self, item):
        return item.content_object.get_absolute_url()

    def item_categories(self, item):
        return item.tags.replace(',', '').split()


class BlogPostsByTag(Feed):
    _settings = Settings.get_current()
    author_name = _settings.author_name
    copyright = _settings.copyright

    @property
    def settings(self):
        if self._settings is None:
            self._settings = Settings.get_current()
        return self._settings

    def title(self):
        return self.settings.site_name

    def description(self):
        return _('Tagged posts on %s') % self.settings.site_name

    def author_name(self):
        return self.settings.author_name

    def copyright(self):
        return self.settings.copyright

    def get_object(self, bits):
        if len(bits) != 1:
            raise ObjectDoesNotExist
        return Tag.objects.get(name__exact=bits[0])

    def link(self, obj):
        if not obj:
            raise FeedDoesNotExist
        return '/tags/%s' % obj.name

    def items(self, obj):
        return TaggedItem.objects.get_by_model(Post, obj)[:10]
