var _flickrData;
function jsonFlickrFeed(data){
	_flickrData = data;
}
$(function(){
	$.getJSON("api/images", function(data){
		$("body").css("background-image", "url(" + data + ")");
	});
});