import threading
from django.core.management import BaseCommand, call_command
from service_a.service_a.grpc.server import serve

class Command(BaseCommand):
    help = "Django runserver (メインスレッド) と gRPC サーバー (サブスレッド) を同時に起動するコマンド"

    def add_arguments(self, parser):
        parser.add_argument(
            "--addrport",
            default="127.0.0.1:8000",
            help="Django runserver のアドレス:ポート (デフォルト: 127.0.0.1:8000)",
        )
        parser.add_argument(
            "--grpcport",
            default="50051",
            help="gRPC サーバーのポート (デフォルト: 50051)",
        )
        parser.add_argument(
            "--noreload",
            action="store_true",
            help="Django runserver の自動リロードを無効化",
        )

    def handle(self, *args, **options):
        addrport = options["addrport"]
        grpcport = options["grpcport"]
        disable_reload = options["noreload"]

        # gRPC をサブスレッドで起動
        def start_grpc_server():
            self.stdout.write(self.style.NOTICE(f"Starting gRPC server at :{grpcport}..."))
            serve(port=grpcport)

        # メインスレッドで runserver する
        def start_django_runserver():
            if disable_reload:
                call_command("runserver", addrport, use_reloader=False)
            else:
                call_command("runserver", addrport)

        # TODO: オートリロードを有効化すると初回だけ２重起動される問題を解決する
        def inner_run():
            serve(port=grpcport)
            grpc_thread = threading.Thread(
                target=start_grpc_server,
                name="gRPC-Thread",
                daemon=True,
            )
            grpc_thread.start()
            start_django_runserver()

        inner_run()
