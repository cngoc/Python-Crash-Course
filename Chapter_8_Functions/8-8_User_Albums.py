# Start with your program from Exercise 8-7. Write a while loop that allows
# users to enter an album's artist and title. Once you have that information,
# call make_album() with the user's input and print the dictionary that's
# created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title):
    """Return a dictionary containing information about an album."""
    album = {'artist': artist_name, 'album': album_title}
    return album

while True:
    print("\n\nEnter 'q' at any time to quit")
    album = input("\nEnter an album name: ")
    if album =='q':
        break

    artist = input("Enter the artist's name of " + album + ": ")
    if artist == 'q':
        break

    print("\nYour response has been stored in the dictionary: ")
    print(make_album(album, artist))
