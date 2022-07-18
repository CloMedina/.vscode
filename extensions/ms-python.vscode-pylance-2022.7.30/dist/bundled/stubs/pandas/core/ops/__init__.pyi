from typing import (
    Any,
    Optional,
    Set,
    Tuple,
)

ARITHMETIC_BINOPS: Set[str] = ...
COMPARISON_BINOPS: Set[str] = ...

def get_op_result_name(left: Any, right: Any): ...
def maybe_upcast_for_op(obj: Any, shape: Tuple[int, ...]) -> Any: ...
def fill_binop(left: Any, right: Any, fill_value: Any): ...
def dispatch_to_series(
    left: Any,
    right: Any,
    func: Any,
    str_rep: Optional[Any] = ...,
    axis: Optional[Any] = ...,
): ...
