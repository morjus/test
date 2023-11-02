import pytest

import pytest_check as check

from test_1.utils import clean_string

ERR_MSG = (
    "{websites} (Frontend:{front_end}|Backend:{back_end}) has {popularity} unique visitors per month. "
    "(Expected more than {value})"
)


@pytest.mark.parametrize(
    "value",
    [
        10**7,
        1.5 * (10**7),
        5 * (10**7),
        10**8,
        5 * (10**8),
        10**9,
        1 * 5 * (10**9),
    ],
)
def test_popularity(programming_languages_table, value):
    table = programming_languages_table
    for row in table:
        popularity = int(clean_string(string=row.popularity))
        check.greater(
            a=popularity,
            b=value,
            msg=ERR_MSG.format(
                websites=row.websites,
                front_end=row.front_end,
                back_end=row.back_end,
                popularity=popularity,
                value=value,
            ),
        )


@pytest.mark.parametrize(
    "value",
    [
        10**7,
        1.5 * (10**7),
        5 * (10**7),
        10**8,
        5 * (10**8),
        10**9,
        1 * 5 * (10**9),
    ],
)
def test_popularity_predefined(programming_languages_datatable, value):
    table = programming_languages_datatable
    for row in table:
        popularity = row.popularity
        check.greater(
            a=popularity,
            b=value,
            msg=ERR_MSG.format(
                websites=row.websites,
                front_end=row.front_end,
                back_end=row.back_end,
                popularity=popularity,
                value=value,
            ),
        )
