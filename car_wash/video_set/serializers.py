from rest_framework import serializers

from video_set.models import VideoSet, VideoFile, Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    cars_quantity = serializers.SerializerMethodField()
    car_set = CarSerializer(many=True, read_only=True)

    class Meta:
        model = VideoFile
        fields = ['video', 'car_set', 'cars_quantity']

    def get_cars_quantity(self, related_video):
        return Car.objects.filter(related_video=related_video).count()


class VideoSetSerializer(serializers.ModelSerializer):
    videofile_set = VideoSerializer(many=True, read_only=True)
    # videos = serializers.SerializerMethodField()
    set_interval = serializers.SerializerMethodField()

    # cars_quantity = serializers.SerializerMethodField()

    class Meta:
        model = VideoSet
        fields = ['set_name', 'set_start_date', 'set_end_date', 'set_interval', 'videofile_set']

    def get_set_interval(self, request):
        set_interval = 'c %s до %s' % (request.set_start_date, request.set_end_date)
        return set_interval.strip()

    # def get_cars_quantity(self, related_video):
    #     return Car.objects.filter(related_video=related_video).count()

    # def get_videos(self, video_set):
    #     video_info = VideoFile.objects.filter(video_set=video_set).values_list('video'), VideoFile.objects.filter(
    #         video_set=video_set).values_list('video', 'car').count()
    #
    #     return video_info
