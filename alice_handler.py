import re
import database

def extract_items(text):
    match = re.search(r'������ � ������ ������� ([\w\s,]+)', text.lower())
    if match:
        return match.group(1).strip()
    return None

def process(data):
    command = data['request']['command']
    user_id = data.get('session', {}).get('user_id', 'default_user')

    items = extract_items(command)
    if items:
        list_id = database.save_list(user_id, items)
        return {
            "response": {
                "text": f"������� � ������ �������: {items}. ����� ������: {list_id}",
                "end_session": True
            }
        }

    return {
        "response": {
            "text": "�� ������ �������. �������: ������ � ������ �������...",
            "end_session": True
        }
    }