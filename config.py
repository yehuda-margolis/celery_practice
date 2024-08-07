task_queues = {
    "preprocess_video_task_queue": {
        "exchange": "ghost_topic",
        "exchange_type": "topic",
        "binding_key": "task.preprocess_video",
    },
    "check_moderation": {
        "exchange": "ghost_topic",
        "exchange_type": "topic",
        "binding_key": "task.check_moderation",
    },
    "remove_background": {
        "exchange": "ghost_topic",
        "exchange_type": "topic",
        "binding_key": "task.remove_background",
    },
    "perform_analysis": {
        "exchange": "ghost_topic",
        "exchange_type": "topic",
        "binding_key": "task.perform_analysis",
    },
    "create_internal_assets": {
        "exchange": "ghost_topic",
        "exchange_type": "topic",
        "binding_key": "task.create_internal_assets",
    },
}

task_routes = {
    "tasks.preprocess_video": {"queue": "preprocess_video_task_queue"},
    "tasks.check_moderation": {"queue": "check_moderation"},
    "tasks.remove_background": {"queue": "remove_background"},
    "tasks.perform_analysis": {"queue": "perform_analysis"},
    "tasks.create_internal_assets": {"queue": "create_internal_assets"},
}
