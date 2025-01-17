#!/usr/bin/env python
import argparse

from lib.strobe import Strobe


def main(connector_name, platform):
    Strobe(connector_name, platform)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--platform",
        type=str,
        default="windows",
        help="Specify platform. Available : windows, linux or freebsd, others WiP (default : windows)",
    )
    parser.add_argument(
        "-s",
        "--source",
        type=str,
        default="meteosat11",
        help="Image connector name. Available : meteosat11, himawari8 "
        "(default : meteosat11)",
    )
    args = parser.parse_args()
    main(args.source, args.platform)
