# Gplay Documentation

## Introduction

This page shows all of the endpoints and explains what they do for the
	gplay api. For v1.0 no error information will be shown, any new versions should add
	error information so that the end user knows how to handle errors.
	
All endpoints should be authenticated with your google account. This api has no
	authentication of it's own. Information is not stored and passed directly to the google play api.
	
# Endpoints
## About
This endpoint gathers information about the api

`GET /about`

## Account Info
This endpoint gives general information about the user's account, such as whether or not
	they are authenticated and if they are subscribed to gplay all access
	
### Query Parameters
un - The username for the google account -required

pw - The password for the google account -required

`GET /account/info?un=foo@google.com&pw=myPassword`

## Playlists (Get All)
This endpoint gathers all playlists from the users account, including the deleted playlists if specified.

### Query Parameters
un - The username for the google account -required

pw - The password for the google account -required

include-deleted - True if you want to include the playlists that the user has previously deleted -defaults to false

`GET /playlists?un=foo@google.com&pw=myPassword&include-deleted=true`

## Search
Allows the user to search google play for songs, playlists, artists, etc.

### Query Parameters
un - The username for the google account -required

pw - The password for the google account -required

q - The search query for the api

`GET /search?un=foo@google.com&pw=myPassword&q=aerosmith`

---

_&copy; 2016 Christian Andersen and Indiscrimusic, All rights reserved_

