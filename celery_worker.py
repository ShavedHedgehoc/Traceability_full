#!/usr/bin/env python
import os
from app import celery, create_app

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app()
app.app_context().push()
