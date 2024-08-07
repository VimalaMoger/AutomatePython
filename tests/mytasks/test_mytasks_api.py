import uuid

import pytest
import requests
import typing

ENDPOINT = "https://todo.pixegami.io"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_can_create_task():
    create_task_response = create_task(get_new_payload())
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    #print("created", data)
    task_id = data["task"]["task_id"]
    content = data["task"]["content"]
    user_id = data["task"]["user_id"]

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    #print("get data", get_task_data)

    assert get_task_data["content"] == content
    assert get_task_data["user_id"] == user_id


@pytest.mark.skip(reason="not currently testing this")
def test_can_get_tasks_userID():
    response = requests.get(ENDPOINT + "/list-tasks/string")
    assert response.status_code == 200
    get_task_data = response.json()
    #print(get_task_data)
    #print(response.status_code)


# @pytest.mark.skip(reason="not currently testing this")
def test_can_update_task():
    """first create task, update the task, get and validate the changes"""

    created_task_response = create_task(get_new_payload())
    data = created_task_response.json()
    created_taskId = data["task"]["task_id"]
    assert created_task_response.status_code == 200
    #print("My created data", data)

    updated_payload = {
        "user_id": get_new_payload()["user_id"],
        "task_id": created_taskId,
        "content": get_new_payload()["content"],
        "is_done": True,
    }
    updated_task_response = updated_task(updated_payload)
    assert updated_task_response.status_code == 200

    get_task_response = get_task(updated_payload["task_id"])
    assert get_task_response.status_code == 200
    get_data = get_task_response.json()
    #print("my updated data", get_data)

    assert get_data["content"] == updated_payload["content"]
    # assert get_data["user_id"] == updated_payload["user_id"]
    assert get_data["task_id"] == updated_payload["task_id"]


def test_can_list_tasks():
    # create N tasks
    n = 3
    payload = get_new_payload()
    for i in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200
        print("created ",create_task_response.json())

    # List tasks, and check that there are N items
    user_id = payload["user_id"]
    list_tasks_response = list_tasks(user_id)
    assert create_task_response.status_code == 200
    data = list_tasks_response.json()['tasks']
    print("data ",data)
    assert len(data) == n

#delete
# first create, delete, get task to check that it is not found
def test_delete_task():
    payload = get_new_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()["task"]["task_id"]

    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404


def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")


#helper functions to reuse
def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)


def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")


def updated_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)


def get_new_payload():
    #  Universally Unique Identifier
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    #print(f"Creating task for user  {user_id} with content {content}")
    new_payload = {
        "content": content,
        "user_id": user_id,
        "is_done": False,
    }
    return new_payload


def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")
