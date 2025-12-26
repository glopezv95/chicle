from typing import Any
import polars as pl
from datetime import date
import pandas as pd

from chicle.chicle import Chicle

class TestChicle:

    data_dict: dict[Any, Any] = {'a': [17], 'b': [32.8], 'c': [date.today()]}

    data_pl_df = pl.DataFrame(data_dict)
    data_pl_lf = pl.LazyFrame(data_dict)
    data_pd_df = pd.DataFrame(data_dict)

    chicle_dict = Chicle(data_dict)
    chicle_pl_df = Chicle(data_pl_df)
    chicle_pl_lf = Chicle(data_pl_lf)
    chicle_pd_df = Chicle(data_pd_df)

    def test_empty(self):

        chicle = Chicle(data={})

        assert isinstance(chicle, Chicle)
        assert isinstance(chicle.unprocessed_lf, pl.LazyFrame)

    def test_types(self):

        assert isinstance(self.chicle_dict, Chicle)
        assert isinstance(self.chicle_pl_df, Chicle)
        assert isinstance(self.chicle_pl_lf, Chicle)
        assert isinstance(self.chicle_pd_df, Chicle)

        assert isinstance(self.chicle_dict.unprocessed_lf, pl.LazyFrame)
        assert isinstance(self.chicle_pl_df.unprocessed_lf, pl.LazyFrame)
        assert isinstance(self.chicle_pl_lf.unprocessed_lf, pl.LazyFrame)
        assert isinstance(self.chicle_pd_df.unprocessed_lf, pl.LazyFrame)

    def test_packages(self):

        assert self.chicle_dict.package == 'python'
        assert self.chicle_pl_df.package == 'polars'
        assert self.chicle_pl_lf.package == 'polars'
        assert self.chicle_pd_df.package == 'pandas'