"""add_vehicle_damage_and_mais_injury_severity_to_involved_and_vehicles_tables

Revision ID: 423a7ea74c0a
Revises: 38b40c62043c
Create Date: 2019-01-19 22:07:01.100200

"""

# revision identifiers, used by Alembic.
revision = '423a7ea74c0a'
down_revision = '38b40c62043c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('involved', sa.Column('injury_severity_mais', sa.Integer(), nullable=True))
    op.add_column('involved_no_location', sa.Column('injury_severity_mais', sa.Integer(), nullable=True))
    op.add_column('vehicles', sa.Column('vehicle_damage', sa.Integer(), nullable=True))
    op.add_column('vehicles_no_location', sa.Column('vehicle_damage', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vehicles_no_location', 'vehicle_damage')
    op.drop_column('vehicles', 'vehicle_damage')
    op.drop_column('involved_no_location', 'injury_severity_mais')
    op.drop_column('involved', 'injury_severity_mais')
    ### end Alembic commands ###
