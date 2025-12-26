from typing import Union, Any
from polars import DataFrame, LazyFrame
from pandas import DataFrame as PandasDataFrame

TypeChicle = Union[dict[Any, Any], DataFrame, LazyFrame, PandasDataFrame]