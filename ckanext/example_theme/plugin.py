import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(
        data_dict={'sort': 'package_count desc', 'all_fields': True})

    # Truncate the list to the 10 most popular groups only.
    groups = groups[:10]

    return groups

def most_recently_updated_pkgs():
    '''Return a sorted list of the most recently updated datasets.'''

    # Get a list of the last 5 most recently updated 
    # datasets.
    pkgs =  toolkit.get_action('package_search')(
        data_dict={'rows': 5, 'sort': 'metadata_modified desc'})

    return pkgs

class ExampleThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):

        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'example_theme')


    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        return {'example_theme_most_recently_updated_pkgs': most_recently_updated_pkgs}
