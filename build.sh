#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Run the superuser script
if [[ -f create_superuser.py ]]; then
    python create_superuser.py
fi
