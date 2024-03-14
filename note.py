from datetime import datetime

class Note:
    def __init__(self, title:str, body:str, created_at:datetime, edited_at:datetime, priority:str, reminder:datetime, attachments:list[str], notebook:str, collaborators:list[str], tags:list[str]):
        self.title:str = title
        self.body:str = body
        self.created_at:str = self._set_created_at(created_at)
        self.edited_at:str = self._set_datetime(edited_at)
        self.priority:str = priority
        self.reminder:str = self._set_datetime(reminder)
        self.attachments:list[str] = attachments
        self.notebook:str = notebook
        self.collaborators:list[str] = collaborators
        self.tags:list[str] = tags
        
    def _set_created_at(self, created_at:datetime) -> str:
        if created_at is None:
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            return created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    def set_datetime(self, datetime:datetime) -> str | None:
        if datetime is None:
            self.edited_at = None
        else:
            self.edited_at datetime.strftime("%Y-%m-%d %H:%M:%S")
        return edited_at.strftime("%Y-%m-%d %H:%M:%S")