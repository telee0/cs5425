        CREATE TABLE tw_user (
            id INT NOT NULL AUTO_INCREMENT,
            created_at VARCHAR(30) DEFAULT NULL,
            description VARCHAR(200) DEFAULT NULL,
            user_id VARCHAR(30) DEFAULT NULL,
            location VARCHAR(20) DEFAULT NULL,
            name VARCHAR(30) DEFAULT NULL,
            pinned_tweet_id varchar(30) DEFAULT NULL,
            profile_image_url varchar(255) DEFAULT NULL,
            url VARCHAR(255) DEFAULT NULL,
            followers_count INT DEFAULT NULL,
            following_count INT DEFAULT NULL,
            username VARCHAR(20) DEFAULT NULL,
            tweet_count INT DEFAULT NULL,
            listed_count INT DEFAULT NULL,
            created DATETIME DEFAULT NULL,
            PRIMARY KEY (id),
            KEY username (username)
        );
