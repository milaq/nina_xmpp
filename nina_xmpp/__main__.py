import asyncio
import logging
import logging.handlers

from . import NinaXMPP

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)


def main():
    import yaml
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('config_file', type=argparse.FileType('r'))
    args = parser.parse_args()

    config = yaml.safe_load(args.config_file)
    args.config_file.close()

    main = NinaXMPP(config)

    asyncio.run(main.run())


if __name__ == '__main__':
    main()
