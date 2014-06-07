from django.conf.urls import patterns, url

urlpatterns = patterns('polls.views',
	# /polls/
	url(r'^$', 'index', name='index'),
	# /polls/5
	url(r'^(?P<poll_id>\d+)/$', 'detail', name="detail"),
	# /poll/5/results
	url(r'^(?P<poll_id>\d+)/results/$', 'results', name="results"),
	# /polls/5/vote
	url(r"^(?P<poll_id>\d+)/vote/$", 'vote', name='vote'),
)