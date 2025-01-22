from sqlalchemy import (
    ForeignKey,
    MetaData,
)
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from flask_sqlalchemy import SQLAlchemy


class Base(DeclarativeBase):
    metadata = MetaData()


db = SQLAlchemy(
    model_class=Base,
    engine_options={
        # # To see generated SQL in stdout
        # "echo": True,
        # # To use Geometric queries, install geoalchemy2
        # "plugins": ["geoalchemy2"]
    },
)


class People(db.Model):
    __tablename__ = "people"
    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column()


class Groups(db.Model):
    __tablename__ = "groups"
    group_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()


class PeopleGroups(db.Model):
    __tablename__ = "people_groups"
    group_id: Mapped[int] = mapped_column(
        ForeignKey("groups.group_id"), primary_key=True
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("people.user_id"), primary_key=True)
