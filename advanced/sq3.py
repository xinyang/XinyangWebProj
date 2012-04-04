#!/usr/bin/env python
from bottle import route, run, request

import json
import pymongo

#database
#songs = open('songs.json', 'r').read()
db = Connection('localhost', '25521').mysite

def find_song(songid):
    """Accepts a songid (str).
    Looks it up in MongoDB.
    Returns a song (mongodb object(like a dict)).
    """
    return db.songs.find_one({'songid':i,})

@route('/todo')
def todo_list():
    starttime = time.time()
    i = request.GET['songid']
    new_title = request.GET.get('title', None)
    
    if new_title is not None:
        songs[i] = new_title
        json_string = json.dumps(songs)
        with open('songs.json', 'w') as f:
            f.write(json_string)
    
    #    song = find_song(i)
    #    song['title'] = new_title
    #    db.songs.save(song)

    #song = find_song(i)

    
    #t = songs['title']

    t = songs[i]
    stoptime = time.time()
    timing = stoptime - starttime
    output = {'api_version':'1.0', 'title':t, 'status': ok, 'time':timing}
    return str(t)

run()