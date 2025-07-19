def is_context_manager(obj):
    try:
        with obj:
            return True
    except:
        return False
