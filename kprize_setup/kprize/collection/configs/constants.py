from swebench.harness.log_parsers import (
    parse_log_astroid,
    parse_log_astropy,
    parse_log_flask,
    parse_log_marshmallow,
    parse_log_pvlib,
    parse_log_pydicom,
    parse_log_pylint,
    parse_log_pytest,
    parse_log_pytest_options,
    parse_log_pytest_v2,
    parse_log_pyvista,
    parse_log_requests,
    parse_log_scikit,
    parse_log_sphinx,
    parse_log_sqlfluff,
    parse_log_xarray,
)

LOG_PARSER_MAP = {
    "parse_log_pytest": parse_log_pytest,
    "parse_log_pytest_options": parse_log_pytest_options,
    "parse_log_pytest_v2": parse_log_pytest_v2,
    "parse_log_astroid": parse_log_astroid,
    "parse_log_flask": parse_log_flask,
    "parse_log_marshmallow": parse_log_marshmallow,
    "parse_log_pvlib": parse_log_pvlib,
    "parse_log_pyvista": parse_log_pyvista,
    "parse_log_sqlfluff": parse_log_sqlfluff,
    "parse_log_xarray": parse_log_xarray,
    "parse_log_pydicom": parse_log_pydicom,
    "parse_log_requests": parse_log_requests,
    "parse_log_pylint": parse_log_pylint,
    "parse_log_astropy": parse_log_astropy,
    "parse_log_scikit": parse_log_scikit,
    "parse_log_sphinx": parse_log_sphinx,
}
