"""

CS4225/5425 project

[2022032901]

https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html
https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html

"""

import mysql.connector
from hidden import mysql as my
from mysql_q import db_queries as dbq

verbose, debug = True, False


def save_debug_msg(msg):
    print("save_debug_msg: {}".format(msg))


def save_error_msg(msg):
    print("save_error_msg: {}".format(msg))


def init():
    # https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users
    #
    sql =\
        """
        CREATE TABLE opensea_event (
            id INT NOT NULL AUTO_INCREMENT,
            approved_account VARCHAR(255) DEFAULT NULL,
            asset_id VARCHAR(30) DEFAULT NULL,
            asset_num_sales INT DEFAULT NULL,
            asset_background_color VARCHAR(20) DEFAULT NULL,
            asset_image_url TEXT(500) DEFAULT NULL,
            asset_image_preview_url TEXT(500) DEFAULT NULL,
            asset_image_thumbnail_url TEXT(500) DEFAULT NULL,
            asset_image_original_url TEXT(500) DEFAULT NULL,
            asset_animation_url TEXT(500) DEFAULT NULL,
            asset_animation_original_url TEXT(500) DEFAULT NULL,
            asset_name VARCHAR(100) DEFAULT NULL,
            asset_description TEXT(5000) DEFAULT NULL,
            asset_external_link VARCHAR(255) DEFAULT NULL,
            asset_asset_contract_address VARCHAR(120) DEFAULT NULL,
            asset_asset_contract_asset_contract_type VARCHAR(30) DEFAULT NULL,
            asset_asset_contract_created_date VARCHAR(30) DEFAULT NULL,
            asset_asset_contract_name VARCHAR(100) DEFAULT NULL,
            asset_asset_contract_nft_version VARCHAR(10) DEFAULT NULL,
            asset_asset_contract_opensea_version VARCHAR(10) DEFAULT NULL,
            asset_asset_contract_owner VARCHAR(30) DEFAULT NULL,
            asset_asset_contract_schema_name VARCHAR(20) DEFAULT NULL,
            asset_asset_contract_symbol VARCHAR(50) DEFAULT NULL,
            asset_asset_contract_total_supply INT DEFAULT NULL,
            asset_asset_contract_description TEXT(5000) DEFAULT NULL,
            asset_asset_contract_external_link VARCHAR(255) DEFAULT NULL,
            asset_asset_contract_image_url TEXT(500) DEFAULT NULL,
            asset_asset_contract_default_to_fiat VARCHAR(10) DEFAULT NULL,
            asset_asset_contract_dev_buyer_fee_basis_points INT DEFAULT NULL,
            asset_asset_contract_dev_seller_fee_basis_points INT DEFAULT NULL,
            asset_asset_contract_only_proxied_transfers VARCHAR(10) DEFAULT NULL,
            asset_asset_contract_opensea_buyer_fee_basis_points INT DEFAULT NULL,
            asset_asset_contract_opensea_seller_fee_basis_points INT DEFAULT NULL,
            asset_asset_contract_buyer_fee_basis_points INT DEFAULT NULL,
            asset_asset_contract_seller_fee_basis_points INT DEFAULT NULL,
            asset_asset_contract_payout_address VARCHAR(120) DEFAULT NULL,
            asset_permalink VARCHAR(255) DEFAULT NULL,
            asset_collection_banner_image_url TEXT(500) DEFAULT NULL,
            asset_collection_chat_url TEXT(500) DEFAULT NULL,
            asset_collection_created_date VARCHAR(30) DEFAULT NULL,
            asset_collection_default_to_fiat VARCHAR(10) DEFAULT NULL,
            asset_collection_description TEXT(5000) DEFAULT NULL,
            asset_collection_dev_buyer_fee_basis_points INT DEFAULT NULL,
            asset_collection_dev_seller_fee_basis_points INT DEFAULT NULL,
            asset_collection_discord_url TEXT(500) DEFAULT NULL,
            asset_collection_display_data_card_display_style VARCHAR(20) DEFAULT NULL,
            asset_collection_external_url TEXT(500) DEFAULT NULL,
            asset_collection_featured VARCHAR(10) DEFAULT NULL,
            asset_collection_featured_image_url TEXT(500) DEFAULT NULL,
            asset_collection_hidden VARCHAR(10) DEFAULT NULL,
            asset_collection_safelist_request_status VARCHAR(20) DEFAULT NULL,
            asset_collection_image_url TEXT(500) DEFAULT NULL,
            asset_collection_is_subject_to_whitelist VARCHAR(10) DEFAULT NULL,
            asset_collection_large_image_url TEXT(500) DEFAULT NULL,
            asset_collection_medium_username VARCHAR(255) DEFAULT NULL,
            asset_collection_name VARCHAR(100) DEFAULT NULL,
            asset_collection_only_proxied_transfers VARCHAR(10) DEFAULT NULL,
            asset_collection_opensea_buyer_fee_basis_points INT DEFAULT NULL,
            asset_collection_opensea_seller_fee_basis_points INT DEFAULT NULL,
            asset_collection_payout_address VARCHAR(120) DEFAULT NULL,
            asset_collection_require_email VARCHAR(10) DEFAULT NULL,
            asset_collection_short_description VARCHAR(255) DEFAULT NULL,
            asset_collection_slug VARCHAR(100) DEFAULT NULL,
            asset_collection_telegram_url TEXT(500) DEFAULT NULL,
            asset_collection_twitter_username VARCHAR(30) DEFAULT NULL,
            asset_collection_instagram_username VARCHAR(30) DEFAULT NULL,
            asset_collection_wiki_url TEXT(500) DEFAULT NULL,
            asset_collection_is_nsfw VARCHAR(10) DEFAULT NULL,
            asset_decimals INT DEFAULT NULL,
            asset_token_metadata TEXT(65535) DEFAULT NULL,
            asset_is_nsfw VARCHAR(10) DEFAULT NULL,
            asset_owner_user_username VARCHAR(80) DEFAULT NULL,
            asset_owner_profile_img_url TEXT(500) DEFAULT NULL,
            asset_owner_address VARCHAR(120) DEFAULT NULL,
            asset_owner_config VARCHAR(255) DEFAULT NULL, 
            asset_token_id VARCHAR(100) DEFAULT NULL,
            asset_bundle VARCHAR(255) DEFAULT NULL,
            auction_type VARCHAR(20) DEFAULT NULL,
            bid_amount VARCHAR(255) DEFAULT NULL,
            collection_slug VARCHAR(100) DEFAULT NULL,
            contract_address VARCHAR(120) DEFAULT NULL,
            created_date VARCHAR(30) DEFAULT NULL,
            custom_event_name VARCHAR(30) DEFAULT NULL,
            dev_fee_payment_event VARCHAR(30) DEFAULT NULL,
            dev_seller_fee_basis_points INT DEFAULT NULL,
            duration VARCHAR(30) DEFAULT NULL,
            ending_price INT DEFAULT NULL,
            event_type VARCHAR(20) DEFAULT NULL,
            from_account VARCHAR(255) DEFAULT NULL,
            event_id VARCHAR(30) DEFAULT NULL,
            is_private VARCHAR(10) DEFAULT NULL,
            owner_account VARCHAR(255) DEFAULT NULL,
            payment_token_symbol VARCHAR(10) DEFAULT NULL,
            payment_token_address VARCHAR(120) DEFAULT NULL,
            payment_token_image_url TEXT(500) DEFAULT NULL,
            payment_token_name VARCHAR(30) DEFAULT NULL,
            payment_token_decimals INT DEFAULT NULL,
            payment_token_eth_price DOUBLE DEFAULT NULL,
            payment_token_usd_price DOUBLE DEFAULT NULL,
            quantity DECIMAL(30) DEFAULT NULL,
            seller_user_username VARCHAR(80) DEFAULT NULL,
            seller_profile_img_url TEXT(500) DEFAULT NULL,
            seller_address VARCHAR(120) DEFAULT NULL,
            seller_config VARCHAR(255) DEFAULT NULL, 
            starting_price INT DEFAULT NULL,
            to_account VARCHAR(255) DEFAULT NULL,
            total_price DECIMAL(30) DEFAULT NULL,
            transaction_block_hash VARCHAR(120) DEFAULT NULL,
            transaction_block_number VARCHAR(20) DEFAULT NULL,
            transaction_from_account_user_username VARCHAR(80) DEFAULT NULL,
            transaction_from_account_profile_img_url TEXT(500) DEFAULT NULL,
            transaction_from_account_address VARCHAR(120) DEFAULT NULL,
            transaction_from_account_config VARCHAR(255) DEFAULT NULL, 
            transaction_id VARCHAR(30) DEFAULT NULL,
            transaction_timestamp VARCHAR(30) DEFAULT NULL,
            transaction_to_account_user VARCHAR(255) DEFAULT NULL,
            transaction_to_account_profile_img_url TEXT(500) DEFAULT NULL,
            transaction_to_account_address VARCHAR(120) DEFAULT NULL,
            transaction_to_account_config VARCHAR(255) DEFAULT NULL, 
            transaction_transaction_hash VARCHAR(120) DEFAULT NULL,
            transaction_transaction_index VARCHAR(20) DEFAULT NULL,
            winner_account_user_username VARCHAR(80) DEFAULT NULL,
            winner_account_profile_img_url TEXT(500) DEFAULT NULL,
            winner_account_address VARCHAR(120) DEFAULT NULL,
            winner_account_config VARCHAR(255) DEFAULT NULL, 
            listing_time VARCHAR(30) DEFAULT NULL,
            created DATETIME DEFAULT NULL,
            PRIMARY KEY (id),
            KEY event_id (event_id)            
        );

        CREATE TABLE opensea_top100 (
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(100) DEFAULT NULL,
            slug VARCHAR(100) DEFAULT NULL,
            logo VARCHAR(255) DEFAULT NULL,
            one_day_volume DOUBLE DEFAULT NULL,
            one_day_change DOUBLE DEFAULT NULL,
            one_day_sales FLOAT DEFAULT NULL,
            one_day_average_price DOUBLE DEFAULT NULL,
            seven_day_volume DOUBLE DEFAULT NULL,
            seven_day_change DOUBLE DEFAULT NULL,
            seven_day_sales FLOAT DEFAULT NULL,
            seven_day_average_price DOUBLE DEFAULT NULL,
            thirty_day_volume DOUBLE DEFAULT NULL,
            thirty_day_change DOUBLE DEFAULT NULL,
            thirty_day_sales FLOAT DEFAULT NULL,
            thirty_day_average_price DOUBLE DEFAULT NULL,
            total_volume DOUBLE DEFAULT NULL,
            total_sales FLOAT DEFAULT NULL,
            total_supply FLOAT DEFAULT NULL,
            count FLOAT DEFAULT NULL,
            num_owners INT DEFAULT NULL,
            average_price DOUBLE DEFAULT NULL,
            num_reports INT DEFAULT NULL,
            market_cap DOUBLE DEFAULT NULL,
            floor_price DOUBLE DEFAULT NULL,
            created DATETIME DEFAULT NULL,
            PRIMARY KEY (id),
            KEY slug (slug)            
        );

        ALTER TABLE opensea_top100
            ADD banner_image_url VARCHAR(255) DEFAULT NULL,
            ADD created_date VARCHAR(30) DEFAULT NULL,
            ADD description TEXT(5000) DEFAULT NULL,
            ADD discord_url VARCHAR(255) DEFAULT NULL,
            ADD external_url VARCHAR(255) DEFAULT NULL,
            ADD image_url VARCHAR(255) DEFAULT NULL,
            ADD large_image_url VARCHAR(255) DEFAULT NULL,
            ADD medium_username VARCHAR(30) DEFAULT NULL,
            ADD short_description VARCHAR(255) DEFAULT NULL,
            ADD telegram_url VARCHAR(255) DEFAULT NULL,
            ADD twitter_username VARCHAR(30) DEFAULT NULL,
            ADD instagram_username VARCHAR(30) DEFAULT NULL,
            ADD wiki_url VARCHAR(255) DEFAULT NULL
        ;

        CREATE TABLE opensea_top100_new (
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(100) DEFAULT NULL,
            slug VARCHAR(100) DEFAULT NULL,
            logo VARCHAR(255) DEFAULT NULL,
            one_day_volume DOUBLE DEFAULT NULL,
            one_day_change DOUBLE DEFAULT NULL,
            one_day_sales FLOAT DEFAULT NULL,
            one_day_average_price DOUBLE DEFAULT NULL,
            seven_day_volume DOUBLE DEFAULT NULL,
            seven_day_change DOUBLE DEFAULT NULL,
            seven_day_sales FLOAT DEFAULT NULL,
            seven_day_average_price DOUBLE DEFAULT NULL,
            thirty_day_volume DOUBLE DEFAULT NULL,
            thirty_day_change DOUBLE DEFAULT NULL,
            thirty_day_sales FLOAT DEFAULT NULL,
            thirty_day_average_price DOUBLE DEFAULT NULL,
            total_volume DOUBLE DEFAULT NULL,
            total_sales FLOAT DEFAULT NULL,
            total_supply FLOAT DEFAULT NULL,
            count FLOAT DEFAULT NULL,
            num_owners INT DEFAULT NULL,
            average_price DOUBLE DEFAULT NULL,
            num_reports INT DEFAULT NULL,
            market_cap DOUBLE DEFAULT NULL,
            floor_price DOUBLE DEFAULT NULL,
            banner_image_url VARCHAR(255) DEFAULT NULL,
            created_date VARCHAR(30) DEFAULT NULL,
            description TEXT(5000) DEFAULT NULL,
            discord_url VARCHAR(255) DEFAULT NULL,
            external_url VARCHAR(255) DEFAULT NULL,
            image_url VARCHAR(255) DEFAULT NULL,
            large_image_url VARCHAR(255) DEFAULT NULL,
            medium_username VARCHAR(30) DEFAULT NULL,
            short_description VARCHAR(255) DEFAULT NULL,
            telegram_url VARCHAR(255) DEFAULT NULL,
            twitter_username VARCHAR(30) DEFAULT NULL,
            instagram_username VARCHAR(30) DEFAULT NULL,
            wiki_url VARCHAR(255) DEFAULT NULL,
            created DATETIME DEFAULT NULL,
            PRIMARY KEY (id),
            KEY slug (slug)            
        );
        
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
                
        """

    return sql


db_fields = {
    'opensea_event': {
        'fields': [
            'approved_account', 'asset_id', 'asset_num_sales', 'asset_background_color',
            'asset_image_url', 'asset_image_preview_url', 'asset_image_thumbnail_url', 'asset_image_original_url',
            'asset_animation_url', 'asset_animation_original_url', 'asset_name', 'asset_description',
            'asset_external_link',
            'asset_asset_contract_address', 'asset_asset_contract_asset_contract_type',
            'asset_asset_contract_created_date', 'asset_asset_contract_name', 'asset_asset_contract_nft_version',
            'asset_asset_contract_opensea_version', 'asset_asset_contract_owner', 'asset_asset_contract_schema_name',
            'asset_asset_contract_symbol', 'asset_asset_contract_total_supply', 'asset_asset_contract_description',
            'asset_asset_contract_external_link', 'asset_asset_contract_image_url',
            'asset_asset_contract_default_to_fiat', 'asset_asset_contract_dev_buyer_fee_basis_points',
            'asset_asset_contract_dev_seller_fee_basis_points', 'asset_asset_contract_only_proxied_transfers',
            'asset_asset_contract_opensea_buyer_fee_basis_points',
            'asset_asset_contract_opensea_seller_fee_basis_points',
            'asset_asset_contract_buyer_fee_basis_points', 'asset_asset_contract_seller_fee_basis_points',
            'asset_asset_contract_payout_address', 'asset_permalink', 'asset_collection_banner_image_url',
            'asset_collection_chat_url', 'asset_collection_created_date', 'asset_collection_default_to_fiat',
            'asset_collection_description', 'asset_collection_dev_buyer_fee_basis_points',
            'asset_collection_dev_seller_fee_basis_points', 'asset_collection_discord_url',
            'asset_collection_display_data_card_display_style', 'asset_collection_external_url',
            'asset_collection_featured', 'asset_collection_featured_image_url', 'asset_collection_hidden',
            'asset_collection_safelist_request_status', 'asset_collection_image_url',
            'asset_collection_is_subject_to_whitelist', 'asset_collection_large_image_url',
            'asset_collection_medium_username', 'asset_collection_name', 'asset_collection_only_proxied_transfers',
            'asset_collection_opensea_buyer_fee_basis_points', 'asset_collection_opensea_seller_fee_basis_points',
            'asset_collection_payout_address', 'asset_collection_require_email', 'asset_collection_short_description',
            'asset_collection_slug', 'asset_collection_telegram_url', 'asset_collection_twitter_username',
            'asset_collection_instagram_username', 'asset_collection_wiki_url', 'asset_collection_is_nsfw',
            'asset_decimals', 'asset_token_metadata', 'asset_is_nsfw', 'asset_owner_user_username',
            'asset_owner_profile_img_url', 'asset_owner_address', 'asset_owner_config', 'asset_token_id',
            'asset_bundle', 'auction_type', 'bid_amount', 'collection_slug', 'contract_address', 'created_date',
            'custom_event_name', 'dev_fee_payment_event', 'dev_seller_fee_basis_points', 'duration', 'ending_price',
            'event_type', 'from_account', 'event_id', 'is_private', 'owner_account',
            'payment_token_symbol', 'payment_token_address', 'payment_token_image_url', 'payment_token_name',
            'payment_token_decimals', 'payment_token_eth_price', 'payment_token_usd_price',
            'quantity', 'seller_user_username', 'seller_profile_img_url', 'seller_address', 'seller_config',
            'starting_price', 'to_account', 'total_price',
            'transaction_block_hash', 'transaction_block_number',
            'transaction_from_account_user_username', 'transaction_from_account_profile_img_url',
            'transaction_from_account_address', 'transaction_from_account_config', 'transaction_id',
            'transaction_timestamp', 'transaction_to_account_user', 'transaction_to_account_profile_img_url',
            'transaction_to_account_address', 'transaction_to_account_config', 'transaction_transaction_hash',
            'transaction_transaction_index', 'winner_account_user_username', 'winner_account_profile_img_url',
            'winner_account_address', 'winner_account_config', 'listing_time'
        ]
    },
    'opensea_top100_old': {
        'fields': ['name', 'slug', 'logo',
                   'one_day_volume', 'one_day_change', 'one_day_sales', 'one_day_average_price',
                   'seven_day_volume', 'seven_day_change', 'seven_day_sales', 'seven_day_average_price',
                   'thirty_day_volume', 'thirty_day_change', 'thirty_day_sales', 'thirty_day_average_price',
                   'total_volume', 'total_sales', 'total_supply', 'count',
                   'num_owners', 'average_price', 'num_reports', 'market_cap', 'floor_price']

    },
    'opensea_top100': {
        'fields': ['name', 'slug', 'logo',
                   'one_day_volume', 'one_day_change', 'one_day_sales', 'one_day_average_price',
                   'seven_day_volume', 'seven_day_change', 'seven_day_sales', 'seven_day_average_price',
                   'thirty_day_volume', 'thirty_day_change', 'thirty_day_sales', 'thirty_day_average_price',
                   'total_volume', 'total_sales', 'total_supply', 'count',
                   'num_owners', 'average_price', 'num_reports', 'market_cap', 'floor_price',
                   'banner_image_url', 'created_date', 'description',
                   'discord_url', 'external_url', 'image_url', 'large_image_url', 'medium_username',
                   'short_description', 'telegram_url', 'twitter_username', 'instagram_username', 'wiki_url']

    },
    'tw_user': {
        'fields': ['created_at', 'description', 'user_id',
                   'location', 'name', 'pinned_tweet_id',
                   'profile_image_url', 'url', 'followers_count', 'following_count',
                   'username', 'tweet_count', 'listed_count']
    },
    'tw_tweet': {
        'fields': ['conversation_id', 'created_at', 'author_id', 'tweet_id', 'query', 'text', 'path',
                   'retweet_count', 'reply_count', 'like_count', 'quote_count']
    },
}


def db_cmd(*args):
    cmd = args[0]
    if cmd not in dbq:
        return False

    if debug:
        save_debug_msg(cmd)

    cmd_type = dbq[cmd]['type']
    if cmd_type in ['D', 'I', 'S', 'U']:
        arg_lst = [dbq[cmd]['sql']] + list(args)[1:]
        args = tuple(arg_lst)

    if debug:
        print("db_cmd: args =", args)

    return cmd_switch[dbq[cmd]['type']](*args)


def db_delete():
    # to be imeplemented
    pass


def db_insert(sql, fields, values):
    for i, value in enumerate(values):

        # logic to handle data types in python
        #
        if value is None:
            value = ""
        elif not isinstance(value, str):
            value = str(value)

        if len(value) > 0:
            values[i] = "'" + value.replace("'", "''") + "'"
        else:
            values[i] = 'NULL'

    field_lst = ', '.join(fields)
    value_lst = ', '.join(values)

    sql = sql % (field_lst, value_lst)

    if debug:
        save_debug_msg('db_insert: ' + sql)

    try:
        cur.execute(sql)
        cnx.commit()
    except mysql.connector.Error as err:
        save_error_msg("{0}: {1}".format(sql, err))

    return cur.lastrowid


def db_search():
    # to be implemented
    pass


def db_select(sql):
    cur.execute(sql)
    return cur.fetchall()

def db_update():
    # to be implemented
    pass


cmd_switch = {
    'D': db_delete,
    'F': db_search,
    'I': db_insert,
    'S': db_select,
    'U': db_update
}


cnx = mysql.connector.connect(**my)
cur = cnx.cursor()
# cur.close()
# cnx.close()
