-- Script that lists all shows contained in 'hbtn_0d_tvshows'
-- that have at least on genre linked.
-- Each record should display: 'tv_shows.title' - 'tv_show_genres.genre_id'

-- Select the column to retrieve data from
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows.title
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
