from urllib import request

import tomli
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):

        content = request.urlopen(self._url).read().decode("utf-8")

        data = tomli.loads(content).get("tool", {}).get("poetry", {})

        name = data.get("name", "Unknown")
        description = data.get("description", "No description")
        dependencies = list(data.get("dependencies", {}).keys())
        dev_dependencies = list(
            data.get("group", {}).get("dev", {}).get("dependencies", {}).keys()
        )
        license = data.get("license", "No license")
        authors = data.get("authors", [])

        project = Project(
            name, description, license, authors, dependencies, dev_dependencies
        )

        return project
