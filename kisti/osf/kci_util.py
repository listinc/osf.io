from datetime import datetime, timezone, date


def change_time(date_data):
    a = datetime.strptime(date_data, "%Y%m")
    result = a.replace(tzinfo=timezone.utc)
    return result


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))
