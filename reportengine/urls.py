from django.conf.urls import url
from reportengine import views

urlpatterns = [
    # Listing of reports
    url('^$', views.report_list, name='reports-list'),

    # view report redirected to current date format (requires date_field argument)
    url('^current/(?P<daterange>(day|week|month|year))/(?P<namespace>[-\w]+)/(?P<slug>[-\w]+)/$',
        views.current_redirect, name='reports-current'),
    # view report redirected to current date format with formatting specified
    url('^current/(?P<daterange>(day|week|month|year))/(?P<namespace>[-\w]+)/(?P<slug>[-\w]+)/(?P<output>[-\w]+)/$',
        views.current_redirect, name='reports-current-format'),
    # specify range of report per time (requires date_field)
    url('^date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<namespace>[-\w]+)/(?P<slug>[-\w]+)/$',
        views.day_redirect, name='reports-date-range'),
    # specify range of report per time with formatting
    url('^date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<namespace>[-\w]+)/(?P<slug>[-\w]+)/(?P<output>[-\w]+)/$',
        views.day_redirect, name='reports-date-range-format'),
    # Show latest calendar of all date accessible reports
    url('^calendar/$', views.calendar_current_redirect, name='reports-calendar-current'),
    # Show specific month's calendar of reports
    url('^calendar/(?P<year>\d+)/(?P<month>\d+)/$', views.calendar_month_view, name='reports-calendar-month'),
    # Show specifi day's calendar of reports
    url('^calendar/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', views.calendar_day_view, name='reports-calendar-day'),

]


urlpatterns += [
    # View report in first output style
    url('^request/(?P<namespace>[-\w]+)/(?P<slug>[-\w]+)/$', views.request_report, name='reports-view'),
    # view report in specified output format
    #url('^request/(?P<namespace>[-\w]+)/(?P<slug>[-\w]+)/(?P<output>[-\w]+)/$', 'request_report', name='reports-view-format'),

    url('^view/(?P<token>[\w\d]+)/$', views.view_report, name='reports-request-view'),
    # view report in specified output format
    url('^view/(?P<token>[\w\d]+)/(?P<output>[-\w]+)/$', views.view_report_export, name='reports-request-view-format'),
]
