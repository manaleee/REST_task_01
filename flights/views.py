from rest_framework.generics import ListAPIView


from .models import Flight, Booking

# from flights.models import Flight

from .serializers import FlightsSerializer, BookingsSerializer


from datetime import datetime



# view for flights
class FlightsListView(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightsSerializer





# # view for bookings
class BookingsListView(ListAPIView):
	# queryset = BookingView.objects.all()
	queryset = Booking.objects.filter(date__gte=datetime.today())
	# queryset = Booking.objects.filter(date = datetime.today())
		# queryset = Booking.objects.filter(datetime = date.today())

	serializer_class = BookingsSerializer


