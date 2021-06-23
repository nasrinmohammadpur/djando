from django.urls import path
from .views import post_list,post_detail,post_share
#from django.conf import settings
#from django.conf.urls.static import static


app_name = 'products'

urlpatterns = [
# post views
      path('',post_list, name='post_list'),
      path('<int:year>/<int:month>/<int:day>/<slug:post>/',
      post_detail,
         name='post_detail'),
      path('<int:post_id>/share/',
            post_share, name='post_share'),
      path('tag/<slug:tag_slug>/',post_list, name='post_list_by_tag'), ]

#if settings.DEBUG:
         #urlpatterns += static(settings.MEDIA_URLS, document_root=settings.MADIA_ROOT)