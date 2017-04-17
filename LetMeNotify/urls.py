from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from Profile import views
from django.views.decorators.cache import cache_page
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/',include('Profile.urls')),
    url(r'^userjson/',views.userList.as_view()),
    url(r'^restaurantjson/',views.restaurantList.as_view()),
    # url(r'^hotelview/',views.HotelviewerList.as_view()),
    url(r'^restaurantsmartsearch/(?P<name>.+)/$',views.restaurantList1.as_view()),
    url(r'^locationjson/',views.locationList.as_view()),
    url(r'^loginjson/',views.LoginList.as_view()),
    url(r'^fueljson/',views.FuelStationList.as_view()),
    url(r'^fuelsmartsearch/(?P<Name>.+)/$',views.FuelStationList1.as_view()),
    url(r'^hoteljson/',views.HotelList.as_view()),
    url(r'^hotelsmartsearch/(?P<Name>.+)/$',views.HotelList1.as_view()),
    url(r'^hotelsorted/(?P<Name>.+)/$',views.HotelList2.as_view()),
    url(r'^fuelsorteach/(?P<sortingvar>.+)/$',views.FuelStationListAllSorted.as_view()),
    url(r'^fuelsortall/(?P<sortingvar>.+)/$',views.FuelStationListAllSorted.as_view()),
    url(r'^hotel/(?P<pk>[0-9]+)/$', views.HotelDetail.as_view()),
    url(r'^hotelname/(?P<Name>[a-zA-Z\s&+,:;=?@.#|]+)/$', views.HotelDetail1.as_view()),
    url(r'^fuelname/(?P<Name>[a-zA-Z\s&+,:;=?@.#|]+)/$', views.FuelStationDetail1.as_view()),
    url(r'^fuel/(?P<pk>[0-9]+)/$', views.FuelStationDetail.as_view()),
    url(r'^restaurant/(?P<pk>[0-9]+)/$', views.restaurantDetail.as_view()),
    url(r'^restaurantname/(?P<name>[a-zA-Z\s&+,:;=?@.#|]+)', views.restaurantDetail1.as_view()),
    url(r'^move/', views.hello),
    # url(r'^$', views.index),
    # url(r'^traced_with_attrs/', views.traced_func_with_attrs),
    # url(r'^traced/', views.traced_func),
    # url(r'^untraced/', views.untraced_func)
]

urlpatterns = format_suffix_patterns(urlpatterns)