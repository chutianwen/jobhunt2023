class Feature:
    def __init__(self, id):
        self.id = id

    def compute(self):
        pass

class User:

class Tweet:

class UserFeature(Feature)
    def __init__(self, user: User):

class TweetFeature(Feature)
    def __init__(self, tweet: Tweet):

class FeatureValue:

class FeatureStore
    def __init__(self, features):
        self.features = features
        self.stats = dict()
        self.logger = Logger()

    def get_data_record(self):
        data_record = defaultdict(FeatureValue)
        for feature in self.features:
            try:
                data_record[feature.id] = feature.compute()
                self.stats['success'] += 1
            except Exception as e:
                self.stats['fail'] += 1
                self.logger.warn(e)


# in production
def get_data_record(user, tweet):
    # shared feature dependency can be heavily cached.
    user_feature_x = UserFeatureX(user)
    user_feature_y = UserFeatureY(user)
    # ...
    tweet_feature_x = TweetFeatureX(tweet)
    tweet_feature_y = TweetFeatureY(tweet)

    features = Seq(user_feature_x, user_feature_y, tweet_feature_x, tweet_feature_y)
    feature_store = FeatureStore(features)
    data_record = feature_store.get_data_record()
    return (user.userId, data_record)