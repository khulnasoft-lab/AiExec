"""Change datetime type

Revision ID: 79e675cb6752
Revises: e3bc869fa272
Create Date: 2024-04-11 19:23:10.697335

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from loguru import logger
from sqlalchemy.dialects import postgresql
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision: str = "79e675cb6752"
down_revision: Union[str, None] = "e3bc869fa272"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)  # type: ignore
    table_names = inspector.get_table_names()
    # ### commands auto generated by Alembic - please adjust! ###
    if "apikey" in table_names:
        columns = inspector.get_columns("apikey")
        created_at_column = next((column for column in columns if column["name"] == "created_at"), None)
        if created_at_column is not None and isinstance(created_at_column["type"], postgresql.TIMESTAMP):
            with op.batch_alter_table("apikey", schema=None) as batch_op:
                batch_op.alter_column(
                    "created_at",
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=False,
                )
        else:
            if created_at_column is None:
                logger.warning("Column 'created_at' not found in table 'apikey'")
            else:
                logger.warning(f"Column 'created_at' has type {created_at_column['type']} in table 'apikey'")
    if "variable" in table_names:
        columns = inspector.get_columns("variable")
        created_at_column = next((column for column in columns if column["name"] == "created_at"), None)
        updated_at_column = next((column for column in columns if column["name"] == "updated_at"), None)
        with op.batch_alter_table("variable", schema=None) as batch_op:
            if created_at_column is not None and isinstance(created_at_column["type"], postgresql.TIMESTAMP):
                batch_op.alter_column(
                    "created_at",
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=True,
                )
            else:
                if created_at_column is None:
                    logger.warning("Column 'created_at' not found in table 'variable'")
                else:
                    logger.warning(f"Column 'created_at' has type {created_at_column['type']} in table 'variable'")
            if updated_at_column is not None and isinstance(updated_at_column["type"], postgresql.TIMESTAMP):
                batch_op.alter_column(
                    "updated_at",
                    existing_type=postgresql.TIMESTAMP(),
                    type_=sa.DateTime(timezone=True),
                    existing_nullable=True,
                )
            else:
                if updated_at_column is None:
                    logger.warning("Column 'updated_at' not found in table 'variable'")
                else:
                    logger.warning(f"Column 'updated_at' has type {updated_at_column['type']} in table 'variable'")

    # ### end Alembic commands ###


def downgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)  # type: ignore
    table_names = inspector.get_table_names()
    # ### commands auto generated by Alembic - please adjust! ###
    if "variable" in table_names:
        columns = inspector.get_columns("variable")
        created_at_column = next((column for column in columns if column["name"] == "created_at"), None)
        updated_at_column = next((column for column in columns if column["name"] == "updated_at"), None)
        with op.batch_alter_table("variable", schema=None) as batch_op:
            if updated_at_column is not None and isinstance(updated_at_column["type"], sa.DateTime):
                batch_op.alter_column(
                    "updated_at",
                    existing_type=sa.DateTime(timezone=True),
                    type_=postgresql.TIMESTAMP(),
                    existing_nullable=True,
                )
            else:
                if updated_at_column is None:
                    logger.warning("Column 'updated_at' not found in table 'variable'")
                else:
                    logger.warning(f"Column 'updated_at' has type {updated_at_column['type']} in table 'variable'")
            if created_at_column is not None and isinstance(created_at_column["type"], sa.DateTime):
                batch_op.alter_column(
                    "created_at",
                    existing_type=sa.DateTime(timezone=True),
                    type_=postgresql.TIMESTAMP(),
                    existing_nullable=True,
                )
            else:
                if created_at_column is None:
                    logger.warning("Column 'created_at' not found in table 'variable'")
                else:
                    logger.warning(f"Column 'created_at' has type {created_at_column['type']} in table 'variable'")

    if "apikey" in table_names:
        columns = inspector.get_columns("apikey")
        created_at_column = next((column for column in columns if column["name"] == "created_at"), None)
        if created_at_column is not None and isinstance(created_at_column["type"], sa.DateTime):
            with op.batch_alter_table("apikey", schema=None) as batch_op:
                batch_op.alter_column(
                    "created_at",
                    existing_type=sa.DateTime(timezone=True),
                    type_=postgresql.TIMESTAMP(),
                    existing_nullable=False,
                )
        else:
            if created_at_column is None:
                logger.warning("Column 'created_at' not found in table 'apikey'")
            else:
                logger.warning(f"Column 'created_at' has type {created_at_column['type']} in table 'apikey'")

    # ### end Alembic commands ###
