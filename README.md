# Template Rendering

## Installation

```
git clone https://github.com/peymanhr/template_rendering.git
cd template_rendering
python3 -m venv ~/.venv/template
source ~/.venv/template/bin/activate
pip install -r requirements.txt
```

## Usage

```
cd template_rendering
source ~/.venv/template/bin/activate
python3 render.py -t templates/gre.j2 -v values/gre.yaml
```