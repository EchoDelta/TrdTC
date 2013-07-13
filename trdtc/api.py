from pyramid.view import view_config
from repositories.backgroundImageRepository import BackgroundImageRepository

@view_config(route_name='api_getImages', renderer='json')
def api_getImages(request):
	imageRepo = BackgroundImageRepository()
	return imageRepo.getBackgroundImage()
	