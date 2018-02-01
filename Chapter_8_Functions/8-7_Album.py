# Write a function called make_album() that builds a dictionary describing a
# music album. The function should take in an artist name and an album title,
# and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album
# information correctly.
# Add an optional parameter to make_album() that allows you to store the number
# of tracks on an album. If the calling line includes a value for the number of
# tracks, add that value to the album's dictionary. Make at least one new
# function call that includes the number of tracks on an album.

#def make_album(artist_name, album_title):
#    """Return a dictionary containing information about an album."""
#    album = {'artist': artist_name, 'album': album_title}
#    return album

def make_album(artist_name, album_title, num_tracks = ''):
    """Return a full album neatly formatted"""
    if num_tracks:
        full_album = '\nThe album ' + album_title.title() + " by " + artist_name.title() + ' has ' + num_tracks + ' tracks.'

    else:
        full_album = artist_name.title() + ' has an album titled ' + album_title.title() + '.'

    return full_album

album_1 = make_album('frou frou', 'details')
album_2 = make_album('the all american rejects', 'move along')
album_3 = make_album('evanescence','fallen', '12')


print(album_1)
print(album_2)
print(album_3)
