pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'card_generator')
gnome = import('gnome')
#scrython = import('scrython')
#json = import('json')
#wget = import('wget')
#requests = import('requests')

gnome.compile_resources('card-generator',
  'card_generator.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'card-generator.in',
  output: 'card-generator',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

card_generator_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(card_generator_sources, install_dir: moduledir)
