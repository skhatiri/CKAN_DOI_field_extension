import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging
import re


log = logging.getLogger(__name__)

DOI_REGEX = r'^[a-zA-Z]{4}_\d{3}_[a-zA-Z]{4}$'


class DoiFieldExtensionPlugin(plugins.SingletonPlugin,toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurer)



    def create_package_schema(self):
        log.info("updating package schema for create")
        # let's grab the default schema in our plugin
        schema = super(DoiFieldExtensionPlugin, self).create_package_schema()
        # our custom field
        schema.update({
            'doi': [toolkit.get_validator('ignore_missing'), 
                    self.Doi_validate,
                    toolkit.get_converter('convert_to_extras')]
        })
        return schema

    def update_package_schema(self):  
        log.info("updating package schema for update")
        schema = super(DoiFieldExtensionPlugin, self).update_package_schema()
        # our custom field
        schema.update({
            'doi': [toolkit.get_validator('ignore_missing'),  
                    self.Doi_validate,
                    toolkit.get_converter('convert_to_extras')]
        })
        return schema

    def show_package_schema(self):
        log.info("updating package schema for show")
        schema = super(DoiFieldExtensionPlugin, self).show_package_schema()
        schema.update({
            'doi': [toolkit.get_converter('convert_from_extras'), 
                    self.Doi_validate,
                    toolkit.get_validator('ignore_missing')]
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

    def Doi_validate(self,value):
        #ignore missing
        if not value:
            return value

        if re.match(DOI_REGEX,value):
            return value
        else:
            raise toolkit.Invalid("DOI does not match the convension : 'cccc_ddd_cccc'")

   
