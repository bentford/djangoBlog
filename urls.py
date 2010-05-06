from django.conf.urls.defaults import patterns, include
from benford_name.blog.feeds import LatestPosts

feed_dict = {'posts':LatestPosts}

urlpatterns = patterns('',
   	(r'^comments/', include('django.contrib.comments.urls')),
    (r'^feeds/(?P<url>.*)$', 'django.contrib.syndication.views.feed', {'feed_dict':feed_dict}),
    (r'^tag/(?P<tag>.*)$', 'benford_name.blog.views.tags'),
    (r'^(?P<year>\d+)/(?P<month>\d+)/(?P<slug>.+)$', 'benford_name.blog.views.posts_for_year_month_slug'),
    (r'^(?P<year>\d+)/(?P<month>\d+)$', 'benford_name.blog.views.posts_for_year_month'),
    (r'^(?P<year>\d+)$', 'benford_name.blog.views.posts_for_year'),
    (r'^archive$', 'benford_name.blog.views.archive'),
    (r'','benford_name.blog.views.posts' )
)
