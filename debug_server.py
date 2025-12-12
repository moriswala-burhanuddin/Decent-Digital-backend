import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projecthub.settings')
django.setup()

from store.models import ChatSession
from store.serializers import ChatSessionSerializer

print("--- Debugging ChatSessionSerializer ---")
try:
    # Try fetching all
    sessions = ChatSession.objects.all()
    print(f"Found {sessions.count()} sessions.")
    
    # Try creating one if empty
    if sessions.count() == 0:
        print("Creating dummy session...")
        ChatSession.objects.create(title="Test Session")
        sessions = ChatSession.objects.all()

    # Try serializing
    for session in sessions:
        print(f"Serializing session {session.id}...")
        serializer = ChatSessionSerializer(session)
        print(serializer.data)
        print("Success!")
        break # Just test one
except Exception as e:
    print("!!! ERROR DURING SERIALIZATION !!!")
    import traceback
    traceback.print_exc()
