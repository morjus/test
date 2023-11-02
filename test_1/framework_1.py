from __future__ import annotations

from collections import UserList
from dataclasses import dataclass, make_dataclass, field
from typing import Union

import bs4
import httpx
from bs4 import BeautifulSoup

from test_1.utils import clean_strings, clean_string


@dataclass
class SoupPage:
    url: str
    page: bs4.BeautifulSoup = None

    def __post_init__(self):
        self.page = self.get_page(url=self.url)

    def get_page(self, url: str) -> bs4.BeautifulSoup:
        html_page = httpx.get(url).text
        soup = BeautifulSoup(html_page, "lxml")
        return soup

    def get_table_by_caption(self, caption: str) -> bs4.element:
        table = None
        for page_caption in self.page.find_all("caption"):
            if page_caption.get_text().strip() == caption:
                table = page_caption.find_parent("table")
        if table:
            return table
        else:
            raise ValueError(f"Table {caption} was not wound")

    def get_dataclass_table(self, caption: str) -> list:
        """Dataclass table without defining"""
        bs4_table = self.get_table_by_caption(caption=caption)
        result = []
        headers = [header.text for header in bs4_table.find_all("th")]
        headers = clean_strings(strings=headers)
        rows = [
            {headers[i]: cell.text.strip() for i, cell in enumerate(row.find_all("td"))}
            for row in bs4_table.find_all("tr")[1:]
        ]

        dataclass_name = clean_strings([caption])[0]
        dataclass_name = "".join(x for x in dataclass_name.title() if not x.isspace())
        NewDataclass = make_dataclass(dataclass_name, headers)
        for row in rows:
            result.append(NewDataclass(**row))
        return result

    def get_predefined_dataclass_table(self, caption: str) -> ProgrammingLanguages:
        """Predefined datatclass table"""
        bs4_table = self.get_table_by_caption(caption=caption)
        headers = [header.text for header in bs4_table.find_all("th")]
        headers = clean_strings(strings=headers)
        rows = [
            {headers[i]: cell.text.strip() for i, cell in enumerate(row.find_all("td"))}
            for row in bs4_table.find_all("tr")[1:]
        ]
        table = ProgrammingLanguages([ProgrammingLanguage(**row) for row in rows])
        return table


@dataclass
class ProgrammingLanguage:
    websites: str
    popularity: Union[int, str]
    front_end: str
    back_end: str
    database: str
    notes: str

    def __post_init__(self):
        self.popularity = int(clean_string(string=self.popularity))


@dataclass
class ProgrammingLanguages(UserList):
    data: list[ProgrammingLanguage] = field(default_factory=list)

    def __getitem__(self, i) -> ProgrammingLanguage | list[ProgrammingLanguage]:
        return super().__getitem__(i)
