from typing import List, Dict
from common.models import Notification
from common.interfaces import NotificationRepo

class SimpleNotificationRepository(NotificationRepo):
    def __init__(self):
        self._notifications: Dict[str, Notification] = {}
        self._user_notifications: Dict[str, List[str]] = {}  # user_id -> list of notification_ids
    
    def get(self, notification_id: str) -> Notification:
        return self._notifications.get(notification_id)
    
    def add(self, notification: Notification) -> None:
        self._notifications[notification.id] = notification
        # Додаємо до списку сповіщень користувача
        if notification.user_id not in self._user_notifications:
            self._user_notifications[notification.user_id] = []
        self._user_notifications[notification.user_id].append(notification.id)
    
    def list_for_user(self, user_id: str) -> List[Notification]:
        # Отримати всі сповіщення для користувача
        notification_ids = self._user_notifications.get(user_id, [])
        return [self._notifications[nid] for nid in notification_ids if nid in self._notifications]
    
    def mark_as_read(self, notification_id: str) -> None:
        # Позначити сповіщення як прочитане
        notification = self._notifications.get(notification_id)
        if notification:
            notification.is_read = True