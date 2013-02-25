Django Site Indexing
====================

A simple Django app created for indexing sites (also allows for static pages, and tracking stats on indexed sites)

Requirements
------------
* Python >= 2.5
* Django 1.4

Installation
------------
1. Modify your project's `settings.py` to add `index` to the `INSTALLED_APPS` array.
2. Modify your project's `urls.py` to add a route to `include('index.urls')`.
3. Run `python manage.py syncdb` to create the databases Django Site Indexing requires.

That's it!

Examples
--------
Django Site Indexing is used on [Make Bitcoins Fast](http://www.makebitcoinsfast.com/).

Примечание:
----------
Простой рейтинг учитывающий количество кликов и просмотров
