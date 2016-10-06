import tweepy
import argparse
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('/etc/stwitto/config.ini')
consumer_key = config.get('twitter_auth_config', 'consumer_key')
consumer_secret = config.get('twitter_auth_config', 'consumer_secret')
access_token = config.get('twitter_auth_config', 'access_token')
access_token_secret = config.get('twitter_auth_config', 'access_token_secret')


def get_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def main():
    parser = argparse.ArgumentParser(description='Automatic Twitter Tweets through CLI')
    parser.add_argument('--tweet', nargs='+', help='your tweet goes here')
    parser.add_argument('--image',  help='your tweet image goes here')
    args = parser.parse_args()
    api = get_api()
    if args.tweet and args.image:
        tweet = ' '.join(args.tweet)
        status = api.update_with_media(args.image, tweet)
    elif args.tweet:
        tweet = ' '.join(args.tweet)
        status = api.update_status(status=tweet)
    else:
        print('Expected an Argument')
        parser.print_help()


if __name__ == "__main__":
    main()
