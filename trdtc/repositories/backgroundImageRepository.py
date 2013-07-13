import json, requests
from random import choice

class BackgroundImageRepository:
	_apiUrl = "http://api.flickr.com/services/rest/"
	_apiGetImagesParams = {
		"api_key": "fa3aab9099cd43acf0db644513aa0ab1",
		"method": "flickr.photos.search",
		"format": "json",
		"nojsoncallback": 1,
		"tags":"trondheim"
	}

	def getBackgroundImage(self):
		image = choice(self.__getImageIdsFromFlickr()).get("id");
		resp = requests.get(url = self._apiUrl, params = {
			"api_key": "fa3aab9099cd43acf0db644513aa0ab1",
			"method": "flickr.photos.getSizes",
			"format": "json",
			"nojsoncallback": 1,
			"photo_id":image
		})
		return resp.json().get("sizes").get("size")[-1].get("source")



	def __getImageIdsFromFlickr(self):
		resp = requests.get(url = self._apiUrl, params = self._apiGetImagesParams)
		return list({"id": photo.get("id")} for photo in resp.json().get("photos").get("photo"))
		