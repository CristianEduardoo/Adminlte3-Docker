# usamos routers en lugar de path, ya que nos permiten hacer varias operaciones
# que gestiona Django como (get, post, delete, etc..)
from rest_framework import routers
from .views import PostViewSet 

app_name = "api_blog"

router = routers.DefaultRouter() # Clave porque lo gestiona Django (get, post, delete, etc..)
router.register('postis', PostViewSet, 'post_api')

urlpatterns = router.urls 