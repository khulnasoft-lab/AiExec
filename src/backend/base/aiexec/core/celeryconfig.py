# celeryconfig.py
import os

aiexec_redis_host = os.environ.get("AIEXEC_REDIS_HOST")
aiexec_redis_port = os.environ.get("AIEXEC_REDIS_PORT")
# broker default user

if aiexec_redis_host and aiexec_redis_port:
    broker_url = f"redis://{aiexec_redis_host}:{aiexec_redis_port}/0"
    result_backend = f"redis://{aiexec_redis_host}:{aiexec_redis_port}/0"
else:
    # RabbitMQ
    mq_user = os.environ.get("RABBITMQ_DEFAULT_USER", "aiexec")
    mq_password = os.environ.get("RABBITMQ_DEFAULT_PASS", "aiexec")
    broker_url = os.environ.get("BROKER_URL", f"amqp://{mq_user}:{mq_password}@localhost:5672//")
    result_backend = os.environ.get("RESULT_BACKEND", "redis://localhost:6379/0")
# tasks should be json or pickle
accept_content = ["json", "pickle"]
