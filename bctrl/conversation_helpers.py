"""A Conversation's history over the one Event log."""
from __future__ import annotations

from typing import Any

from ._generated.conversations.client import AsyncConversationsClient, ConversationsClient
from ._generated.events.client import AsyncEventsClient, EventsClient


class Conversations(ConversationsClient):
    def history(self, conversation_id: str, **kwargs: Any) -> Any:
        """The Conversation's Events (``/events?conversation=``), oldest first unless ``order`` says otherwise."""
        kwargs.setdefault("order", "asc")
        return EventsClient(client_wrapper=self._raw_client._client_wrapper).list(conversation=conversation_id, **kwargs)


class AsyncConversations(AsyncConversationsClient):
    async def history(self, conversation_id: str, **kwargs: Any) -> Any:
        kwargs.setdefault("order", "asc")
        return await AsyncEventsClient(client_wrapper=self._raw_client._client_wrapper).list(conversation=conversation_id, **kwargs)
