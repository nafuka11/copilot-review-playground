def calculate_total(items: list[float]) -> float:
    return sum(items)


def get_user(user_id: int) -> dict:
    return {"id": user_id, "name": "Alice"}


def process_data(data: list) -> list:
    return [x * 2 for x in data]
