import pytest

from test_1.framework_1 import ProgrammingLanguages, SoupPage

MOST_USED_LANGUAGES_URL = (
    "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
)


@pytest.fixture
def programming_languages_table() -> list:
    most_used_langs_page = SoupPage(url=MOST_USED_LANGUAGES_URL)
    table_caption = "Programming languages used in most popular websites*"
    return most_used_langs_page.get_dataclass_table(caption=table_caption)


@pytest.fixture
def programming_languages_datatable() -> ProgrammingLanguages:
    most_used_langs_page = SoupPage(url=MOST_USED_LANGUAGES_URL)
    table_caption = "Programming languages used in most popular websites*"
    return most_used_langs_page.get_predefined_dataclass_table(caption=table_caption)
