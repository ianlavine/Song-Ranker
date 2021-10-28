from string import capwords
import urllib.error as err
from urllib.request import urlopen as uReq
import certifi
import ssl
from bs4 import BeautifulSoup as soup

addons = ['musician', 'band', 'album']

def scrape_data(artist):
	addons.insert(2, rename(artist) + '_album')
	data = []
	page = grab_page(artist, addons)
	if page != None:
		albums = get_artist_albums(page)

		for album in albums:
			apage = grab_page(album, addons[2:])
			if apage != None:
				songs = get_album_songs(apage, album)
				if songs != None:
					data.append((songs, album))

	return data


def get_artist_albums(page_html):

	albums = []
	page_soup = soup(page_html, "html.parser")

	target = page_soup.find('h2',text="Discography")

	if target == None:
		target = page_soup.find('dl',text="Studio albums")

	if target == None:
		targets = page_soup.find_all("h2")
		for i in targets:
			nt = i.find(id="Discography")
			if nt != None:
				target = i
				break

	for sib in target.find_next_siblings():

		if sib.name=="ul":
			albums = sib.text.split('\n')
			break

		if sib.name=="table":
			table = sib
			rows = table.tbody.findAll('tr')
			for row in range(2, len(rows) -1):
				nss = rows[row].find_all('th')[0].text
				if len(nss) > 2:
					albums.append(nss)
			break

	cutAlbums = [album_cut(a) for a in albums]

	return(cutAlbums)

def get_album_songs(page_html, album):

	songs = []
	page_soup = soup(page_html, "html.parser")

	table = page_soup.find("table", class_="tracklist")
	if table == None:
		return None

	rows = table.tbody.findAll('tr')
	for row in rows:
		nss = row.find_all('td')
		if len(nss) > 1:
			songs.append(nss[0].text)

	return(songs)

def album_cut(album):
	no_n = album_backn_cut(album)
	no_year = album_year_cut(no_n)
	return no_year

def album_year_cut(album):
	newAlbum = ""
	for l in range(len(album) - 1, 0-1, -1):
		if album[l] == '(' and len(album) > l + 5 and album[l + 5] == ')':
			return album[:l]
	return album

def album_backn_cut(album):
	return album.strip()


def grab_page(search, addons):

	word = rename(search)
	my_url = ''
	for addon in addons:
		my_url = 'https://en.wikipedia.org/wiki/' + word + "_(" + addon + ")"
		try:
			uClient = uReq(my_url, context=ssl.create_default_context(cafile=certifi.where()))
			break
		except err.HTTPError as exception:
			my_url = 'https://en.wikipedia.org/wiki/' + word
	try:
		uClient = uReq(my_url, context=ssl.create_default_context(cafile=certifi.where()))
		page = uClient.read()
		uClient.close()
	except err.HTTPError as exception:
		"Album Or Artist Not Found"
		page = None

	return page

def rename(word):
	capitalised = capitalise(word)
	underscored = underscore(capitalised)
	return underscored

def underscore(word):
	break_word = word.split(' ')
	new_word = '_'.join(break_word)
	return(new_word)

def capitalise(word):
	cap_str = capwords(word)
	cap = list(cap_str)
	for l in range(1, len(cap) - 3):
		if cap[l] == ' ' and cap[l + 1] == 'O' and cap[l + 2] == 'f' and cap[l + 3] == ' ':
			cap[l + 1] = 'o'
		if cap[l] == ' ' and cap[l + 1] == 'A' and cap[l + 2] == ' ':
			cap[l + 1] = 'a'
		if cap[l] == ' ' and cap[l + 1] == 'I' and cap[l + 2] == 'n' and cap[l + 3] == ' ':
			cap[l + 1] = 'i'
		if cap[l] == ' ' and cap[l + 1] == 'T' and cap[l + 2] == 'h' and cap[l + 3] == 'e' and cap[
			l + 4] == ' ':
			cap[l + 1] = 't'
	cap_str = "".join(cap)

	return(cap_str)

# scrape_data(artist)