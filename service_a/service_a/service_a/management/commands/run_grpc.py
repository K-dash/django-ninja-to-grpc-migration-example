from django.core.management.base import BaseCommand
from service_a.grpc.server import serve


class Command(BaseCommand):
    help = "サービスAのgRPCサーバーを起動するコマンド"

    def add_arguments(self, parser):
        parser.add_argument(
            "--port",
            type=int,
            default=50051,
            help="Port number on which the gRPC server will listen (default: 50051)."
        )

    def handle(self, *args, **options):
        port = options["port"]
        serve(port=port)
