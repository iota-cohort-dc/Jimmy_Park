SELECT first_name, tweet
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id