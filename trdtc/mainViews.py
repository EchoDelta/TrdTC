from pyramid.view import view_config

@view_config(route_name='main', renderer='templates/main.pt')
def main_view(request):
	return {
		'title':'Trondheim Tech Corner',
		'tagline':'The dark corner of a pub where developers gather'
	}