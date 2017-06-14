"""localprojects URL Configuration"""
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from survey import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', admin.site.urls),
    url(r'^ref_tokens/$',
        views.RefTokenList.as_view(),
        name='ref-token-list'),
    url(r'^ref_tokens/(?P<pk>[0-9]+)/$',
        views.RefTokenDetail.as_view(),
        name='ref-token-detail'),
    url(r'^tokens/$',
        views.TokenList.as_view(),
        name='token-list'),
    url(r'^tokens/(?P<pk>[0-9]+)/$',
        views.TokenDetail.as_view(),
        name='token-detail'),
    url(r'^ref_questions/$',
        views.RefQuestionList.as_view(),
        name='ref-question-list'),
    url(r'^ref_questions/(?P<pk>[0-9]+)/$',
        views.RefQuestionDetail.as_view(),
        name='ref-question-detail'),
    url(r'^users/$',
        views.PersonList.as_view(),
        name='user-list'),
    url(r'^users/(?P<user__username>[a-zA-Z]+)/questions/(?P<question_id>[0-9]+)/$',
        views.PersonDetail.as_view(),
        name='user-detail'),
    url(r'^users/(?P<user__username>[a-zA-Z]+)/questions/(?P<question_id>[0-9]+)/answer/(?P<answer>yes|no|YES|NO)/$',
        views.PersonDetail.as_view(),
        name='user-detail'),
    url(r'^users/(?P<user__username>[a-zA-Z]+)/$',
        views.PersonDetail.as_view(),
        name='user-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
