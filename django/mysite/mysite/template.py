from django import template
t = template.Template('My name is {{ name }}')
c = template.Context({'name': 'adrian'})
print t.render(c)

c = template.Context({'name': 'Fred'})
print t.render(c)
