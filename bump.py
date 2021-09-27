import json
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("You should pass the json file as argument on cli")

    with open(sys.argv[1], "r") as f:
        file_content = json.load(f)

        if not "version" in file_content:
            raise Exception("The filed supplied doesn't have a version key")

        version = file_content["version"]
        if len(version.split(".")) < 3:
            raise Exception("Version {} is not semver".format(version))

        major, minor, patch = version.split(".")

        patch = int(patch)
        patch += 1

        new_version = ".".join([major, minor, str(patch)])
        file_content["version"] = new_version

    with open(sys.argv[1], "w") as f:
        json.dump(file_content, f)

