from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin
from django.conf import settings

from .utils import get_weather_info, get_json


class WeatherNowView(TemplateResponseMixin, View):

	def dispatch(self, request, *args, **kwargs):
		if request.method == 'GET':
			self.template_name = 'weather/form.html'
		else:
			self.template_name = 'weather/now.html'
		return super().dispatch(request, *args, **kwargs)

	def get(self, request):
		context = {}
		return self.render_to_response(context)	
	
	def post(self, request):
		city = request.POST.get('city')
		url = settings.WEATHER_API_URL.format(
			city, 
			settings.OPEN_WEATHER_API_KEY
		)
		data = get_json(url)
		if data:
			context = get_weather_info(data)
			return self.render_to_response(context)
		messages.error(request, 'Incorrect name of the city!')
		return redirect('weather:now')
		