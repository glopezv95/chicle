import polars as pl
import pandas as pd

from .types import TypeChicle

class Chicle:

    def __init__(self, data: TypeChicle) -> None:
        
        self.data = data
        self.type = type(data)
        self.package = self._get_package()
    
    def _get_package(self) -> str:
        return (
            'polars' if self.type in (pl.DataFrame, pl.LazyFrame)
            else 'pandas' if self.type == pd.DataFrame
            else 'python'
        )

if __name__ == '__main__':

    df = pl.DataFrame()
    chicle = Chicle(df)
    print('pl.DataFrame', chicle.package, sep='\n', end='\n')

    df_dict = dict(zip(['s'], [17]))
    chicle = Chicle(df_dict)
    print('python dict', chicle.package, sep='\n', end='\n')
    
    df = pd.DataFrame()
    chicle = Chicle(df)
    print('pd.DataFrame', chicle.package, sep='\n', end='\n')