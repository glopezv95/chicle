from typing import Union, Any
from polars import DataFrame, LazyFrame
from pandas import DataFrame as PandasDataFrame

TypeChicle = Union[dict[str, Any], DataFrame, LazyFrame, PandasDataFrame]