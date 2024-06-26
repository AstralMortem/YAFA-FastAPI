"""init user model

Revision ID: 32ef9d7a47a9
Revises: 
Create Date: 2024-06-25 21:42:25.694874

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy.generics


# revision identifiers, used by Alembic.
revision: str = "32ef9d7a47a9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("full_name", sa.String(), nullable=False),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column(
            "gender", sa.Enum("male", "female", name="genderenum"), nullable=False
        ),
        sa.Column("height", sa.Integer(), nullable=False),
        sa.Column("weight", sa.Integer(), nullable=False),
        sa.Column("training_time", sa.Integer(), nullable=False),
        sa.Column("rest_time", sa.Integer(), nullable=False),
        sa.Column("training_per_week", sa.Integer(), nullable=False),
        sa.Column(
            "training_aim",
            sa.Enum("flesh", "fit", "lose", name="trainingaimenum"),
            nullable=False,
        ),
        sa.Column("id", fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_table(
        "oauth_account",
        sa.Column("id", fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
        sa.Column(
            "user_id", fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False
        ),
        sa.Column("oauth_name", sa.String(length=100), nullable=False),
        sa.Column("access_token", sa.String(length=1024), nullable=False),
        sa.Column("expires_at", sa.Integer(), nullable=True),
        sa.Column("refresh_token", sa.String(length=1024), nullable=True),
        sa.Column("account_id", sa.String(length=320), nullable=False),
        sa.Column("account_email", sa.String(length=320), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="cascade"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_oauth_account_account_id"),
        "oauth_account",
        ["account_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_oauth_account_oauth_name"),
        "oauth_account",
        ["oauth_name"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_oauth_account_oauth_name"), table_name="oauth_account")
    op.drop_index(op.f("ix_oauth_account_account_id"), table_name="oauth_account")
    op.drop_table("oauth_account")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###
