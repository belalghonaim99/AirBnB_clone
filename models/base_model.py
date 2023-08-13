from datetime import datetime
import models
import uuid

class BaseModel:
    """
    Base class containing public instance attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the instance with unique ID, creation and update timestamps.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the class.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Save class data into a file for later use.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

