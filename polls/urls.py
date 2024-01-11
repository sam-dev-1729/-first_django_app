from django.urls import path

from .views import vote,IndexView,DetailView,ResultsView


app_name = "polls"

urlpatterns = [
    # path("", index, name="index"),
    path("", IndexView.as_view(), name="index"),

    # path("<int:question_id>/", detail, name="detail"),
        path("<int:pk>/", DetailView.as_view(), name="detail"),

    # path("<int:question_id>/results/", results, name="results"),
        path("<int:pk>/results/", ResultsView.as_view(), name="results"),
    # path("<int:question_id>/vote/", vote, name="vote"),
        path("<int:question_id>/vote/", vote, name="vote"),

]
