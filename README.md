# CKAN_DOI_field_extension
A CKAN extension to add a custom DOI field to datasets schema

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

1. You should have Docker or a CKAN instance installed before using this extension

### Installing

1. Clone the repository
```
$ git clone https://github.com/skhatiri/CKAN_DOI_field_extension.git
```

#### On your own CKAN instalation:

4. Add ``"doi_field_extension"`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/ckan.ini``).

5. Go to project's root, Activate your CKAN virtual environment, and run ``setup.py develop``
```
$ . /usr/lib/ckan/default/bin/activate
$ python setup.py develop    
```

6. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

```
$ sudo service apache2 reload
```

## Authors

* **Sajad Khatiri** - [s.khatiri](https://github.com/skhatiri)


## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details


