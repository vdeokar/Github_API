import json
import unittest
import os
from unittest.mock import patch, Mock, mock_open
import utils.util
import github_fetch


class TestConfig:
    params = {
        'sha': 'tester',
        'per_page': '1',
        'page': '1'
    }
    headers = {'Accept': 'application/json'}
    repo_url = 'https://api.example.com/repos/test/tester/commits'
    items = [{'SHA': 'ABCDEF',
              'AUTHOR': 'Jon Doe',
              'MESSAGE': 'testing jinja'}]


class BasicTests(unittest.TestCase):

    @patch('github_fetch.requests.get')
    def test_request_response_get_json(self, mock_get,
                                       config=TestConfig()):

        dir_name = os.path.dirname(__file__)
        filename = os.path.join(dir_name, 'sample-test-data.json')
        with open(filename) as data_file:
            data_json = json.load(data_file)

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = data_json

        output = github_fetch.fetch_commits(config.repo_url,
                                            config.params,
                                            config.headers)
        out_data = output[0]
        self.assertEqual(out_data['SHA'],
                         data_json[0]['sha'])
        self.assertEqual(out_data['MESSAGE'],
                         data_json[0]['commit']['message'])
        self.assertEqual(out_data['AUTHOR'],
                         data_json[0]['commit']['author']['name'])

    @patch('github_fetch.requests.get')
    def test_request_response_no_json(self, mock_get,
                                      config=TestConfig()):
        mock_get.return_value.ok = False
        mock_get.return_value.json.return_value = None
        out = github_fetch.fetch_commits(config.repo_url,
                                         config.params,
                                         config.headers)
        self.assertEqual(out, [])

    @patch('github_fetch.requests.get')
    def test_request_response_ok(self, mock_get, config=TestConfig()):

        mock_get.return_value.status_code = 200
        out = github_fetch.get_commit_details(config.repo_url,
                                              config.params,
                                              config.headers)
        self.assertEqual(out.status_code, 200)

    @patch('github_fetch.requests.get')
    def test_request_response_not_ok(self, mock_get, config=TestConfig()):

        mock_get.return_value.ok = False
        out = github_fetch.get_commit_details(config.repo_url,
                                              config.params,
                                              config.headers)
        self.assertIsNone(out)

    @staticmethod
    def test_jinja_rendered_html(config=TestConfig()):

        result = utils.util.create_html_file(config.items)

        assert config.items[0]['SHA'] in result
        assert config.items[0]['AUTHOR'] in result
        assert config.items[0]['MESSAGE'] in result

    def test_write_file_output(self):

        fake_file_path = './'
        data = 'testing write to file'
        with patch('utils.util.open', mock_open()) as open_mock:
            utils.util.copy_to_path(fake_file_path, data)
            open_mock.assert_called_with(fake_file_path+'index.html', 'w')
            open_mock.return_value.write.assert_called_once_with(data)


if __name__ == '__main__':
    unittest.main()
