from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_list, name='page_list'),
    path('page/<uuid:page_id>/', views.page_viewer, name='page_viewer'),
    path('page/<uuid:page_id>/edit', views.page_editor, name='page_editor'),
    path('create_page/', views.create_page, name='create_page'),
    path('page/<uuid:page_id>/create_section/', views.create_section, name='create_section'),
    path('section/<uuid:section_id>/create_element/', views.create_element, name='create_element'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('import_html/', views.import_html, name='import_html'),
    path('export_html/<uuid:page_id>/', views.export_html, name='export_html'),
    path('page/<uuid:page_id>/delete/', views.delete_page, name='page_delete'),
    path('page/<uuid:page_id>/HTML_activate/', views.activate_html, name='page_act_html'),
    path('search/', views.search, name='search'),
    path('user/', views.user_page, name='user'),
    path('themes/', views.select_theme, name='theme'),
    path('save_edits/<uuid:page_id>/', views.save_edits, name='save_edits'),
    path('page/<uuid:page_id>/admin/', views.admin_panel, name='admin_panel'),
    path('page/<uuid:page_id>/locked/', views.locked_page_view, name='locked_page'),
    path('theme_builder/', views.theme_builder, name='theme_builder'),
]
