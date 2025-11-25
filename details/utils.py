from django.contrib.postgres.search import SearchVector, SearchHeadline, SearchQuery, SearchRank

from .models import CityWeather


def q_search(query):
    vector = SearchVector("name", "created_at")
    query = SearchQuery(query)
    result = CityWeather.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>',
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "created_at",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>',
        )
    )
    return result
