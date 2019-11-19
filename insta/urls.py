from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from insta.views import PostLikeToggle, PostLikeAPIToggle

urlpatterns = [
    url(r'signup/$', views.signup, name='signup'),
    url(r'^$',views.index,name="index"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^user_profile/(?P<username>\w+)', views.user_profile, name='user_profile'),
    url(r'^post/(?P<id>\d+)', views.post_comment, name='comment'),
    url(r'^post/(?P<id>)\d+', PostLikeToggle.as_view(), name='liked'),
    url(r'^api/post/(?P<id>)\d+', PostLikeAPIToggle.as_view(), name='liked-api'),
    url(r'^like', views.like_post, name='like_post'),
    url(r'^search/', views.search_profile, name='search'),
    url(r'^follow/(?P<user_id>\d+)', views.follow, name='follow'),
    url(r'^unfollow/(?P<user_id>\d+)', views.unfollow, name='unfollow'),
   
 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
