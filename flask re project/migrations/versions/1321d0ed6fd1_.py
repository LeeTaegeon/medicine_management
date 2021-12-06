"""empty message

Revision ID: 1321d0ed6fd1
Revises: 9d679b9a533e
Create Date: 2021-12-04 20:25:02.819856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1321d0ed6fd1'
down_revision = '9d679b9a533e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_medicine', sa.Column('user_itemname', sa.String(length=151), nullable=True))
    op.add_column('user_medicine', sa.Column('user_efcyqesitm', sa.String(length=1000), nullable=True))
    op.add_column('user_medicine', sa.Column('user_usemethodqesitm', sa.String(length=1000), nullable=True))
    op.drop_constraint('user_medicine_user_email_fkey', 'user_medicine', type_='foreignkey')
    op.drop_column('user_medicine', 'user_email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_medicine', sa.Column('user_email', sa.VARCHAR(length=32), autoincrement=False, nullable=True))
    op.create_foreign_key('user_medicine_user_email_fkey', 'user_medicine', 'users', ['user_email'], ['email'])
    op.drop_column('user_medicine', 'user_usemethodqesitm')
    op.drop_column('user_medicine', 'user_efcyqesitm')
    op.drop_column('user_medicine', 'user_itemname')
    # ### end Alembic commands ###