-- Script that lists all shows contained in 'hbtn_0d_tvshows'
-- that have at least on genre linked.
-- Each record should display: 'tv_shows.title' - 'tv_show_genres.genre_id'

-- Select the column to retrieve data from
SELECT tv_shows.title, tv_show_genres.genre_id
-- Select the table which the linking will be based on
FROM tv_show_genres
-- Use inner join to list all data
INNER JOIN tv_shows
-- Specify the rule on which the tables should be joined
ON tv_shows.id = tv_show_genres.show_id
-- Order in ascending order by title and genre_id in
-- tv_shows and tv_show_genres table, respectively
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
