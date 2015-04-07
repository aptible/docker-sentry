# Bootstrap the Sentry environment
from sentry.utils.runner import configure
configure()

from sentry.models import Team, Project, ProjectKey, User

username = os.environ.get('ADMIN_USERNAME', 'aptible')
user, created = User.objects.get_or_create(username, defaults={
    'email': os.environ.get('ADMIN_EMAIL'),
    'is_superuser': True
})

if created:
    user.set_password(os.environ['PASSWORD'])
    user.save()

team_name = os.environ.get('TEAM_NAME', 'Aptible')
team, created = Team.objects.get_or_create(name=team_name, defaults={
    'owner': user
})

# for project_name in ('webserver', 'webclient', 'socketserver', 'ios'):
#     project, created = Project.objects.get_or_create(
#         name=project_name, defaults={
#             'team': team,
#             'owner': user,
#         })

#     key = ProjectKey.objects.filter(project=project)[0]
#     print project_name, 'SENTRY_DSN = {}'.format(key.get_dsn())
