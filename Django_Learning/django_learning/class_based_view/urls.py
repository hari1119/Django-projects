from django.urls import path, re_path 
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView, LoginView
from .views import crud_operation, user_register_and_login, api_operation, orm_method, mail, htmx


urlpatterns = [ 
    path('', user_register_and_login.Employee.as_view(), name='cbv_index'),
    path('sample_temp', user_register_and_login.DemoTempalte.as_view(), name='Sample_temp', ),
    
    path('default_signup/', user_register_and_login.DefaultSignUp.as_view(), name='default_signup', ),
    path('custom_signup/', user_register_and_login.CustomSignUp.as_view(), name='custom_signup', ),

    path('logins/', TemplateView.as_view(template_name='foo.html'), name='login', ), 
    # Direct template render from url

    path('emp_login/', user_register_and_login.EmpLoginForm.as_view(), name='emp_login', ), 
    # Custom login from view 

    # path('emp_login/', LoginView.as_view(template_name = 'login.html'), name='emp_login'), 
    # Default django Login from url 

    path('logout/',LogoutView.as_view(), name='logout', ), 
    # Default django Logout from url 

    
    path('stdnt_form/',crud_operation.StudentForm.as_view(), name='stdnt_form', ), 
    path('stdnt_list/',crud_operation.StudentList.as_view(), name='stdnt_list', ), 
    path('stdnt_detail/<int:pk>/detail/', crud_operation.StudentDetail.as_view(), name='stdnt_detail', ),
    path('stdnt_update/<int:pk>/update/', crud_operation.StudentUpdate.as_view(), name='stdnt_update', ),
    path('stdnt_delete/<int:pk>/delete/', crud_operation.StudentDelete.as_view(), name='stdnt_delete', ),

    path('orm/',orm_method.OrmFunction.as_view(), name='orm_function', ), 

    path('api_crud/',api_operation.StudentData.as_view(), name='api_crud'), 

    path('mail/',mail.contactview, name='mail', ), 

    path('htmx/',htmx.htmx, name='htmx'), 
    path('htmx_form/',htmx.htmx_form, name='htmx_form'), 
    path('testing_date/',crud_operation.test_date, name='test_date')
]