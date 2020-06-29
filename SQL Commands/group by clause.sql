-- albums by total track list, no album field
SELECT COUNT(*) FROM  Track
GROUP BY AlbumId;

-- albums by total track list, showing album ID as album field
SELECT AlbumId, COUNT(*) FROM Track
GROUP BY AlbumId;

-- albums by total track list, showing album name
SELECT Album.Title, COUNT(*) FROM Track
INNER JOIN Album ON Track.AlbumId = Album.AlbumId
GROUP BY Track.AlbumId;

-- albums by total track list, showing album ID as album field, showing min price of track on album
SELECT AlbumId, MIN(UnitPrice) FROM Track
GROUP BY AlbumId;

-- albums by total track list, showing album ID as album field, showing max price of track on album
SELECT AlbumId, MAX(UnitPrice) FROM Track
GROUP BY AlbumId;

-- albums by total track list, showing album ID as album field, showing total price of tracks on album
SELECT AlbumId, ROUND(SUM(UnitPrice), 2) FROM Track
GROUP BY AlbumId;

-- albums by total track list, showing album name as album field, showing min price of tracks on album
SELECT Album.Title, ROUND(SUM(UnitPrice), 2) FROM Track
INNER JOIN Album ON Track.AlbumId = Album.AlbumId
GROUP BY Track.AlbumId;