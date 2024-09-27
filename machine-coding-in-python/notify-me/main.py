from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from typing import List, Dict

# Enums
class NotificationType(Enum):
    EMAIL = 1
    SMS = 2
    PUSH = 3

class NotificationStatus(Enum):
    PENDING = 1
    SENT = 2
    FAILED = 3

# Value Objects
class UserId:
    def __init__(self, value: str):
        self.value = value

class ItemId:
    def __init__(self, value: str):
        self.value = value

# Entities
class User:
    def __init__(self, user_id: UserId, email: str, phone: str):
        self.user_id = user_id
        self.email = email
        self.phone = phone

class Item:
    def __init__(self, item_id: ItemId, name: str, is_available: bool):
        self.item_id = item_id
        self.name = name
        self.is_available = is_available

class Notification:
    def __init__(self, user: User, item: Item, notification_type: NotificationType):
        self.user = user
        self.item = item
        self.notification_type = notification_type
        self.status = NotificationStatus.PENDING
        self.created_at = datetime.now()
        self.sent_at = None

    def mark_as_sent(self):
        self.status = NotificationStatus.SENT
        self.sent_at = datetime.now()

    def mark_as_failed(self):
        self.status = NotificationStatus.FAILED

# Repositories
class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: UserId) -> User:
        pass

    @abstractmethod
    def save_user(self, user: User) -> None:
        pass

class ItemRepository(ABC):
    @abstractmethod
    def get_item(self, item_id: ItemId) -> Item:
        pass

    @abstractmethod
    def save_item(self, item: Item) -> None:
        pass

    @abstractmethod
    def get_subscribed_users(self, item_id: ItemId) -> List[User]:
        pass

class NotificationRepository(ABC):
    @abstractmethod
    def save_notification(self, notification: Notification) -> None:
        pass

    @abstractmethod
    def get_pending_notifications(self) -> List[Notification]:
        pass

# Services
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, notification: Notification) -> bool:
        pass

class EmailNotificationService(NotificationService):
    def send_notification(self, notification: Notification) -> bool:
        # Implementation for sending email notification
        print(f"Sending email notification to {notification.user.email}")
        return True

class SMSNotificationService(NotificationService):
    def send_notification(self, notification: Notification) -> bool:
        # Implementation for sending SMS notification
        print(f"Sending SMS notification to {notification.user.phone}")
        return True

class PushNotificationService(NotificationService):
    def send_notification(self, notification: Notification) -> bool:
        # Implementation for sending push notification
        print(f"Sending push notification to user {notification.user.user_id.value}")
        return True

# Factories
class NotificationServiceFactory:
    @staticmethod
    def create_service(notification_type: NotificationType) -> NotificationService:
        if notification_type == NotificationType.EMAIL:
            return EmailNotificationService()
        elif notification_type == NotificationType.SMS:
            return SMSNotificationService()
        elif notification_type == NotificationType.PUSH:
            return PushNotificationService()
        else:
            raise ValueError("Invalid notification type")

# Use Cases
class NotifyMeUseCase:
    def __init__(self, user_repo: UserRepository, item_repo: ItemRepository, notification_repo: NotificationRepository):
        self.user_repo = user_repo
        self.item_repo = item_repo
        self.notification_repo = notification_repo

    def execute(self, user_id: UserId, item_id: ItemId, notification_type: NotificationType) -> None:
        user = self.user_repo.get_user(user_id)
        item = self.item_repo.get_item(item_id)
        
        if item.is_available:
            raise ValueError("Item is already available")

        notification = Notification(user, item, notification_type)
        self.notification_repo.save_notification(notification)

class ProcessNotificationsUseCase:
    def __init__(self, notification_repo: NotificationRepository):
        self.notification_repo = notification_repo

    def execute(self) -> None:
        pending_notifications = self.notification_repo.get_pending_notifications()
        for notification in pending_notifications:
            service = NotificationServiceFactory.create_service(notification.notification_type)
            success = service.send_notification(notification)
            if success:
                notification.mark_as_sent()
            else:
                notification.mark_as_failed()
            self.notification_repo.save_notification(notification)

class UpdateItemAvailabilityUseCase:
    def __init__(self, item_repo: ItemRepository, notification_repo: NotificationRepository):
        self.item_repo = item_repo
        self.notification_repo = notification_repo

    def execute(self, item_id: ItemId, is_available: bool) -> None:
        item = self.item_repo.get_item(item_id)
        item.is_available = is_available
        self.item_repo.save_item(item)

        if is_available:
            subscribed_users = self.item_repo.get_subscribed_users(item_id)
            for user in subscribed_users:
                notification = Notification(user, item, NotificationType.EMAIL)  # Default to email
                self.notification_repo.save_notification(notification)

# Example usage
class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: Dict[str, User] = {}

    def get_user(self, user_id: UserId) -> User:
        return self.users.get(user_id.value)

    def save_user(self, user: User) -> None:
        self.users[user.user_id.value] = user

class InMemoryItemRepository(ItemRepository):
    def __init__(self):
        self.items: Dict[str, Item] = {}
        self.subscriptions: Dict[str, List[User]] = {}

    def get_item(self, item_id: ItemId) -> Item:
        return self.items.get(item_id.value)

    def save_item(self, item: Item) -> None:
        self.items[item.item_id.value] = item

    def get_subscribed_users(self, item_id: ItemId) -> List[User]:
        return self.subscriptions.get(item_id.value, [])

class InMemoryNotificationRepository(NotificationRepository):
    def __init__(self):
        self.notifications: List[Notification] = []

    def save_notification(self, notification: Notification) -> None:
        self.notifications.append(notification)

    def get_pending_notifications(self) -> List[Notification]:
        return [n for n in self.notifications if n.status == NotificationStatus.PENDING]

# Client code
user_repo = InMemoryUserRepository()
item_repo = InMemoryItemRepository()
notification_repo = InMemoryNotificationRepository()

notify_me_use_case = NotifyMeUseCase(user_repo, item_repo, notification_repo)
process_notifications_use_case = ProcessNotificationsUseCase(notification_repo)
update_item_availability_use_case = UpdateItemAvailabilityUseCase(item_repo, notification_repo)

# Create a user and an item
user = User(UserId("user1"), "user@example.com", "1234567890")
user_repo.save_user(user)

item = Item(ItemId("item1"), "Example Item", False)
item_repo.save_item(item)

# User clicks "Notify Me" button
notify_me_use_case.execute(UserId("user1"), ItemId("item1"), NotificationType.EMAIL)

# Item becomes available
update_item_availability_use_case.execute(ItemId("item1"), True)

# Process notifications
process_notifications_use_case.execute()