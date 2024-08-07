import uvicorn
from fastapi import FastAPI

from dags import build_workflow, create_avatar_flow_dag

app = FastAPI()


@app.post("/execute-workflow/")
async def execute_workflow_endpoint():
    workflow = build_workflow(create_avatar_flow_dag)
    result = workflow.apply_async()
    return {"message": "Video processing started", "task_id": result.id}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
