SELECT A.slug, A.twitter_username,
	B.user_id, B.followers_count,
	C.tweet_id, C.author_id, C.query
FROM opensea_top100 as A, tw_user as B, tw_tweet as C
WHERE A.twitter_username = B.username
	AND B.user_id = C.author_id
	AND (A.slug = 'cryptopunks' OR A.slug = 'boredapeyachtclub')
ORDER BY A.id DESC
LIMIT 20
;


SELECT author_id, tweet_id, query, substring(text, 1, 20), retweet_count, like_count
FROM tw_tweet
WHERE retweet_count > 10000
ORDER BY id DESC LIMIT 30
;


SELECT id, asset_collection_image_url
FROM opensea_event
ORDER BY id DESC
LIMIT 10
;
