class MiApp3Router(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_3 models go to mi_db_3.
        """
        if model._meta.app_label == 'consultasWMS':
            return 'mi_db_3'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_3 models go to mi_db_3.
        """
        if model._meta.app_label == 'consultasWMS':
            return 'mi_db_3'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_3 app is involved.
        """
        if obj1._meta.app_label == 'consultasWMS' or \
           obj2._meta.app_label == 'consultasWMS':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_3 app only appears in the 'mi_db_3'
        database.
        """
        if app_label == 'consultasWMS':
            return db == 'mi_db_2'
        return None 