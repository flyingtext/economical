import pandas as pd
from typing import Dict, Any


def compute_features(df: pd.DataFrame, config: Dict[str, Any]) -> pd.DataFrame:
    """Apply feature operations defined in *config* to *df*.

    Parameters
    ----------
    df:
        Source data as a pandas DataFrame.
    config:
        Dictionary describing feature operations. Expected format::

            {
                "operations": [
                    {
                        "operation": "sum",
                        "columns": ["a", "b"],
                        "new_column": "a_plus_b"
                    },
                    {
                        "operation": "ratio",
                        "numerator": "a",
                        "denominator": "b",
                        "new_column": "a_div_b"
                    }
                ]
            }

    Returns
    -------
    pandas.DataFrame
        DataFrame including new feature columns.
    """
    operations = config.get("operations", [])

    for op in operations:
        name = op.get("new_column")
        if not name:
            raise ValueError("Each operation requires a 'new_column' field")

        op_type = op.get("operation")
        if op_type == "sum":
            cols = op.get("columns", [])
            df[name] = df[cols].sum(axis=1)
        elif op_type == "difference":
            cols = op.get("columns", [])
            if len(cols) != 2:
                raise ValueError("'difference' requires exactly two columns")
            df[name] = df[cols[0]] - df[cols[1]]
        elif op_type == "ratio":
            num = op.get("numerator")
            den = op.get("denominator")
            df[name] = df[num] / df[den]
        elif op_type == "mean":
            cols = op.get("columns", [])
            df[name] = df[cols].mean(axis=1)
        else:
            expr = op.get("expression")
            if expr is None:
                raise ValueError(f"Unsupported operation: {op_type}")
            df[name] = df.eval(expr)

    return df
