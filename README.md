# Notes

On alembic.ini, change `prepend_sys_path` to `..` for finding the module. 
Add each table to the imports
alembic revision --autogenerate
alembic upgrade head
