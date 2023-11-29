from django.urls import path  
from . import views
from django.contrib.auth.decorators import login_required
from . import views
from .views import NewView,EmployeeCreate,EmployeeRetrieve,EmployeeDetail,EmployeeUpdate,EmployeeDelete,EmployeeNote


urlpatterns = [  
    # path('',views.index, name='index'),  
    path('', EmployeeCreate.as_view(),name = 'EmployeeCreate'),  
    path('about/', NewView.as_view(), name='response'),  
    path('retrieve/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),
    path('detail/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
    path('<int:pk>/update/', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),    
    path('<pk>/delete/', EmployeeDelete.as_view(), name = 'EmployeeDelete'),
    path('api', EmployeeNote.as_view(), name='api'),  
    path('test_api/', views.api, name='test_api'),

]  