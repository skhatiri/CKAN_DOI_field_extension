import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging

log = logging.getLogger(__name__)


class DoiFieldExtensionPlugin(plugins.SingletonPlugin,toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurer)

    def create_package_schema(self):
        log.info("updating package schema for create")
        # let's grab the default schema in our plugin
        schema = super(ExampleIDatasetFormPlugin, self).create_package_schema()
        # our custom field
        schema.update({
            'doi': [toolkit.get_validator('ignore_missing')]
        })
        return schema

    def update_package_schema(self):  
        log.info("updating package schema for update")
        schema = super(ExampleIDatasetFormPlugin, self).update_package_schema()
        # our custom field
        schema.update({
            'doi': [toolkit.get_validator('ignore_missing')]
        })
        return schema

    def show_package_schema(self):
        log.info("updating package schema for show")
        schema = super(ExampleIDatasetFormPlugin, self).show_package_schema()
        schema.update({
            'doi': [toolkit.get_validator('ignore_missing')]
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
    
    def update_config(self, config):
        log.info("configuring the extension")
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')

    # IConfigurer

    #def update_config(self, config_):
    #    toolkit.add_template_directory(config_, 'templates')
    #    toolkit.add_public_directory(config_, 'public')
    #    toolkit.add_resource('fanstatic',
    #        'doi_field_extension')
