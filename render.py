from jinja2 import Template
import yaml
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-t",
                    "--template",
                    help="Jinja template file",
                    required=True)

parser.add_argument("-v",
                    "--values",
                    help="Values YAML file",
                    required=True)

args = parser.parse_args()

with open(args.template) as f:
    template = Template(f.read())

with open(args.values) as f:
    values = yaml.safe_load(f.read())

rendered = template.render(**values)
print(rendered)
