        CREATE TABLE tw_tweet (
            id INT NOT NULL AUTO_INCREMENT,
            conversation_id VARCHAR(30) DEFAULT NULL,                
            created_at VARCHAR(30) DEFAULT NULL,            
            author_id VARCHAR(30) DEFAULT NULL,
            tweet_id VARCHAR(30) DEFAULT NULL,
            query VARCHAR(255) DEFAULT NULL,
            text VARCHAR(500) DEFAULT NULL,
            path VARCHAR(255) DEFAULT NULL,                                    
            retweet_count INT DEFAULT NULL,
            reply_count INT DEFAULT NULL,
            like_count INT DEFAULT NULL,
            quote_count INT DEFAULT NULL,
            created DATETIME DEFAULT NULL,
            PRIMARY KEY (id),
            KEY author_id (author_id)
        );
