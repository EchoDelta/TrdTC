var _flickrData;
function jsonFlickrFeed(data){
	_flickrData = data;
}
$(function(){
	if(_flickrData.items.length > 0 ){
		var image = _flickrData.items[Math.floor(Math.random()*_flickrData.items.length)];
		$("body").css("background-image", "url(" + image.media.m + ")");			
	}
});