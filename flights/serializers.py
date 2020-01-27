from rest_framework import serializers

from .models import Flight, Booking 


# from flights.models import FlightsSerializer, BookingsSerializer



class FlightsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['id', 'destination', 'time', 'price']

	
	



class BookingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ["flight", "date", "id"]

	
	
