import json
import re
import sys


def main():
    payload = json.loads(sys.argv[1])
    branches = json.loads(payload['version']['branches'])

    source = payload['source']
    if 'branch_regex' in source:
        regex = re.compile(source['branch_regex'])
        output = [{'name': branch, 'groups': regex.match(branch).groupdict(),'env': 'production' if branch == 'main'  or branch == 'master' else 'staging'} for branch in branches]
    else:
        output = [{'name': branch,'env': 'production' if branch == 'main'  or branch == 'master' else 'staging'} for branch in branches]

    print(json.dumps(output))


if __name__ == '__main__':
    main()
