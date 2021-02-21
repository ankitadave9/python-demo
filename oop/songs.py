class Song:
    """class to represent songs
    
    Attributes:
        title (str): the title of the sing
        artist (Artist): an artist object representing the song of creator
        duration (int):the duration of the song in seconds. may be zero
    """

    def __init__(self, title, artist, duration=0):
        """song init method
    Args:
        title (str) : initialises the 'title' attributes
        artist (srt) :  an artist object representing the song's creator.
        duration (optional(int)) : initial value for the duration attributes.
        will default to zero if not specified.
    """
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """class to represent an album,using it's track list
    attributes:
    name(str) = the name of the album
    year (int) : the year was album was released.
    artist : (Artist) : the artist responsible for the album.if not specified,
    the artist will default to an artist with the name "various artists"
    tracks (list[song]): a list of the song on tne album.
    methods :
    add_Song : used to add a new song to album's track list.
     """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "various artists"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """add a song to the track list

        args:
        song(song):the title of a song to add.
        position(optional[int]): if specified,the song will be added to that position
        in the track list-inserting it between other song if necessary.
        otherwise, the song will be added to the end of the list.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = song(song, self.artist)
            if position is None:
                self.tracks.append(song)
            else:
                self.tracks.insert(position, song)


class Artist:
    """basic class to store artist details.
    attributes:
    name(srt) : the name of the artist.
    album (list[album]) : a list of the album by this artist.
     the list includes only those albums in this collection , it is
     not in exhaustive list of the artist's published album
    """
    def __init__(self, name):
        self.name = name
        self.album = []

    def add_album(self, album):
        """add a new album to the list

        args:
        album(album) : album object to the list.
        if the album is already present , it will not added again (although this is yet to implemented).
        """
        self.album.append(album)

    def add_song(self,name,year,title):
        """add a song in to collection
        this method will add a song in to collection . a new album will be created
        if it doesnt already excited
        args:
        name:name of the album
        year:the year the album was published
        title: title of the song
        """

        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + "not found")
            album_found = Album(name,year,self.name)
            self.add_album(album_found)
        else:
            print("found album " + name)

        album_found.add_song(title)


def find_object(field,object_list):
    for item in object_list:
        if item.name== field:
            return item
    return None


def load_data():
    artist_list = []

    with open("albums.txt", 'r') as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song")
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = artists(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    "create a check file from object for comparison with the original file"
    with open("checkfile.txt",'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.album:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.year}\t{2.name}"
                          .format(new_artist, new_album, new_song),file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("there are {} artists".format(len(artists)))

    create_checkfile(artists)
