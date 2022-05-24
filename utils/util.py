from jinja2 import Environment, FileSystemLoader
import os
import logging
logger = logging.getLogger(__name__)


def create_html_file(items):

    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('index_template.html')
    logger.debug('Render jinja template {0} using {1}'.format(template,
                                                              items))
    obj = template.render(items=items)
    return obj


def copy_to_path(output_path, data):
    # Check output_path directory exists
    if os.path.exists(output_path):
        filename = output_path + 'index.html'
        logger.debug('writing output to file {0}'.format(filename))
        with open(filename, 'w') as fh:
            fh.write(data)
            fh.close()
    else:
        logger.error('Path does not exist {0}'.format(output_path))
