from django.contrib.syndication.feeds import Feed
from benford_name.blog import models

class LatestPosts(Feed):
    title = 'Benford.name - Personal Blog'
    link = 'http://www.benford.name/blog'
    description = 'a personal web log'
    
    def items(self):
        return models.Post.objects.order_by('-dateCreated')
        
    def item_link(self,obj):
        return obj.get_absolute_url()