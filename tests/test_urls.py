# -*- coding: utf-8 -*-
from textile import Textile
import re

def test_urls():
    t = Textile()
    assert t.relURL("http://www.google.com/") == 'http://www.google.com/'

    result = t.links('fooobar "Google":http://google.com/foobar/ and hello world "flickr":http://flickr.com/photos/jsamsa/ ')
    expect = 'fooobar {0}2:shelve and hello world {0}4:shelve '.format(t.uid)
    assert result == expect

    result = t.links('""Open the door, HAL!"":https://xkcd.com/375/')
    expect = '{0}6:shelve'.format(t.uid)
    assert result == expect

    result = t.links('"$":http://domain.tld/test_[brackets]')
    expect = '{0}8:shelve'.format(t.uid)
    assert result == expect

    result = t.links('<em>"$":http://domain.tld/test_</em>')
    expect = '<em>{0}10:shelve</em>'.format(t.uid)
    assert result == expect

    expect = '"":test'
    result = t.links(expect)
    assert result == expect

    expect = '"$":htt://domain.tld'
    result = t.links(expect)
    assert result == expect

    result = t.shelveURL('')
    expect = ''
    assert result == expect

    result = t.retrieveURLs('{0}2:url'.format(t.uid))
    expect = ''
    assert result == expect

    result = t.encode_url('http://domain.tld/übermensch')
    expect = 'http://domain.tld/%C3%BCbermensch'
    assert result == expect

    result = t.parse('A link that starts with an h is "handled":/test/ incorrectly.')
    expect = '\t<p>A link that starts with an h is <a href="/test/">handled</a> incorrectly.</p>'
    assert result == expect

def test_rel_attribute():
    t = Textile(rel='nofollow')
    result = t.parse('"$":http://domain.tld')
    expect = '\t<p><a href="http://domain.tld" rel="nofollow">domain.tld</a></p>'
    assert result == expect
