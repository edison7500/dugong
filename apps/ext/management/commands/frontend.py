import subprocess
from django.core.management.base import LabelCommand, CommandError
from django.conf import settings


class Command(LabelCommand):

    frontend_dir = getattr(settings, "FRONTEND_DIR")
    commands = ["install", "build", "dev"]

    @classmethod
    def validate(cls, label):
        if label not in cls.commands:
            raise CommandError("{} Subcommand doesn't exist".format(label))

    def handle_label(self, label, **options):
        Command.validate(label)
        getattr(self, "handle_{}".format(label))(**options)

    def handle_install(self, **options):
        self.stdout.write("process install")
        self.npm_run(["install"])

    def handle_dev(self, **options):
        self.npm_run(["run", "dev"])

    def handle_build(self, **options):
        self.npm_run(["run", "build"])

    def npm_run(self, commands: list) -> None:
        try:
            subprocess.run(["npm"] + commands, cwd=self.frontend_dir)
        except KeyboardInterrupt:
            pass
