#coding=utf-8

import os
import flasgger     #type:ignore


template = {
  'swagger': '2.0',
  'info': {
    'title': os.getenv('SERVICE_NAME', '{{cookiecutter.pkg_name}}'),
    'description': '',
    'contact': {
      'responsibleOrganization': '{{cookiecutter.author}}',
      'responsibleDeveloper': '{{cookiecutter.author}}',
      'email': '{{cookiecutter.author_email}}',
    },
    'version': '{{cookiecutter.version}}'
  },
}

swagger_config = flasgger.Swagger.DEFAULT_CONFIG
SWAGGER_UI_VER = '3.35.1'
swagger_config.update({
  'swagger_ui': True,
  'specs_route': '/docs',
  'swagger_ui_bundle_js': f'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/{SWAGGER_UI_VER}/swagger-ui.min.js',      #pylint:disable=C0301
  'swagger_ui_standalone_preset_js': f'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/{SWAGGER_UI_VER}/swagger-ui-standalone-preset.min.js',     #pylint:disable=C0301
  'swagger_ui_css': f'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/{SWAGGER_UI_VER}/swagger-ui.min.css',       #pylint:disable=C0301
  'jquery_js': 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js',
})

swagger = flasgger.Flasgger(
  config=swagger_config,
  template=template
)
