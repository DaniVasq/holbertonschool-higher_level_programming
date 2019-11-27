-- import database dump to my server
SELECT tv_show.title, tv_show_genres.genre_id
FROM tv_show, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
