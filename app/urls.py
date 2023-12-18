from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('example/', views.listar_example, name='example'),
    path('example/create/', views.crear_example, name='crear_example'),
    path('example/<int:example_id>/', views.detalle_example, name='detalle_pexample'),
    path('example/<int:example_id>/editar/', views.editar_example, name='editar_example'),
    path('example/<int:example_id>/eliminar/', views.eliminar_example, name='eliminar_example'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
