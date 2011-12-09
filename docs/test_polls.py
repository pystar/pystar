#!/usr/bin/env python

'''
Tests for the 'polls' application.  Call using:

    ./manage.py test polls

'''


# called automatically by ./manage.py test; no harm though.
from django.test.utils import setup_test_environment
setup_test_environment()

# uses the new 'unittest2' improved testing framework, django 1.3+
from django.utils import unittest 
from django.test.client import Client

import datetime
import random

import django
if django.VERSION < (1,3):
    raise Exception("Needs Django 1.3+, becuase it uses unittest2")


## check whether the models even exist yet!
models_importable = False
try:
    from polls.models import Choice,Poll
    models_importable = True
except ImportError:
    pass



def setup_metal(seed=2929485983):
    '''
    produce a number of heavy metal polls, to populate the db with.
    
    Args:
        seed:  int for random number generator
    
    Returns:
        a list of constucted, *saved* polls.
    
    '''
    opinions = ['HEINOUS!', 'suxxors', 'rulez!', 
    'AWESOME!', 'righTEOUS', 'HAVE MY BABY!!!!',
    'BEYOND METAL','SUCKS','RULES', 'TOTALLY RULES']

    band_names = '''
    Abonos Meshuggah Xasthur Silencer Fintroll Beherit Basilisk Cryptopsy
    '''.strip().split()

    random.seed(seed)  # so it will always make the same polls
    def make_metal_poll(bandname,opinions):
        pub = datetime.datetime.now()
        marks = '?' * random.randint(1,5)
        question = bandname + marks
        chosen = random.sample(opinions,5)
        choices = list()
        for c in chosen:
            votes = random.randint(1,1000)
            choices.append(Choice(choice=c,votes=votes))
        
        p = Poll(question=question,pub_date=pub)
        p.save()
        p.choice_set=choices
        return p

    polls = [make_metal_poll(band,opinions) for band in band_names]
    return polls

## Tests

''' (r'^polls/$', 'polls.views.index'),
 (r'^polls/(\d+)/$', 'polls.views.detail'),
 (r'^polls/(\d+)/results/$', 'polls.views.results'),
 (r'^polls/(\d+)/vote/$', 'polls.views.vote'),'''

class Text_example(unittest.TestCase):
    def test_testing_is_sane(self):
        self.assertEqual(1,1)


## some testing utilities
def get(url):
    c = Client()
    response = c.get(url)
    return response

def post(url,post_kwargs=None):
    if post_kwargs is None:  post_kwargs={}
    c = Client()
    response = c.post(url,post_kwargs)
    return response

def fail(self,msg=None):
    self.assertFalse(True,msg=msg)

def ok_(self,msg=None):
    self.assertTrue(True,msg=msg)


def no_test_written(self):
    fail(self,"test not yet written")


def vote(poll_id,up=True):
    url = '/polls/%i/vote' % poll_id,
    r = post(url,)
    return r

def get_poll(id):
    try:
        return Poll.objects.get(id=id)
    except Exception,exc:
        return None


class Test_urls(unittest.TestCase):

    def test_root_redirects(self):
        response = get('/')
        self.assertEqual(response.status_code, 302)

    def test_poll_responds(self):
        response = get('/polls/')
        self.assertEqual(response.status_code, 200)

    def test_poll_reachable_if_exists(self):
        response = get('/polls/1/results/')
        self.assertEqual(response.status_code, 200)

    def test_poll_vote_reachable_if_exists(self):
        response = get('/polls/1/vote/')
        self.assertEqual(response.status_code, 200)

    def test_non_exist_poll_404s(self):
        # get a non-existent poll, then 404!
        response = get('/polls/1000000/')
        self.assertEqual(response.status_code, 404)
    
    def test_poll_post_without_choice_redirects(self):
        # Verify that if you submit the form without having chosen a 
        # choice, you should stay
        response = post('/polls/1/vote',{})
        self.assertEqual(response.status_code, 301)


class Test_index(unittest.TestCase):
    def setUp(self):
        if models_importable:
            self.polls = setup_metal()
        else:
            self.polls=None

    def test_index_has_5(self):
        if not models_importable :
            self.assertFalse()
        
        response = post('/polls/')
        content = response.content
        # silly!
        self.assertTrue(content.count('<li>',5))

class Test_detail(unittest.TestCase):
    def setUp(self):
        if models_importable:
            self.polls = setup_metal()
        else:
            self.polls=None

    def test_poll_1_has_right_count_of_choices(self):
        if not models_importable :
            self.assertFalse()
        
        expecting = len(get_poll(1).choice_set.all())
        response = post('/polls/1/')
        content = response.content
        # silly!
        self.assertEqual(content.count('radio'), expecting)

class Test_voting(unittest.TestCase):
    def setUp(self):
        if models_importable:
            self.polls = setup_metal()
        else:
            self.polls=None

    def test_vote_up_raises_vote_by_one(self):
        if not models_importable :
            self.assertFalse()
        
        c = get_poll(1).choice_set.all()[0]
        before = c.votes

        # simlulate a vote
        r = response = post('/polls/1/vote/',{'choice':c.id})
        c = get_poll(1).choice_set.all()[0]
        after = c.votes
        self.assertEqual(before+1, after)

    def test_after_vote_redirect_to_poll_details(self):
        ## after voting in a poll, it should redirect to that poll
        # post=....).redirects to whatever!
        if not models_importable :
            self.assertFalse()
        
        c = get_poll(1).choice_set.all()[0]
        r = response = post('/polls/1/vote/',{'choice':c.id})
        self.assertEqual(response.status_code, 302)
        # /polls/1/results/


## there must be a more elegant way
## to get this from Django!
def check_attrs(obj,attrs):
    for attr in attrs:
        try:
            getattr(obj,attr)
        except AttributeError,Exc:
            return False
        
        return True


## this isn't a great test, but illustrative.
## (unit-testy, fragile, not BDD).
class Test_models(unittest.TestCase):
    def setUp(self):
        if models_importable :
            self.polls = setup_metal()
        else:
            self.polls=None
    
    def test_poll_has_right_fields(self):
        if not models_importable:
            fail(self)
        
        P = Poll()
        assert check_attrs(P,['choice_set','question','pub_date','was_published_today'])
    
    def test_choice_has_right_fields(self):
        if not models_importable:
            fail(self)
        
        C = Choice()
        assert check_attrs(C,['choice','votes'])




## polls need to have pubdate and text
## choices need text and votes

## also choices need a 'is today' method.

## templates!
'''
Usually when I go about testing a Django application, there are 3 major parts that I test. Models, Views, and Template Tags. Templates are hard to test, and are generally more about aesthetics than code, so I tend not to think about actually testing Templates. This should cover most of the parts of your application that are standard. Of course, if your project has utils, forms, feeds, and other things like that, you can and should probably test those as well!

/ lives
something good at slash!

/other/lives 
something is good there!


try import models...
except....
assert false!



'''


