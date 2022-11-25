from rest_framework import serializers

from video_set.models import VideoSet, VideoFile, Car


<<<<<<< HEAD
class VideoSetSerializer(serializers.ModelSerializer):
    # videos = serializers.SerializerMethodField()
    set_date = serializers.SerializerMethodField()
    cars_quantity = serializers.SerializerMethodField()

    class Meta:
        model = VideoSet
        fields = ['set_name', 'set_date', 'cars_quantity']

    @staticmethod
    def get_set_date(request):
        set_date = request.set_date
        return set_date

    @staticmethod
    def get_cars_quantity(related_video):
        return Car.objects.filter(related_video=related_video).count()

    # def get_videos(self, video_set):
    #     video_info = VideoFile.objects.filter(video_set=video_set).values_list('video'), VideoFile.objects.filter(
    #         video_set=video_set).values_list('video', 'car').count()
    #
    #     return video_info
=======
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
>>>>>>> 65edd09ba869f8eb91373fc0caf0ae21c25f39f6


class VideoSerializer(serializers.ModelSerializer):
    cars_quantity = serializers.SerializerMethodField()
    car_set = CarSerializer(many=True, read_only=True)

    class Meta:
        model = VideoFile
        fields = ['video', 'box', 'car_set', 'cars_quantity']

    @staticmethod
    def get_cars_quantity(related_video):
        return Car.objects.filter(related_video=related_video).count()


class VideoSetSerializer(serializers.ModelSerializer):
    videofile_set = VideoSerializer(many=True, read_only=True)

    # set_interval = serializers.SerializerMethodField()

    class Meta:
        model = VideoSet
        fields = ['set_name', 'set_date', 'videofile_set']

    # def get_set_interval(self, request):
    #     set_interval = 'c %s до %s' % (request.set_start_date, request.set_end_date)
    #     return set_interval.strip()
