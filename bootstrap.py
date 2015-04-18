# Bootstrap the Sentry environment
from sentry.utils.runner import configure
configure()

import os

from sentry.models import Team, Project, ProjectKey, User

username = os.environ.get('ADMIN_USERNAME', 'aptible')
user, created = User.objects.get_or_create(username=username, defaults={
    'email': os.environ.get('ADMIN_EMAIL', 'root@localhost'),
    'is_superuser': True
})

user.set_password(os.environ['ADMIN_PASSWORD'])
user.save()

team_name = os.environ.get('TEAM_NAME', 'Aptible')
team, created = Team.objects.get_or_create(name=team_name, defaults={
    'owner': user
})
