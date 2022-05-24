import requests
import argparse
import logging
from utils import util

format_string = '[%(asctime)s] %(levelname)s %(name)s:%(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format_string)
logger = logging.getLogger(__name__)


def fetch_commits(repo_url, params, headers):
    # Fetch response object and parse commit info into list
    items = []
    resp = get_commit_details(repo_url, params, headers)
    if resp is not None:
        details = resp.json()
        logger.debug('Fetch commit info {0}'.format(details))
        for commit in range(0, len(details)):
            commit_info = details[commit]
            sha = commit_info['sha']
            author = commit_info['commit']['author']['name']
            message = commit_info['commit']['message']
            items.append(dict(SHA=sha,
                              AUTHOR=author,
                              MESSAGE=message))
    logger.debug('Fetch commit items {0}'.format(items))
    return items


def get_commit_details(repo_url, params, headers):
    # Make GET API call to fetch commits for repo-branch
    try:
        logger.debug('Calling Get for repo commits {0}'.format(repo_url))
        resp = requests.get(repo_url,
                            headers=headers,
                            params=params,
                            timeout=10)
        if resp.ok:
            return resp
    except BaseException as err:
        logger.error('Received error {0}'.format(err))
    return None


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-a',
                        '--url',
                        dest='github_url',
                        help='Enter Github base URL',
                        required=True)
    parser.add_argument('-o',
                        '--owner',
                        dest='github_owner',
                        help='Enter Github repo owner',
                        required=True)
    parser.add_argument('-r',
                        '--repo',
                        dest='github_repo',
                        help='Enter Github repo name',
                        required=True)
    parser.add_argument('-b',
                        '--branch',
                        dest='github_branch',
                        help='Enter Github repo branch',
                        required=True)
    parser.add_argument('-p',
                        '--path',
                        dest='output_path',
                        help='Enter Path for Output html',
                        required=True)
    args = parser.parse_args()
    github_url = args.github_url.strip()
    github_owner = args.github_owner.strip()
    github_repo = args.github_repo.strip()
    github_branch = args.github_branch.strip()
    output_path = args.output_path.strip()
    params = {
        'sha': github_branch,
        'per_page': 5,
        'page': 1
    }
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    repo_url = 'https://{0}/repos/{1}/{2}/commits'.format(github_url,
                                                          github_owner,
                                                          github_repo)
    items = fetch_commits(repo_url, params, headers)
    if len(items) != 0:
        obj = util.create_html_file(items=items)
        util.copy_to_path(output_path, obj)
    else:
        logger.error('found no commits for {0}'.format(repo_url))


if __name__ == '__main__':
    main()
