from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from video_set.models import VideoFile

from car_wash_project.car_wash.detectobj.models import InferencedFrame


class InferencedFrameDetectionView(LoginRequiredMixin, DetailView):
    model = VideoFile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        frame_qs = self.get_object()
        frameset = frame_qs.frame_set
        frames_qs = frameset.frames.all()

        # For pagination GET request
        self.get_pagination(context, frame_qs)

        is_inf_frame = InferencedFrame.objects.filter(
            orig_image=frame_qs).exists()
        if is_inf_frame:
            inf_frame_qs = InferencedFrame.objects.get(orig_image=frame_qs)
            context['inf_img_qs'] = inf_frame_qs

        context["img_qs"] = frame_qs
        return context
