import fire
import json


def main(param1: dict, param2: int):
    result = {
        "param1": param1,
        "param2": param2,
    }
    print(json.dumps(result))


if __name__ == "__main__":
    fire.Fire(main)
