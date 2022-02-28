from django.core.management.base import BaseCommand

from extras.models import JobResult
from peering.jobs import poll_bgp_sessions
from peering.models import Router


class Command(BaseCommand):
    help = "Poll BGP sessions on routers."

    def add_arguments(self, parser):
        parser.add_argument(
            "-l",
            "--limit",
            nargs="?",
            help="Limit BGP session polling to the given set of routers (comma separated).",
        )
        parser.add_argument(
            "-t",
            "--tasks",
            action="store_true",
            help="Delegate BGP sessions polling to Redis worker process.",
        )

    def process(self, router, as_task=False):
        self.stdout.write(f"  - {router.hostname} ... ", ending="")

        if not as_task:
            success = router.poll_bgp_sessions()
            if success:
                self.stdout.write(self.style.SUCCESS("success"))
            else:
                self.stdout.write(self.style.ERROR("failed"))
        else:
            job = JobResult.enqueue_job(
                poll_bgp_sessions,
                "commands.poll_bgp_sessions",
                Router,
                None,
                router,
            )
            self.stdout.write(self.style.SUCCESS(f"task #{job.id}"))

    def handle(self, *args, **options):
        routers = Router.objects.filter(poll_bgp_sessions_state=True)
        if options["limit"]:
            routers = routers.filter(hostname__in=options["limit"].split(","))

        self.stdout.write("[*] Polling BGP sessions state")

        for r in routers:
            self.process(r, as_task=options["tasks"])