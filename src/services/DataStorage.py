

class DataStorage:
    @staticmethod
    def store_data(repository, channel, videos, comments_by_video):
        repository.save(channel, videos, comments_by_video)