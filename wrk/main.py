import os
import argparse
import asyncio
from spydy.engine import Engine
from spydy.urls import DummyUrls
from spydy.request import AsyncHttpRequest
from spydy.logs import StatsReportLog
from spydy.utils import check_configs


def main():
    arg_parser = argparse.ArgumentParser(
        prog="py-wrk",
        description="Small http benchmarking tool written in python",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    # prepare args
    arg_parser.add_argument("url", type=str, help="Url")

    arg_parser.add_argument(
        "-m", "--method", type=str, help="Http method", default="Get"
    )

    arg_parser.add_argument("-p", "--params", type=str, help="Request Parameters")

    arg_parser.add_argument("-d", "--data", type=str, help="Request body")

    arg_parser.add_argument("-H", "--headers", type=str, help="Request header")

    arg_parser.add_argument("--cookies", type=str, help="Cookies")

    arg_parser.add_argument("--user", type=str, help="User for Authentication")

    arg_parser.add_argument("--password", type=str, help="Passworf for Authentication")

    arg_parser.add_argument(
        "-c",
        "--connections",
        type=int,
        help="Number of Connetions at same time",
        default=10,
    )

    arg_parser.add_argument(
        "-n", "--numbers", type=int, help="Totoal numbers to call", default=100
    )
    # Parse args
    args = arg_parser.parse_args()

    url = args.url
    method = args.method
    connections = args.connections
    numbers = args.numbers
    user = args.user
    password = args.password
    if user and password:
        auth = (user, password)
    else:
        auth = None

    # Parse dict-like string to python dict
    params = args.params
    try:
        if params:
            params = eval(params)
    except:
        raise ValueError("Can not parse params")
    data = args.data
    try:
        if data:
            data = eval(data)
    except:
        raise ValueError("Can not parse data")
    headers = args.headers
    try:
        if headers:
            headers = eval(headers)
    except:
        raise ValueError("Can not parse headers")
    cookies = args.cookies
    try:
        if cookies:
            cookies = eval(cookies)
    except:
        raise ValueError("Can not parse cookies")

    spydy_config = {
        "Globals": {
            "run_mode": "async_forever",
            "nworkers": connections,
            "verbose": "False",
        },
        "PipeLine": [
            DummyUrls(url=url, repeat=numbers),
            AsyncHttpRequest(
                method=method,
                params=params,
                data=data,
                headers=headers,
                cookies=cookies,
                auth=auth
            ),
            StatsReportLog(every=int(numbers / 10)),
        ],
    }
    check_configs(spydy_config)
    spider = Engine.from_dict(spydy_config)
    spider.run()
