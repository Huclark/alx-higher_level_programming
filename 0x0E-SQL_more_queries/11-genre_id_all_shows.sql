-- Script that ists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL

-- Select the columns to retrieve data from
SELECT tv_shows.title, tv_show_genres.genre_id
-- Select the table which the linking will be based on
FROM tv_show_genres
RIGHT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
