import polars as pl
import pandas as pd

from .types import TypeChicle

class Chicle:

    def __init__(self, data: TypeChicle) -> None:
        
        self.data = data
        self.type = type(self.data)
        self.package = self._get_package()
        self.unprocessed_lf = self._get_df()
    
    def _get_package(self) -> str:
        return (
            'polars' if self.type in (pl.DataFrame, pl.LazyFrame)
            else 'pandas' if self.type == pd.DataFrame
            else 'python'
        )
    
    def _get_df(self) -> pl.LazyFrame:
        return (
            self.data
            if isinstance(self.data, pl.LazyFrame)
            else pl.LazyFrame(self.data)
        )