(
  SELECT results FROM (
    SELECT u.name AS results
    FROM MovieRating r
    LEFT JOIN Users u ON r.user_id = u.user_id
    GROUP BY r.user_id
    ORDER BY COUNT(r.movie_id) DESC, u.name
    LIMIT 1
  ) AS top_user
)
UNION ALL
(
  SELECT results FROM (
    SELECT m.title AS results
    FROM MovieRating r
    LEFT JOIN Movies m ON r.movie_id = m.movie_id
    WHERE r.created_at LIKE '2020-02%'
    GROUP BY r.movie_id
    ORDER BY AVG(r.rating) DESC, m.title
    LIMIT 1
  ) AS top_movie
);
