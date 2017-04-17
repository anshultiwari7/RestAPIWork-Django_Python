from django.db import connection
# from crypt import methods
# from datetime import datetime
from datetime import datetime
import properties as properties
from django.http import Http404, HttpResponse
from django.core.cache import cache
from django.utils.html import linebreaks
from rest_framework.decorators import api_view
from copy import deepcopy
# from rest_framework import pagination
# from rest_framework.decorators import api_view
# from django_filters import models
from rest_framework.filters import OrderingFilter
# import django_filters
# from django.shortcuts import render
from django_filters.rest_framework import filters
from rest_framework import status, generics
# from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import user, Restaurant, FuelStation, Hotel
from .serializers import userSerializer, restaurantSerializer, locationSerialzier, LoginSerializer,FuelStationSerializer, HotelSerializer

# from rest_framework import permissions

http_method_names = ['get', 'purge', 'post', 'head', 'options', 'copy', 'put', 'patch', 'lock', 'unlock', 'delete',
                         'propfind','view']




content = [
    {
        'error': 0,
        'response': 'success'
    }
]
error = [
    {
        'error': 1,
        'response': 'fail'
    }
]

'''

tracer = settings.OPENTRACING_TRACER

def index(request):
    return HttpResponse("index")

@tracer.trace('path', 'scheme', 'fake_setting')
def traced_func_with_attrs(request):
    currentSpanCount = len(settings.OPENTRACING_TRACER._current_spans)
    response = HttpResponse()
    response['numspans'] = currentSpanCount
    return response

@tracer.trace()
def traced_func(request):
    currentSpanCount = len(settings.OPENTRACING_TRACER._current_spans)
    response = HttpResponse()
    response['numspans'] = currentSpanCount
    return response

def untraced_func(request):
    currentSpanCount = len(settings.OPENTRACING_TRACER._current_spans)
    response = HttpResponse()
    response['numspans'] = currentSpanCount
    return response
'''


class userList(APIView):
    def get(self, request):
        users = user.objects.all()
        u_serializer = userSerializer(users, many=True)
        return Response(u_serializer.data)

    def post(self, request):
        u_serializer = userSerializer(data=request.data)
        if u_serializer.is_valid():
            u_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class LoginList(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        l = LoginSerializer(data=request.data)
        if l.is_valid():
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


'''
class userList(APIView):

    def get(self,request):
        p = user.objects.all()
        serializer = userSerializer(p,many=True)
        return Response(serializer.data)

    def profile_details(request):
        all_profiles = user.objects.all()
        context = {'all_profiles' : all_profiles}
        return render(request, 'profile_names.html' , context)

    def friend_names(request):
        return HttpResponse("<h1>you friend list will be shown here soon</h1>")
'''


class restaurantList(APIView):
    def get(self, request):
        p = Restaurant.objects.all()
        serializer = restaurantSerializer(p, many=True)
        # API_LIMIT_PER_PAGE = 50
        return Response(serializer.data)

    # def post(self,request):
    #     serializer = restaurantSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        temp = request.data
        for x in temp:
            serializer = restaurantSerializer(data=x)
            if serializer.is_valid():
                serializer.save()


class restaurantListAllSorted(APIView):
    def get_object(self, sortingvar):
        try:
            if sortingvar == 'pkasc':
                return Restaurant.objects.filter().order_by('pk')
            if sortingvar == 'pk':
                return Restaurant.objects.filter().order_by('pk')
            elif sortingvar == 'pkdesc':
                return Restaurant.objects.filter().order_by('-pk')
            elif sortingvar == 'nameasc':
                return Restaurant.objects.filter().order_by('name')
            elif sortingvar == 'name':
                return Restaurant.objects.filter().order_by('name')
            elif sortingvar == 'namedesc':
                return Restaurant.objects.filter().order_by('-name')
            elif sortingvar == 'addressasc':
                return Restaurant.objects.filter().order_by('address')
            elif sortingvar == 'address':
                return Restaurant.objects.filter().order_by('address')
            elif sortingvar == 'addressdesc':
                return Restaurant.objects.filter().order_by('-address')
            elif sortingvar == 'localityasc':
                return Restaurant.objects.filter().order_by('locality')
            elif sortingvar == 'locality':
                return Restaurant.objects.filter().order_by('locality')
            elif sortingvar == 'localitydesc':
                return Restaurant.objects.filter().order_by('-locality')
            elif sortingvar == 'cityasc':
                return Restaurant.objects.filter().order_by('city')
            elif sortingvar == 'city':
                return Restaurant.objects.filter().order_by('city')
            elif sortingvar == 'citydesc':
                return Restaurant.objects.filter().order_by('-city')
            elif sortingvar == 'lat':
                return Restaurant.objects.filter().order_by('latitude')
            elif sortingvar == 'latasc':
                return Restaurant.objects.filter().order_by('latitude')
            elif sortingvar == 'latdesc':
                return Restaurant.objects.filter().order_by('-latitude')
            elif sortingvar == 'longasc':
                return Restaurant.objects.filter().order_by('city')
            elif sortingvar == 'long':
                return Restaurant.objects.filter().order_by('longitude')
            elif sortingvar == 'longdesc':
                return Restaurant.objects.filter().order_by('-longitude')
            elif sortingvar == 'avgcostasc':
                return Restaurant.objects.filter().order_by('average_cost_for_two')
            elif sortingvar == 'avgcost':
                return Restaurant.objects.filter().order_by('average_cost_for_two')
            elif sortingvar == 'avgcostdesc':
                return Restaurant.objects.filter().order_by('-average_cost_for_two')
            elif sortingvar == 'votesasc':
                return Restaurant.objects.filter().order_by('votes')
            elif sortingvar == 'votes':
                return Restaurant.objects.filter().order_by('votes')
            elif sortingvar == 'votesdesc':
                return Restaurant.objects.filter().order_by('-votes')

        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, sortingvar, format=None):
        restaurant = self.get_object(sortingvar)
        serializer = restaurantSerializer(restaurant, many=True)
        return Response(serializer.data)


class restaurantList1(APIView):
    def get_object(self, name):
        try:
            return Restaurant.objects.filter(name__icontains=name)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        restaurant = self.get_object(name)
        serializer = restaurantSerializer(restaurant, many=True)
        return Response(serializer.data)


class restaurantDetail(APIView):
    """
    Retrieve, update or delete a restaurant instance.
    """

    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        serializer = restaurantSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        serializer = restaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        restaurant = self.get_object(pk)
        serializer = restaurantSerializer(restaurant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        if restaurant.Lock == True:
            return Response(status=status.HTTP_403_FORBIDDEN)
        restaurant.delete()

    def lock(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        restaurant.Lock = True
        restaurant.save()

    def unlock(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        restaurant.Lock = False
        restaurant.save()

    http_method_names = ['get', 'post', 'head', 'options', 'copy', 'put', 'patch', 'lock', 'unlock', 'delete']


class restaurantList2(APIView):
    def get_object(self, Name):
        try:
            return Restaurant.objects.filter(Name=Name).order_by('-Name')
        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, Name, format=None):
        restaurant = self.get_object(Name)
        serializer = restaurantSerializer(Hotel, many=True)
        return Response(serializer.data)


class restaurantDetail1(APIView):
    """
    Retrieve, update or delete a Fuel instance.
    """

    def get_object(self, name):
        try:
            return Restaurant.objects.filter(name=name)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        restaurant = self.get_object(name)
        serializer = restaurantSerializer(restaurant, many=True)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        restaurant = self.get_object(name)
        for x in restaurant:
            serializer = restaurantSerializer(x, data=request.data)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, name, format=None):
        restaurant = self.get_object(name)
        for x in restaurant:
            serializer = restaurantSerializer(x, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        restaurant = self.get_object(name)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FuelStationList(APIView):
    def get(self, request):
        q = FuelStation.objects.all()
        serializer = FuelStationSerializer(q, many=True)
        # pagination_class = StandardResultsSetPagination
        return Response(serializer.data)

    def post(self, request):
        temp = request.data
        for x in temp:
            serializer = FuelStationSerializer(data=x)
            if serializer.is_valid():
                serializer.save()


class FuelStationList1(APIView):
    def get_object(self, Name):
        try:
            return FuelStation.objects.filter(Name__icontains=Name)
        except FuelStation.DoesNotExist:
            raise Http404

    def get(self, request, Name, format=None):
        FuelStation = self.get_object(Name)
        serializer = FuelStationSerializer(FuelStation, many=True)
        # pagination_class = StandardResultsSetPagination
        return Response(serializer.data)


class FuelStationList2(APIView):
    def get_object(self, Name):
        try:
            return FuelStation.objects.filter(Name=Name).order_by('pk')
        except FuelStation.DoesNotExist:
            raise Http404

    def get(self, request, Name, format=None):
        FuelStation = self.get_object(Name)
        serializer = FuelStationSerializer(FuelStation, many=True)
        return Response(serializer.data)


class FuelStationListAllSorted(APIView):
    def get_object(self, sortingvar):
        try:
            if sortingvar == 'pkasc':
                return FuelStation.objects.filter().order_by('pk')
            if sortingvar == 'pk':
                return FuelStation.objects.filter().order_by('pk')
            elif sortingvar == 'pkdesc':
                return FuelStation.objects.filter().order_by('-pk')
            elif sortingvar == 'nameasc':
                return FuelStation.objects.filter().order_by('Name')
            elif sortingvar == 'name':
                return FuelStation.objects.filter().order_by('Name')
            elif sortingvar == 'namedesc':
                return FuelStation.objects.filter().order_by('-Name')
            elif sortingvar == 'addressasc':
                return FuelStation.objects.filter().order_by('Address')
            elif sortingvar == 'address':
                return FuelStation.objects.filter().order_by('Address')
            elif sortingvar == 'addressdesc':
                return FuelStation.objects.filter().order_by('-Address')
            elif sortingvar == 'stateasc':
                return FuelStation.objects.filter().order_by('State')
            elif sortingvar == 'state':
                return FuelStation.objects.filter().order_by('State')
            elif sortingvar == 'statedesc':
                return FuelStation.objects.filter().order_by('-State')
            elif sortingvar == 'cityasc':
                return FuelStation.objects.filter().order_by('City')
            elif sortingvar == 'city':
                return FuelStation.objects.filter().order_by('City')
            elif sortingvar == 'citydesc':
                return FuelStation.objects.filter().order_by('-City')
        except FuelStation.DoesNotExist:
            raise Http404

    def get(self, request, sortingvar, format=None):
        FuelStation = self.get_object(sortingvar)
        serializer = FuelStationSerializer(FuelStation, many=True)
        return Response(serializer.data)


class FuelStationDetail(APIView):
    """
    Retrieve, update or delete a Fuel instance.
    """

    def get_object(self, pk):
        try:
            return FuelStation.objects.get(pk=pk)
        except FuelStation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Fuel = self.get_object(pk)
        serializer = FuelStationSerializer(Fuel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Fuel = self.get_object(pk)
        serializer = FuelStationSerializer(Fuel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        Fuel = self.get_object(pk)
        serializer = FuelStationSerializer(Fuel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def lock(self, request, pk, format=None):
        Fuel = self.get_object(pk)
        Fuel.Lock = True
        Fuel.save()

    def delete(self, request, pk, format=None):
        Fuel = self.get_object(pk)
        if Fuel.Lock == True:
            return Response(status=status.HTTP_403_FORBIDDEN)
        Fuel.delete()

    def unlock(self, request, pk, format=None):
        Fuel = self.get_object(pk)
        Fuel.Lock = False
        Fuel.save()

    http_method_names = ['get', 'post', 'head', 'options', 'copy', 'put', 'patch', 'lock', 'unlock', 'delete']


class FuelStationDetail1(APIView):
    """
    Retrieve, update or delete a Fuel instance.
    """

    def get_object(self, Name):
        try:
            return FuelStation.objects.filter(Name=Name)
        except FuelStation.DoesNotExist:
            raise Http404

    def get(self, request, Name, format=None):
        Fuel = self.get_object(Name)
        serializer = FuelStationSerializer(Fuel, many=True)
        return Response(serializer.data)

    def put(self, request, Name, format=None):
        Fuel = self.get_object(Name)
        for x in Fuel:
            serializer = FuelStationSerializer(x, data=request.data)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, Name, format=None):
        Fuel = self.get_object(Name)
        for x in Fuel:
            serializer = FuelStationSerializer(x, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, Name, format=None):
        Fuel = self.get_object(Name)
        Fuel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        # @list_route(methods=['GET'])
        # def schema(self, request):
        # meta = self.metadata_class()
        # data = meta.determine_metadata(request, self)
        # return Response(data)




class HotelList(APIView):
    def get(self, request):
        q = Hotel.objects.all()
        serializer = HotelSerializer(q, many=True)
        API_LIMIT_PER_PAGE = 5
        return Response(serializer.data)

    def post(self, request):
        temp = request.data
        for x in temp:
            serializer = HotelSerializer(data=x)
            if serializer.is_valid():
                serializer.save()

    # def view(self,request):
    #     Hotel.objects.raw('create view HotelView as select Name,Address from Hotel')
    #     Response(Hotel.objects.raw('select * from HotelView'))


            # return Response()
            # response={"Name":x.Name, "Address":x.Address}
            # y = str(response)+ ',' + str(linebreaks)



    http_method_names = ['get', 'purge', 'post', 'head', 'options', 'copy', 'put', 'patch', 'lock', 'unlock', 'delete',
                         'propfind','view']


class HotelListAllSorted(APIView):
    def get_object(self, sortingvar):
        try:
            if sortingvar == 'pkasc':
                return Hotel.objects.filter().order_by('pk')
            if sortingvar == 'pk':
                return Hotel.objects.filter().order_by('pk')
            elif sortingvar == 'pkdesc':
                return Hotel.objects.filter().order_by('-pk')
            elif sortingvar == 'nameasc':
                return Hotel.objects.filter().order_by('Name')
            elif sortingvar == 'name':
                return Hotel.objects.filter().order_by('Name')
            elif sortingvar == 'namedesc':
                return Hotel.objects.filter().order_by('-Name')
            elif sortingvar == 'addressasc':
                return Hotel.objects.filter().order_by('Address')
            elif sortingvar == 'address':
                return Hotel.objects.filter().order_by('Address')
            elif sortingvar == 'addressdesc':
                return Hotel.objects.filter().order_by('-Address')
            elif sortingvar == 'hotelurlasc':
                return Hotel.objects.filter().order_by('HotelUrl')
            elif sortingvar == 'hotelurl':
                return Hotel.objects.filter().order_by('HotelUrl')
            elif sortingvar == 'hotelurldesc':
                return Hotel.objects.filter().order_by('-State')

        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, sortingvar, format=None):
        Hotel = self.get_object(sortingvar)
        serializer = HotelSerializer(Hotel, many=True)
        return Response(serializer.data)


'''
class HotelList1(generics.ListAPIView):
    serializer_class = HotelSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        Name = self.kwargs['Name']
        return Hotel.objects.filter(Name=Name)


class HotelList1(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = (filters.OrderingFilter,)
    order_fields = ('Name', 'Address')
'''


class HotelList1(APIView):
    def get_object(self, Name):
        try:
            return Hotel.objects.filter(Name__icontains=Name)
        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, Name, format=None):
        Hotel = self.get_object(Name)
        serializer = HotelSerializer(Hotel, many=True)
        return Response(serializer.data)

    def link(self, request, Name, format=None):
        Hotel = self.get_object(Name)
        # Hotel.Link = True
        i=0
        p_s = [
            {
                'Hotel Name':Name,
                'data':[]
                }]
        for x in Hotel:
            p_s[0]['data'].insert(i,x.id)
            i = i+1
        # Hotel.Link = True
        return Response(p_s)
    #
    # def unlink(self,request,Name,format=None):
    #     Hotel = self.get_object(Name)
    #     Hotel.link = False

    http_method_names = ['get', 'purge', 'post', 'head', 'options', 'copy', 'put', 'patch', 'lock', 'unlock', 'delete',
                             'propfind','view','link']
class HotelList2(APIView):
    def get_object(self, Name):
        try:
            return Hotel.objects.filter(Name=Name).order_by('-Name')
        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, Name, format=None):
        Hotel = self.get_object(Name)
        serializer = HotelSerializer(Hotel, many=True)
        return Response(serializer.data)


'''
def allowed_methods(self):
    """
    Return the list of allowed HTTP methods, uppercased.
    """
    self.http_method_names.append("copy")
    return [method.upper() for method in self.http_method_names
            if hasattr(self, method)]

    def delete(self, request, pk, format=None):
        Hotel = self.get_object(pk)
        Hotel.pk = None
        Hotel.save()
'''


def get_object(Fuel,pk):
        try:
            return Fuel.objects.get(pk=pk)
        except Fuel.DoesNotExist:
            raise Http404


# @api_view(['GET','POST','COPY'])
class HotelDetail(APIView):
    def get_object(self, pk):
        try:
            return Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Hotel = self.get_object(pk)
        key = 'my_key/' + str(pk)
        cache.set(key, Hotel, 10 * 60)
        # hello(Hotel)
        serializer = HotelSerializer(Hotel)
        return Response(serializer.data)




    def view(self, request, pk, format=None):
        p_s = []
        z = 1
        for i in range(0,100):
            key = 'my_key/' + str(i)
            hotel = cache.get(key)
            serializer = HotelSerializer(hotel)
            p_s.insert(z,serializer.data)
            z = z+1
        return Response(p_s)


    def patch(self, request, pk):
        Hotel = self.get_object(pk)
        serializer = HotelSerializer(Hotel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        Hotel = self.get_object(pk)
        serializer = HotelSerializer(Hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Hotel = self.get_object(pk)
        if Hotel.Lock == True:
            return Response(status=status.HTTP_403_FORBIDDEN)
        Hotel.delete()

    def copy(self, request, pk, format=None):
        Hotel = self.get_object(pk)
        Hotel.pk = None
        Hotel.save()

    def lock(self, request, pk, format=None):
        Hotel = self.get_object(pk)
        Hotel.Lock = True
        Hotel.save()

    def unlock(self, request, pk, format=None):
        Hotel = self.get_object(pk)
        Hotel.Lock = False
        Hotel.save()

    def propfind(self, request, pk, format=None):
        Hotel = self.get_object(pk)
        if Hotel.Lock == True:
            var = 'True'
        else:
            var = 'False'
        response = {'Name': 'Charfield', 'HotelUrl': 'CharField', 'Address': 'CharField','DeleteLocked':var,'Primary Key':Hotel._meta.pk.name}
        return Response(response)



    http_method_names = ['get', 'purge', 'post', 'head', 'options', 'copy', 'put', 'patch', 'lock', 'unlock', 'delete',
                         'propfind','view','link']


    def purge(self, request, pk, format=None):
        key = 'my_key/' + str(pk)
        hotel = cache.get(key)
        serializer = HotelSerializer(hotel)
        cache.delete(key)
        return Response(serializer.data)




@api_view(['GET'])
def hello(xyz):
        hotel = xyz
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
    # if request.method == 'POST':
    #     pass


class HotelDetail1(APIView):
    """
    Retrieve, update or delete a Hotel instance.
    """

    def get_object(self, Name):
        try:
            return Hotel.objects.filter(Name=Name)
        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, Name, format=None):
        Hotel = self.get_object(Name)
        serializer = HotelSerializer(Hotel, many=True)
        return Response(serializer.data)

    def put(self, request, Name, format=None):
        Hotel = self.get_object(Name)
        for x in Hotel:
            serializer = HotelSerializer(x, data=request.data)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, Name, format=None):
        Hotel = self.get_object(Name)
        for x in Hotel:
            serializer = HotelSerializer(x, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, Name, format=None):
        Hotel = self.get_object(Name)
        Hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





        # def options(self,request, pk, format=None):
        # meta = self.metadata_class()
        # data = meta.determine_metadata(request, self)
        # return Response(data)

        # return Response("hello")

        # class FuelList(APIView):
        #     def get(self, request):
        #         q = FuelStation.objects.all()
        #         for i in range():
        #             api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key=AIzaSyBmiTnXvnNhSpdSf7XumgbIB8s73UmDtYU'.format(i.Address))
        #             api_response_dict = api_response.json()
        #             a = FuelStation.objects.get(id = i.id)
        #             a.Latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        #             a.Longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        #             a.save()
        #             FuelStation.objects.get(id = i.id).update(Longitude=api_response_dict['results'][0]['geometry']['location']['lng'])
        # api_re/sponse_dict['results'][0]['geometry']['location']['lng']
        #
        # serializer = FuelStationSerializer(q, many=True)
        # return Response(serializer.data)
        #
        # def post(self, request):
        #     pass


#
#

class locationList(APIView):
    def get(self, request):
        p = Restaurant.objects.all()
        serializer = locationSerialzier(p, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = locationSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
def my_view(request):
    cache_page(60*10)
    return HttpResponse("hello")
'''
