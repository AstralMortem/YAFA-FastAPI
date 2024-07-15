"""add routines table and relation

Revision ID: 5d4e14fa8746
Revises: c4011cdb5030
Create Date: 2024-07-15 17:01:21.699275

"""

from typing import Sequence, Union

from alembic import op
import fastapi_users_db_sqlalchemy.generics
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5d4e14fa8746"
down_revision: Union[str, None] = "c4011cdb5030"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "routines",
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("is_public", sa.Boolean(), nullable=False),
        sa.Column(
            "author_id", fastapi_users_db_sqlalchemy.generics.GUID(), nullable=True
        ),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "exercise_routine_rel",
        sa.Column("exercise_id", sa.Uuid(), nullable=False),
        sa.Column("routine_id", sa.Uuid(), nullable=False),
        sa.Column("sets", sa.Integer(), nullable=False),
        sa.Column("reps", sa.Integer(), nullable=False),
        sa.Column("reps_is_time", sa.Boolean(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["exercise_id"],
            ["exercises.id"],
        ),
        sa.ForeignKeyConstraint(
            ["routine_id"],
            ["routines.id"],
        ),
        sa.PrimaryKeyConstraint("exercise_id", "routine_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("exercise_routine_rel")
    op.drop_table("routines")
    # ### end Alembic commands ###
