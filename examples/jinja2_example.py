from jinja2 import Template

template = Template(
    'print("{{ message }}")'
)

with open('render_result.py', 'w') as file:
    file.write(template.render(message='from Jinja'))
