from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from Course.views import CourseListViewSet, CourseDetailViewSet, SyllabusViewSet, LessonViewSet, PageViewSet, ParagraphViewSet
from Class.views import ClassViewSet, PostViewSet, CommentViewSet
from Mocktest.views import MockTestViewSet, MockQuestionsViewSet, MockTestScoresViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseListViewSet)
router.register(r'course/details', CourseDetailViewSet)
router.register(r'syllabi', SyllabusViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'pages', PageViewSet)
router.register(r'paragraphs', ParagraphViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet)
router.register(r'mocktest', MockTestViewSet)
router.register(r'mocktest/questions', MockQuestionsViewSet)
router.register(r'mocktest/scores', MockTestScoresViewSet)


#pagkuha og indibidwal nga mga kurso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^syllabi/(?P<course_id>[^/.]+)/$', SyllabusViewSet.as_view({'get': 'by_course'})),
    re_path(r'^lessons/(?P<course_id>[^/.]+)/$', LessonViewSet.as_view({'get': 'by_course'})),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)