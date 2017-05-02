#!/usr/bin/env python
import os
import sys

import click
from credstash import getSecret, listSecrets
from jinja2 import Environment, FileSystemLoader


def render_with_credentials(file):
    """Render file argument with credstash credentials

    Load file as jinja2 template and render it with context where keys are 
    credstash keys and values are credstash values

    Args:
        file (str): jinja2 template file path

    Returns:
        str: Rendered string

    """
    env = Environment(loader=FileSystemLoader(os.path.dirname(file)))
    template = env.get_template(os.path.basename(file))
    context = {secret['name']: getSecret(secret['name'])
               for secret in listSecrets()}
    return template.render(**context)


@click.command()
@click.argument('file')
def main(file):
    """Output rendered template

    Args:
        file (str): jinja2 template file path

    """
    sys.stdout.write(render_with_credentials(file))


if __name__ == '__main__':
    main()
