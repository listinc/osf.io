"""
Listens for actions to be done to OSFstorage file nodes specifically.
"""
from website.project.signals import contributor_removed

@contributor_removed.connect
def checkin_files_by_user(node, user):
    """ Listens to a contributor being removed to check in all of their files
    """
    node.files.filter(checkout=user).update(checkout=None)
