import importlib
from datetime import timedelta

from celery import group

create_avatar_flow_dag = {
    "preprocess_video": {
        "task": "preprocess_video",
        "path": "tasks.preprocess_video",
        "dependencies": [],
        "max_retries": 3,
        "retry_delay": timedelta(minutes=5),
    },
    "check_moderation": {
        "task": "check_moderation",
        "path": "tasks.check_moderation",
        "dependencies": ["preprocess_video"],
        "max_retries": 3,
        "retry_delay": timedelta(minutes=5),
    },
    "remove_background": {
        "task": "remove_background",
        "path": "tasks.remove_background",
        "dependencies": ["check_moderation"],
        "max_retries": 3,
        "retry_delay": timedelta(minutes=5),
    },
    "perform_analysis": {
        "task": "perform_analysis",
        "path": "tasks.perform_analysis",
        "dependencies": ["check_moderation"],
        "max_retries": 3,
        "retry_delay": timedelta(minutes=5),
    },
    "create_internal_assets": {
        "task": "create_internal_assets",
        "path": "tasks.create_internal_assets",
        "dependencies": ["remove_background", "perform_analysis"],
        "max_retries": 3,
        "retry_delay": timedelta(minutes=5),
    },
}


def get_function_by_path(path):
    module_path, function_name = path.rsplit(".", 1)
    module = importlib.import_module(module_path)
    return getattr(module, function_name)


def build_task(task_info):
    task_func = get_function_by_path(task_info["path"])
    return task_func.si().set(
        max_retries=task_info["max_retries"], retry_delay=str(task_info["retry_delay"])
    )


def build_workflow(dag):
    tasks = {}

    for task_name, task_info in dag.items():
        if not task_info["dependencies"]:
            tasks[task_name] = build_task(task_info)
        else:
            dependency_tasks = [tasks[dep] for dep in task_info["dependencies"]]
            if len(dependency_tasks) == 1:
                tasks[task_name] = dependency_tasks[0] | build_task(task_info)
            else:
                tasks[task_name] = group(dependency_tasks) | build_task(task_info)

    final_task = tasks["create_internal_assets"]
    return final_task
