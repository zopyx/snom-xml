import requests
import pprint
from pyramid.response import Response
from pyramid.view import view_config

API_KEY = '74bd568f272457a41da25719fc69af8f'

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'snom'}

@view_config(name='incoming-call', renderer='templates/incoming-call.pt')
def incoming_call(request):

#    number = '06897768639'
    number = request.params['number']
    params = dict(key=API_KEY, number=number)
    result = requests.get('http://openapi.klicktel.de/searchapi/invers', params=params)
    if result.status_code == 200:
        result = result.json()
        try:
            entry = result['response']['results'][0]['entries'][0]
        except IndexError:
            return Response(status=404)

        pprint.pprint(entry)
        pprint.pprint(entry['displayname'])
        return dict(entry=entry)

    return Response(status=404)

