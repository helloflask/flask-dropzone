Flask-Dropzone Changelog
=========================

1.5.0
-----
released date: --

WARNING: **New major upstream release (backwards incompatible!).**

* Remove `dropzone.load()` method.


1.4.6
-----
released date: 2018/6/8

* Change built-in resource's url path to `dropzone/static/...` to prevent conflict with user's static path.

1.4.4
-----
released date: 2018/5/28

* `dropzone.load()` method was deprecated due to inflexible.
Now it's divided into three methods:
  * Use `load_css()` to load css resources.
  * Use `load_js()` to load js resources.
  * Use `config()` to configure Dropzone.
  * Besides, we recommend user to manage the resouces manually.
* Add basic unit tests.

1.4.3
------
released date: 2018/3/23

* Add support to use custom resources with `js_url` and `css_url` param
 in `load()`.
* Fix built-in static bug ([#11]).
* Use package instead of module.

[#11]:https://github.com/greyli/flask-dropzone/issues/11

1.4.2
------
released date: 2018/2/17

* Add support to integrate with CSRFProtect (enabled via `DROPZONE_ENABLE_CSRF`
 or `csrf` flag in `dropzone.create()`).
* Fix bug: `False` in JavaScript.
* Bump built-in resource's version to 5.2.0
* Add `action` argument in `dropzone.create()`. For example, 
`dropzone.create(action=url_for('upload'))`.

1.4.1
------

* New configuration options: `DROPZONE_UPLOAD_MULTIPLE`,
 `DROPZONE_PARALLEL_UPLOADS`, `DROPZONE_REDIRECT_VIEW`.
* Fix local static files bug.
* Add support for automatic redirection when upload was conmplete.

1.4
---

WARNING: **New major upstream release (backwards incompatible!).**

* Method `include_dropzone()` rename to `load()`.
* Add a `create()` method to create dropzone form.
* Add a `style()` method to add style to upload area.
* Use `action_view` argument (in `create()`) to set action url.
* Dropzonejs version increase to 5.1.1.
* PEP8 and bug fix.

1.3
---
* Documentation fix.

1.2
---
* Upload address fix.
* Delete useless code.

1.1
---
* Add more configuration options.
* Support local resource serve.
* Add basic documentation.

1.0
---
* Init release.
