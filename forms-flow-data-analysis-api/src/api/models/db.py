"""Create SQLAlchenmy and Schema managers.

These will get initialized by the application using the models
"""

# from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# by convention in the Flask community these are lower case,
# whereas pylint wants them upper case
# ma = Marshmallow()  # pylint: disable=invalid-name
db = SQLAlchemy()  # pylint: disable=invalid-name
migrate = Migrate()  # pylint: disable=invalid-name
