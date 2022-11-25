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
        fields = ['video', 'box', 'car_set', 'cars_quantity']

    def get_cars_quantity(self, related_video):
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
