# -*- coding:utf-8 -*-

from mybottle.core.app_common import app


def add_db_close_plugin(db_instance):
    def db_close(callback):
        def wrapper(*args, **kwargs):
            body = callback(*args, **kwargs)
            db_instance.close()
            return body

        return wrapper

    app.install(db_close)
