from django.db import models


class user(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    dob = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=26)
    phone = models.CharField(max_length=20)
    photo = models.CharField(max_length=100)
    friends = models.CharField(max_length=20)
    reg_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class friend(models.Model):
    f_name = models.CharField(max_length=100)
    f_userid = models.ForeignKey(user, on_delete=models.CASCADE)
    f_lat = models.CharField(max_length=300)
    f_long = models.CharField(max_length=300)



class Restaurant(models.Model):
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    locality = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20,default="Not Available")
    average_cost_for_two = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    menu_url = models.CharField(max_length=300)
    aggregate_rating = models.CharField(max_length=20)
    rating_text = models.CharField(max_length=300)
    votes = models.CharField(max_length=100)
    cuisines = models.CharField(max_length=300)
    Lock = models.BooleanField(default = False)
    def __str__(self):
        return self.name


class FuelStation(models.Model):
    State = models.CharField(max_length=300)
    City = models.CharField(max_length=300)
    Name = models.CharField(max_length=300)
    Address = models.CharField(max_length=300)
    CompanyName = models.CharField(max_length=300)
    Lock = models.BooleanField(default = False)
    def __str__(self):
        return self.Name


    # @property
    # def cityfun(self):
    #     return self.City
    #
    # def countcity(self):
    #     counter =0
    #     name = self.cityfun()
    #     if name =





class Hotel(models.Model):
    Name = models.CharField(max_length=300)
    HotelUrl = models.CharField(max_length=300)
    Address = models.CharField(max_length=300)
    Lock = models.BooleanField(default = False)
    # link
    def __str__(self):
        return self.Name





#
# class HFR(models.Model):
#     HotelName = Hotel.Name
#     HotelAddress = Hotel.Address
#     FuelStationName = FuelStation.Name
#     FuelStationAddress = FuelStation.Address
#     RestaurantName = Restaurant.name
#     RestaurantAddress = Restaurant.address
#

'''
{
  "fuel_stations": [
    {

      "cards_accepted": null,
      "city": "Golden",
      "date_last_confirmed": "2012-12-31",
      "expected_date": null,
      "fuel_type_code": "ELEC",
      "geocode_status": "200-8",
      "groups_with_access_code": "Private access only",
      "hy_status_link": null,
      "intersection_directions": "Building 17",
      "latitude": 39.7408399,
      "longitude": -105.1685277,
      "open_date": "2011-05-20",
      "owner_type_code": "FG",
      "station_name": "National Renewable Energy Laboratory - Denver West",
      "station_phone": null,
      "status_code": "E",
      "street_address": "15013 Denver West Pkwy",
      "zip": "80401",
      "state": "CO",
      "ng_fill_type_code": null,
      "ng_psi": null,
      "ng_vehicle_class": null,
      "e85_blender_pump": null,
      "ev_level1_evse_num": null,
      "ev_level2_evse_num": 38,
      "ev_dc_fast_num": null,
      "ev_other_evse": null,
      "ev_network": null,
      "ev_network_web": null,
      "lpg_primary": null,
      "id": 39534,
      "updated_at": "2013-01-16T16:09:02Z",
      "distance": 0.92673,
      "federal_agency": {
        "id": 8,
        "name": "U.S. Department of Energy"
      }
    }
  ],
  "latitude": 39.744696,
  "longitude": -105.15186,
  "offset": 0,
  "precision": {
    "name": "address",
    "types": [
      "street_address"
    ],
    "value": 8
  },
  "station_locator_url": "http://www.afdc.energy.gov/afdc/locator/stations/",
  "total_results": 12
}



'''

'''
class all_reviews(models.Model):
    res_id = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    rating = models.IntegerField(max_length=10)
    rating_text = models.CharField(max_length=300)
    rating_color = models.CharField(max_length=50)
    review_time_friendly = models.CharField(max_length=20)
    review_text = models.CharField(max_length=300)
    timestamp = models.CharField(max_length=20)
    likes = models.IntegerField(max_length=20)
    comments_count = models.IntegerField(max_length=10)

class location(models.Model):
    id = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    address = models.CharField(max_length=300)
    locality = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    lat = models.IntegerField(max_length=20)
    long = models.IntegerField(max_length=20)
    zipcode = models.IntegerField(max_length=20)
class photos(models.Model):
    url = models.CharField(max_length=300)
    thumb_url = models.CharField(max_length=300)
    res_id = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    '''
