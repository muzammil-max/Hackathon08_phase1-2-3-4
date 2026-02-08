import uuid
from datetime import datetime
from typing import Optional, List
from enum import Enum
from sqlmodel import Field, SQLModel, Relationship

class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class TaskPriority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

# Better Auth Compatible Models
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    name: Optional[str] = None
    image: Optional[str] = None

class User(UserBase, table=True):
    id: str = Field(primary_key=True)
    emailVerified: bool = Field(default=False)
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)
    
    tasks: List["Task"] = Relationship(back_populates="owner")
    sessions: List["Session"] = Relationship(back_populates="user")

class UserCreate(UserBase):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    password: str

class UserRead(UserBase):
    id: str
    createdAt: datetime
    updatedAt: datetime

class Session(SQLModel, table=True):
    id: str = Field(primary_key=True)
    expiresAt: datetime
    token: str
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)
    ipAddress: Optional[str] = None
    userAgent: Optional[str] = None
    userId: str = Field(foreign_key="user.id")
    
    user: User = Relationship(back_populates="sessions")

class Account(SQLModel, table=True):
    id: str = Field(primary_key=True)
    accountId: str
    providerId: str
    userId: str = Field(foreign_key="user.id")
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    idToken: Optional[str] = None
    accessTokenExpiresAt: Optional[datetime] = None
    refreshTokenExpiresAt: Optional[datetime] = None
    scope: Optional[str] = None
    password: Optional[str] = None
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

class Verification(SQLModel, table=True):
    id: str = Field(primary_key=True)
    identifier: str
    value: str
    expiresAt: datetime
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

class TaskBase(SQLModel):
    title: str = Field(index=True)
    status: TaskStatus = Field(default=TaskStatus.TODO)
    priority: Optional[TaskPriority] = Field(default=TaskPriority.MEDIUM)

class Task(TaskBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner_id: str = Field(foreign_key="user.id")
    
    owner: User = Relationship(back_populates="tasks")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None

class TaskRead(TaskBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    owner_id: str
