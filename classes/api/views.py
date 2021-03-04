from classes.models import Lesson, Subject
# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

# from classes.api.serializers import LessonSerializer, SubjectSerializer


# from rest_framework import viewsets

# class LessonViewSet(viewsets.ModelViewSet):
#     serializer_class = LessonSerializer
#     queryset = Lesson.objects.all()
#

# class SubjectListView(ListAPIView):
#     serializer_class = SubjectSerializer
#     queryset = Subject.objects.all()
#
#
# class LessonCreateView(CreateAPIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer
#
#
# class LessonUpdateView(UpdateAPIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer
#
#
# class LessonListView(ListAPIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer
#
#
# class LessonDetailView(RetrieveAPIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer
#
#
# class LessonDeleteView(DestroyAPIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer
