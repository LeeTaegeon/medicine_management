"""empty message

Revision ID: ba6333af6ba1
Revises: 5b0f0bbe0346
Create Date: 2021-11-30 17:11:14.697882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba6333af6ba1'
down_revision = '5b0f0bbe0346'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('email', sa.String(length=32), nullable=False),
    sa.Column('password', sa.String(length=32), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    op.drop_table('uesrs')
    op.create_foreign_key(None, 'user_medicine', 'medicine', ['medicine_id'], ['id'])
    op.create_foreign_key(None, 'user_medicine', 'users', ['user_email'], ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_medicine', type_='foreignkey')
    op.drop_constraint(None, 'user_medicine', type_='foreignkey')
    op.create_table('uesrs',
    sa.Column('email', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('email', name='uesrs_pkey')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
