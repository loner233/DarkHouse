from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
import mdeditor
from myBlog.upload import upload_image
from myBlog.views import index, archive, article, tag, category, do_logout, do_reg, do_login, comment_post
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  # path('admin/upload/(?P<dir_name>[^/]+)', upload_image, name='upload_image'),
                  url(r'mdeditor/', include('mdeditor.urls')),
                  path('archive', archive, name='archive'),
                  path('article', article, name='article'),
                  path('tag', tag, name='tag'),
                  path('category', category, name='category'),
                  path('comment/post/', comment_post, name='comment_post'),
                  path('logout', do_logout, name='logout'),
                  path('reg', do_reg, name='reg'),
                  path('login', do_login, name='login'),
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
