import os
import jwt
from flask import request
from api import app
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        try:
            token = request.headers['Authorization'].split("Bearer ")[1]
        except:
            return {'message': 'a valid token is missing'}

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],
                              issuer=os.environ.get('ME', 'plasmedis-api-local'),
                              algorithms=["HS256"],
                              options={
                                  "require": ["exp", "sub", "iss", "aud"],
                                  "verify_aud": False,
                                  "verify_iat": False, "verify_nbf": False
                              })
        except jwt.exceptions.InvalidKeyError:
            return {'message': 'Secret Key is not in the proper format'}
        except jwt.exceptions.InvalidAlgorithmError:
            return {'message': 'Algorithm is not recognized by PyJWT'}
        except jwt.exceptions.ExpiredSignatureError:
            return {'message': 'Token is expired'}
        except jwt.exceptions.InvalidIssuerError:
            return {'message': 'Token has a different issuer'}
        except jwt.exceptions.MissingRequiredClaimError:
            return {'message': 'Token is missing a required claim'}
        except jwt.exceptions.DecodeError:
            return {'message': 'Token failed validation'}
        except Exception as ex:
            return {'message': 'There was a error decoding the token'}

        return f(*args, **kwargs)

    return decorator


def json_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if not request.is_json:
            return {'message': 'Espected json'}, 400
        return f(request.get_json(), *args, **kwargs)

    return decorator
